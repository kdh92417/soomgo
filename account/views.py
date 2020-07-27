import requests
import json
import jwt
import bcrypt

from django.http import (
        HttpResponse,
        JsonResponse
)
from django.views import View
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import *
from .utils import Login_Required
from my_settings import (
        ALGORITHM,
        SECRET_KEY
)

class KakaoSignInView(View):
    def _get_kakao_user_info(self, id_token):
        headers         = {'Authorization' : f'Bearer {id_token}'}
        url             = "https://kapi.kakao.com/v2/user/me"
        response        = requests.request("POST", url, headers = headers)
        kakao_user_info = response.json()
        return kakao_user_info

    def post(self, request):
        try:
            kakao_id_token = request.headers.get('Authorization', None)

            if kakao_id_token is None:
                return JsonResponse({'message': 'MISSING_KAKAO_TOKEN'}, status=401)

            kakao_user_info = self._get_kakao_user_info(kakao_id_token)

            if 'code' in kakao_user_info:
                message = kakao_user_info['msg']
                return JsonResponse({'message' : message}, status=402)

            kakao_user_email = kakao_user_info['kakao_account']['email']
            kakao_user_id = kakao_user_info['id']

            if not Account.objects.filter(kakao_id = kakao_user_id).exists():
                user_id = Account.objects.create(
                        email       = kakao_user_email,
                        kakao_id    = kakao_user_id,
                        is_provider = False
                        ).id
            else:
                user_id = Account.objects.filter(kakao_id = kakao_user_id).id

            access_token = jwt.encode({'user_id' : user_id}, SECRET_KEY, ALGORITHM).decode('utf-8')
            return JsonResponse({'access_token' : access_token}, status = 200)

        except KeyError:
            return HttpResponse(status = 400)

class SignUpView(View):
    def _encrypt(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def post(self, request):
        user_data = json.loads(request.body)
        try:
            validate_email(user_data['email'])

            if not Account.objects.filter(email = user_data['email']).filter(is_provider = False).exists():
                encrypt_pw = self._encrypt(user_data['password']).decode('utf-8')
                Account.objects.create(
                        email       = user_data['email'],
                        password    = encrypt_pw,
                        name        = user_data['name'],
                )
                return HttpResponse(status = 200)
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

        except ValidationError:
            return JsonResponse({"message" : "INVALID_EMAIL"}, status = 402)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEY"}, status = 400)

class SignInView(View):
    def post(self, request):
        user_data = json.loads(request.body)
        try:
            if Account.objects.filter(email = user_data['email']).exists():
                user = Account.objects.get(email = user_data['email'])
                provider = user.is_provider

                if bcrypt.checkpw(user_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
                    return JsonResponse({'access_token' : access_token}, status = 200)
                    
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 401)
            
            if ProviderInfo.objects.filter(email = user_data['email']).exists():
                user = ProviderInfo.objects.get(email = user_data['email'])

                if bcrypt.checkpw(user_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
                    return JsonResponse({'access_token' : access_token}, status = 200)
                

                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 401)
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 402)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)

class ProviderSignUpView(View):
    def _encrypt(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def post(self, request):
        user_data = json.loads(request.body)
        try:
            validate_email(user_data['email'])
            
            encrypt_pw = self._encrypt(user_data['password']).decode('utf-8')

            addr_id = Address.objects.get_or_create(
                address = user_data['address']
            )[0]
            ProviderInfo.objects.create(
                email    = user_data['email'],
                password = encrypt_pw,
                address = addr_id
            )

            if Account.objects.filter(email = user_data['email']).exists():
                user = Account.objects.get(email = user_data['email'])
                user.is_provider = True
                user.save()
            return HttpResponse(status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)
        
        except ValidationError:
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 401)

class ProviderProfile(View):
    def _encrypt(self, password):
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    @Login_Required
    def get(self, request):
        user = request.user
        info = {
            'address' : user.address.address,
            'is_business': user.is_business,
            'is_identity': user.is_identity,
            'is_certificate' : user.is_certificate
        }
        return JsonResponse({'provider_profile' : info}, status = 200)
    
    @Login_Required
    def post(self, request):
        current_user = request.user
        modify_user  = json.loads(request.body)

        current_user.address.address = modify_user['address']
        current_user.career = modify_user['career']
        current_user.employee = modify_user['employee']
        current_user.is_business = modify_user['is_business']
        current_user.is_identity = modify_user['is_identity']
        current_user.is_certificate = modify_user['is_certificate']
        current_user.profile_set.values('introduce')[0] = modify_user['introduce']

        current_user.save()

        return JsonResponse({'message' : 'PROFILE_UPDATE'}, status = 200)


class ListView(View):
    def get(self, request):
        list_info = ProviderInfo.objects.prefetch_related('profileimage_set').prefetch_related('profile_set')
        list_provider = [
                {
                "provider_id"  : info.id,
                "provider_name": info.name,
                "profile_img"  : info.profileimage_set.values('image_url').first(),
                "introduce"    : info.profile_set.first().introduce
                } for info in list_info
                ]
        return JsonResponse({"pro_list":list_provider}, status=200)

class ProviderView(View):
    def get(self, request, req_pro_id):
        provider_group = ProviderInfo.objects.select_related('address').prefetch_related('profile_set').prefetch_related('subimages_set').get(id=req_pro_id)

        #image_url에 null값이 있어서 오류를 해결하기 위한 조건문
        if provider_group.profileimage_set.first() is None:
            profile_img = ''
        else:
            profile_img = provider_group.profileimage_set.first().image_url

        provider_search = {
                "provider_name" : provider_group.name,
                "profile_img"   : profile_img,
                "introduce"     : provider_group.profile_set.first().introduce,
                "si"            : provider_group.address.si.name,
                "gu"            : provider_group.address.gu.name,
                "career"        : provider_group.career,
                "employee"      : provider_group.employee,
                "description"   : provider_group.profile_set.first().description,
                "sub_img"       : [group.image_url for group in provider_group.subimages_set.all()]
                }
        return JsonResponse({"provider_search": provider_search}, status=200)