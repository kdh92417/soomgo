from django.db import models

class Account(models.Model):
    name        = models.CharField(max_length = 100)
    email       = models.EmailField(max_length = 200)
    password    = models.CharField(max_length = 200)
    is_provider = models.BooleanField(default = False)
    kakao_id    = models.IntegerField(default = None, null = True)
    created_at  = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'accounts'

class ProviderInfo(models.Model):
    name                           = models.CharField(max_length = 100, default = '')
    email                          = models.EmailField(max_length = 200, default = '')
    password                       = models.CharField(max_length = 200, default = '')
    gender                         = models.ForeignKey('Gender', on_delete=models.SET_NULL, null = True)
    phone_number                   = models.CharField(max_length = 50, default='01000000000')
    career                         = models.IntegerField(default=1)
    employee                       = models.IntegerField(default=1)
    is_business                    = models.BooleanField(default = False)
    is_identity                    = models.BooleanField(default = False)
    is_certificate                 = models.BooleanField(default = False)
    address                        = models.ForeignKey('Address', on_delete=models.SET_NULL, null = True)
    provider_time                  = models.ManyToManyField('Time', through = 'ProviderTime')
    created_at                     = models.DateTimeField(auto_now_add = True)
    provider_info_third_category   = models.ManyToManyField('category.ThirdCategory',
                through = 'category.ProviderInfoThirdCategory',
                related_name='info_category')
    order                          = models.ManyToManyField('order.Order',
                through = 'order.ProviderInfoOrder',
                related_name='provider_order')
    payment                        = models.ManyToManyField('Payment',
                through = 'providerInfoPayment',
                related_name='provider_payment')

    class Meta:
        db_table = 'provider_infos'

class Address(models.Model):
    address    = models.CharField(max_length = 300)
    si         = models.ForeignKey('Si', on_delete=models.SET_NULL, null = True)
    gu         = models.ForeignKey('Gu', on_delete=models.SET_NULL, null = True)
    dong       = models.ForeignKey('Dong', on_delete=models.SET_NULL, null = True)
    x_position = models.DecimalField(max_digits=22, decimal_places=16, null = True)
    y_position = models.DecimalField(max_digits=22, decimal_places=16, null = True)

    class Meta:
        db_table = 'addresses'

class Si(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'si'

class Gu(models.Model):
    si   = models.ForeignKey('Si', on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'gu'

class Dong(models.Model):
    gu   = models.ForeignKey('Gu', on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'dong'

class Gender(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'gender'

class ProviderInfoPayment(models.Model):
    provider_info = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null = True)
    payment       = models.ForeignKey('Payment', on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'provider_infos_payments'

class SubImages(models.Model):
    provider_info = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null = True)
    image_url     = models.URLField(max_length = 2000)

    class Meta:
        db_table  = 'sub_images'

class ProfileImage(models.Model):
    provider_info = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null = True)
    image_url     = models.URLField(max_length = 2000)

    class Meta:
        db_table = 'profile_images'

class Time(models.Model):
    start_time = models.IntegerField()
    last_time  = models.IntegerField()

    class Meta:
        db_table = 'times'

class ProviderTime(models.Model):
    time     = models.ForeignKey('Time', on_delete=models.SET_NULL, null = True)
    provider = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null=True)

class Profile(models.Model):
    provider_info = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null= True)
    introduce     = models.CharField(max_length = 2000)
    description   = models.CharField(max_length = 6000)

    class Meta:
        db_table = 'profiles'

class Review(models.Model):
    provider_info = models.ForeignKey('ProviderInfo', on_delete=models.SET_NULL, null= True)
    account       = models.ForeignKey('Account', on_delete=models.SET_NULL, null= True)
    score         = models.DecimalField(max_digits=2, decimal_places=1)
    comment       = models.CharField(max_length = 3000)
    created_at    = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'reviews'

class Payment(models.Model):
    method = models.CharField(max_length = 50)

    class Meta:
        db_table = 'payments'

class Campaign(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'campaings'
