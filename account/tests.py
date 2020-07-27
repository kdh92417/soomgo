from django.test import TestCase

from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
from .models import *
import json
import jwt
import bcrypt
import requests

class AccounSignUpTest(TestCase):
    def setUp(self):
        client = Client()
        Account.objects.create(
            email    = 'what_is@naver.com',
            name     = 'pjkfckr',
            password = 'dwqdqwf'
        )
        
    def tearDown(self):
        Account.objects.all().delete()

    def test_get_account_signup_view(self):
        client = Client()
        user = {
            'email' : 'pjkfck@nav.com',
            'name'  : 'whatis',
            'password' : 'dwqdqzxc'
        }
        response = client.post('/account/sign-up', json.dumps(user), content_type = 'applications/json')
        self.assertEqual(response.status_code, 200)

    def test_error_400_account_signup_view(self):
        client = Client()
        user = {
            'emaila' : 'park@naver.com',
            'namesa'  : 'whatisd',
            'password' : 'dwqdqsdzxc'
        }
        response = client.post('/account/sign-up', json.dumps(user), content_type = 'applications/json')
        self.assertEqual(response.status_code, 400)

    def test_error_401_account_signup_view(self):
        client = Client()
        user = {
            'email' : 'what_is@naver.com',
            'name'  : 'pjkfckr',
            'password' : 'dwqdq'
        }
        response = client.post('/account/sign-up', json.dumps(user), content_type = 'applications/json')
        self.assertEqual(response.status_code, 401)

    def test_error_402_account_signup_view(self):
        client = Client()
        user = {
            'email' : 'parksang.com',
            'name'  : 'whatis',
            'password' : 'dwqdqzxc'
        }
        response = client.post('/account/sign-up', json.dumps(user), content_type = 'applications/json')
        self.assertEqual(response.status_code, 402)

class AccounSignInTest(TestCase):
    def setUp(self):
        client = Client()
        Account.objects.create(
            email='what_is@naver.com',
            name  = 'pjkfckr',
            password = bcrypt.hashpw('dwqdqwf'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )

    def tearDown(self):
        Account.objects.all().delete()

    def test_get_account_signin_view(self):
        client = Client()
        user_data = {
            'email' : 'what_is@naver.com',
            'name'  : 'pjkfckr',
            'password' : 'dwqdqwf'
        }
        response = client.post(
                '/account/sign-in', 
                json.dumps(user_data), 
                content_type = 'applications/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_error_400_account_signin_view(self):
        client = Client()
        user_data = {
            'emaila' : 'what_is@naver.com', 
            'namesas'  : 'pjkfckr', 
            'passwordodsa' : 'dwqdqwf'
        }
        response = client.post(
                '/account/sign-in', 
                json.dumps(user_data), 
                content_type = 'applications/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_error_401_account_signin_view(self):
        client = Client()
        user_data = {
            'email' : 'what_is@naver.com', 
            'name'  : 'pjkfckr', 
            'password' : 'zxczxc'
        }
        response = client.post(
                '/account/sign-in', 
                json.dumps(user_data), 
                content_type = 'applications/json'
        )
        self.assertEqual(response.status_code, 401)

    def test_error_402_account_signin_view(self):
        client = Client()
        user_data = {
                'email' : 'whatis@naver.com', 
                'name'  : 'pjkfckr', 
                'password' : 'dwqdqwf'
        }
        response = client.post(
                '/account/sign-in', 
                json.dumps(user_data), 
                content_type = 'applications/json'
        )
        self.assertEqual(response.status_code, 402)

class KakaoSignInTest(TestCase):
    def setUp(self):
        Account.objects.create(
                email = 'parkji@naver.com',
                kakao_id = '123123123',
        )

    def tearDown(self):
        Account.objects.filter(email = 'parkji@naver.com').delete()
    
    @patch('account.views.KakaoSignInView._get_kakao_user_info')
    def test_kakao_account(self, mock__get_kakao_user_info):
        client = Client()
        mock__get_kakao_user_info.return_value = {
                'id' : '1232332',
                'kakao_account' : {'email' : 'pjkdsa@naver.com'}
        }

        header = {'HTTP_Authorization' : '123123'}

        body = {
            'id_token' : '123123222'
        }
        response = client.post(
                '/account/kakao', 
                content_type = 'application/json', 
                data = body,
                **header
        )
        self.assertEqual(response.status_code, 200)

    @patch('account.views.KakaoSignInView._get_kakao_user_info')
    def test_kakao_account_error_400(self, mock__get_kakao_user_info):
        client = Client()
        mock__get_kakao_user_info.return_value = {
                'id' : '1232332',
                'kakao_account' : {'emaill' : 'pjkdsa@naver.com'}
        }

        header = {'HTTP_Authorization' : 'dwqd12'}

        body = {
            'id_token' : '123123'
        }
        response = client.post(
                '/account/kakao',
                content_type = 'application/json',
                data = body,
                **header
        )
        self.assertEqual(response.status_code, 400)

    @patch('account.views.KakaoSignInView._get_kakao_user_info')
    def test_kakao_account_error_401(self, mock__get_kakao_user_info):
        client = Client()
        mock__get_kakao_user_info.return_value = {
                'id' : '12332321',
                'kakao_account' : {'email' : 'pjkfr@naver.com'}
        }

        header = {'HTTP_Authorization' : None}

        body = {
            'id_token' : '123123222'
        }
        response = client.post(
                '/account/kakao',
                content_type = 'application/json',
                data = body,
                **header
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
                {'message' : 'MISSING_KAKAO_TOKEN'}
        )

