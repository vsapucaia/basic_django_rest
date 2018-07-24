from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BucketlistSerializer, CitySerializer
from .models import Bucketlist, City
import json
from django.http import HttpResponse


def find_values(key, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[key])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class TranslateJSON(APIView):
    """
    Searches for every city inside a json file and loads to the database.
    There's an example file in app/core/json_examples
    """
    def post(self, request, *args, **kwargs):
        posted_data = json.dumps(self.request.data)
        return_data = find_values('City', posted_data)

        for item in return_data:
            serializer = CitySerializer(data=item)
            if serializer.is_valid():
                serializer.save()

        return Response(status=200, data=return_data)
