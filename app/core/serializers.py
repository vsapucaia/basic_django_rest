from rest_framework import serializers
from .models import Bucketlist, City


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Bucketlist
        fields = ("id", "name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")


class CitySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = City
        fields = ("id", "name", "state", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
