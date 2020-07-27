import json

from django.db.models   import Q
from django.views       import View
from django.http        import (
    JsonResponse,
    HttpResponse
)
from django.test        import (
    TestCase, 
    Client
)

from category.models import *

class TotalListView(View):
    def get(self, request):
        try:
            category_name = request.GET.get('category', None)
            category_list = FirstCategory.objects.prefetch_related('secondcategory_set__thirdcategory_set').filter(name=category_name).first()
            second_items  = category_list.secondcategory_set.all()
            
            main_category = {
                'category_name' : category_list.name,
                'category_url'  : category_list.image_url
            }
            
            popular_item = [{
                'detail_category' : item.name,
                'image_url' : item.image_url 
            } for second_item in second_items for item in second_item.thirdcategory_set.filter(is_popular=1)]

            category_item = [{
                'sub_category' : second_item.name,
                'detail_category' : [ third.name for third in second_item.thirdcategory_set.all()]
            } for second_item in second_items]
    
            return JsonResponse({"main_category" : main_category, "category_list": category_item, "popular_list" : popular_item}, status = 200)
        
        except KeyError:
            return HttpResponse(status = 400)
        
        


        
