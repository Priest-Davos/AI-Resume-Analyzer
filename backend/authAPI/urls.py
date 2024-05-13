# urls.py
from django.urls import path
from .views import CreateUserView, PasswordResetRequestView, PasswordResetConfirmAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # Import views for JWT token management

urlpatterns = [
  
    path("user/register/", CreateUserView.as_view(), name="register"),  # Map the URL '/api/user/register/' to the CreateUserView for user registration
    path("token/", TokenObtainPairView.as_view(), name="get_token"),  # Map the URL '/api/token/' to the TokenObtainPairView for obtaining JWT tokens
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),  # Map the URL '/api/token/refresh/' to the TokenRefreshView for refreshing JWT tokens
  
    # URL pattern for password reset request
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password_reset_request'),

    # URL pattern for password reset confirmation
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),
]
