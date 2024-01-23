from django.urls import path

from . import views

app_name="contact_form"
urlpatterns = [
    path(
        'message', 
        views.MessageDetails.as_view(), 
        name="message-details"
    ),
]