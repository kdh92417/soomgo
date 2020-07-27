import json, jwt


from my_settings import (
        ALGORITHM,
        SECRET_KEY
)
from .models import *

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def response(message, status):
    return JsonResponse({'message' : message}, status = 200)

def Login_Required(func):
    def decorator_func(self, request, *arg, **kwargs):
        access_token = request.headers.get('Authorization', None)

        if access_token is None:
            return JsonResponse({'message' : 'MISSING_TOKEN'}, status = 401)

        try:
            payload = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user_id = payload['id']
            request.user = ProviderInfo.objects.get(id = user_id)
        
        except jwt.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 402)
        
        return func(self, request, *arg, **kwargs)
    return decorator_func
