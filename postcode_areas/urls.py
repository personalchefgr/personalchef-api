from django.urls import path

from . import views

app_name = "postcode_areas"
urlpatterns = [
    path('', views.PostcodeAreaList.as_view(), name="postcode_area-list"),
    path('postcode-area/<int:postcode>', views.PostcodeAreaDetails.as_view(), name="postcode_area-details"),
]