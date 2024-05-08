from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

class Authentication:

    
    def authenticate(self, request):
        import pdb;pdb.set_trace()
        # Get the token from the request headers
        token = request.headers.get('Authorization')

        if not token:
            raise AuthenticationFailed('Invalid token')
        
        # Implement your token validation logic here
        try:
            user_id = Token.objects.filter(key=token).first()
            if user_id is None:
                raise AuthenticationFailed('Invalid token')

            else:
                user_id = user_id.user_id  # Assuming you have a custom token field in your User model

            user = User.objects.get(id=user_id)

        except (User.DoesNotExist, AuthenticationFailed):
            raise AuthenticationFailed

        return (user, None)