from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from . import views

app_name="users"
urlpatterns = [
    path("", views.UserList.as_view(), name="user-list"),
    # path("user/<int:id>", views.UserDetails.as_view(), name="user-details"),
    path("user", views.UserDetails.as_view(), name="user-details"),
    path("user/register", views.UserRegister.as_view(), name="user-register"),
    # JWT routes
    path('user/login', 
        jwt_views.TokenObtainPairView.as_view(), 
        name='token_obtain_pair'),
    path('user/login/refresh', 
        jwt_views.TokenRefreshView.as_view(), 
        name='token_refresh'),
    path("user/logout", views.UserLogOut.as_view(), name="user-logout"),
]
