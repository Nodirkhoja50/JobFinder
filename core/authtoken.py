from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone





#this return left time
def expires_in(token):
    token = Token.objects.get(key=token)
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(days = 7) - time_elapsed
    return left_time

# token checker if token expired or not
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds = 0)

# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    token = Token.objects.get(key = token)
    is_expired = is_token_expired(token)
    if is_expired:
        
        token.delete()
        token = Token.objects.create(user = token.user)
    return is_expired, token


class ExpiringTokenAuthentication(TokenAuthentication):

    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    def authenticate(self, request):
        # Custom authentication logic
        # Retrieve the token from the request header or any other source
        token = request.headers.get("token")
        token = Token.objects.get(key = token)
        is_expired, token = token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")
        # Perform token validation and retrieve the associated user
        user =Token.objects.get(key=token).user

        if user is None:
            raise AuthenticationFailed('Invalid token')

        
        return (user, token)
    
    '''def authenticate_credentials(self, key):
        try:
            print(key)
            token = Token.objects.get(key = key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")
        
        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        is_expired, token = token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")
        
        return (token.user, token)
    
    '''