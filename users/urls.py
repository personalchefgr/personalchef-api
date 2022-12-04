from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from . import views

app_name="users"
urlpatterns = [
    path("", 
        views.UserList.as_view(), 
        name="user-list"),

    path("user", 
        views.UserDetails.as_view(), 
        name="user-details"),

    path("user/profile", 
        views.UserProfile.as_view(), 
        name="user-profile"),

    path("user/register", 
        views.UserRegister.as_view(), 
        name="user-register"),

    path('user/token', 
        jwt_views.TokenObtainPairView.as_view(), 
        name='token_obtain_pair'),

    path('user/token/refresh', 
        jwt_views.TokenRefreshView.as_view(), 
        name='token_refresh'),

    path("user/login", 
        views.UserLogIn.as_view(), 
        name="user-login"),
        
    path("user/logout", 
        views.UserLogOut.as_view(), 
        name="user-logout"),
]
