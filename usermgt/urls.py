from django.urls import path
from rest_framework_simplejwt import views as jwt_views

URLPATTERNS = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refreshtoken/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
]
