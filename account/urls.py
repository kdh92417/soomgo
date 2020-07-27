from django.urls import path
from account.views import (
    ListView,
    ProviderView,
)
from .views import (
    KakaoSignInView,
    SignUpView,
    SignInView,
    ProviderSignUpView,
    ProviderProfile
)

urlpatterns = [
    path('/prolist', ListView.as_view()),
    path('/proinfo/<slug:req_pro_id>', ProviderView.as_view()),
    path('/kakao', KakaoSignInView.as_view()),
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/provider', ProviderSignUpView.as_view()),
    path('/profile', ProviderProfile.as_view())
]
    
