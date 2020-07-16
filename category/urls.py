from django.urls    import path
from .views         import *

urlpatterns = [
    path('', TotalListView.as_view()),  
]
