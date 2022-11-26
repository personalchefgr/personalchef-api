from django.urls import path

from . import views

app_name = "postcode_areas"
urlpatterns = [
    path("<int:postcode>", views.PostcodeAreaDetails.as_view(), name="postcode_area-details"),
]