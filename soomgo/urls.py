from django.urls import path, include

urlpatterns = [
   path('category', include('category.urls')),
   path('account', include('account.urls'))
]