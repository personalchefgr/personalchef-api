from django.urls import path, include

from . import views

app_name="users"
urlpatterns = [
    path("", views.UserList.as_view(), name="user-list"),
    # path("user/<int:id>", views.UserDetails.as_view(), name="user-details"),
    path("user", views.UserDetails.as_view(), name="user-details"),
    path("user/register", views.UserRegister.as_view(), name="user-register"),
    path("user/login", views.UserLogIn.as_view(), name="user-login"),
    path("user/logout", views.UserLogOut.as_view(), name="user-logout"),
]
