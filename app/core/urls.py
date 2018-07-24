# from rest_framework import routers
# from app.core.views import TranslateJSON
#
# router = routers.DefaultRouter()
# router.register(r'translate', TranslateJSON, base_name='translate')
#
# urlpatterns = router.urls

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.core.views import CreateView, DetailsView, TranslateJSON
from django.urls import path

urlpatterns = {
    url(r"^bucketlists/$", CreateView.as_view(), name="create"),
    url(r"^bucketlists/(?P<pk>[0-9]+)/$", DetailsView.as_view(), name="details"),
    path("translate/", TranslateJSON.as_view(), name='translate')
}

urlpatterns = format_suffix_patterns(urlpatterns)
