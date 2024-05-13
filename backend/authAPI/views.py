
from django.contrib.auth.models import User
from .serializers import UserSerializer,PasswordResetSerializer
from rest_framework import generics , status
from rest_framework.views import APIView


from rest_framework.permissions import IsAuthenticated, AllowAny  # Import permission classes from Django REST Framew

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import smart_bytes , smart_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.urls import reverse
from rest_framework.response import Response
from django.core.mail import send_mail


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

 # View to handle password reset request.
class PasswordResetRequestView(generics.GenericAPIView):

    # Serializer class for handling password reset request data
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        """
        Handle POST requests for password reset.

        :param request: HTTP request object
        :return: HTTP response with reset URL or validation errors
        """

        # Initialize serializer with request data
        serializer = self.serializer_class(data=request.data)

        # Validate serializer data
        if serializer.is_valid():
            # Extract email address from validated data
            email = serializer.validated_data['email']

            try:
                # Retrieve user object associated with the email address
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # If user does not exist, return error response
                return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Generate unique URL for password reset confirmation page
            uid = urlsafe_base64_encode(smart_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})

            # Here you would typically send the password reset email to the user's email address
            subject = 'Password Reset'
            message = f'Click the following link to reset your password: {reset_url}'
            from_email = 'priestdavos1@gmail.com'
            to_email = [email]
            send_mail(subject, message, from_email, to_email)

            # Return response with reset URL
            return Response({"reset_url": reset_url}, status=status.HTTP_200_OK)

        # If serializer data is invalid, return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        # Decode email to get user object
        uid = smart_str(urlsafe_base64_decode(email))
        try:
            user = User.objects.get(pk=uid)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Verify token
        if default_token_generator.check_token(user, token):
            # Token is valid, update user's password
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
