from django.test import TestCase, Client
from .models     import (
    FirstCategory,
    SecondCategory,
    ThirdCategory
)


class JustTest(TestCase):
    def setUp(self):
        FirstCategory.objects.create(
            id        = 1,
            name      = 'main',
            image_url = 'www.naver.com'
        )
        
        SecondCategory.objects.create(
            id                = 1,
            first_category = FirstCategory.objects.get(id=1),
            name              = 'sub'
        )
        
        ThirdCategory.objects.create(
            id              = 1,
            second_category = SecondCategory.objects.get(id=1),
            name = 'third',
            image_url = 'www.google.com',
            is_popular = True
        )
        
    def tearDown(self):
        FirstCategory.objects.all().delete()
        SecondCategory.objects.all().delete()
        ThirdCategory.objects.all().delete()
    
    def test_totallist_get_success(self):
        client = Client()
        response = client.get('/category?category=main', content_type = 'application/json')
        result = {
            'main_category' : {
                'category_name' : 'main',
                'category_url'  : 'www.naver.com'
            },
            'category_list' : [
                {'sub_category'   : 'sub', 
                 'detail_category': ['third']
                 }
                ], 
            'popular_list': [
                {'detail_category' : 'third', 
                 'image_url'       : 'www.google.com'
                 }
                ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)
        
    def test_totallist_get_not_found(self):
        client = Client()
        response = client.get('/categor?category=main', content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
