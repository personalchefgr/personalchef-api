from django.urls import path

from . import views

app_name="newsletter"
urlpatterns = [
    path('ping',
        views.PingAccountView.as_view(),
        name="ping"),
        
    path('subscribe', 
        views.SubscribeView.as_view(), 
        name="subscribe"),
]

