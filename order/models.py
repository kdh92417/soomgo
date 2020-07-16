from django.db import models

class Order(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey('account.Address', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class RequestSurvey(models.Model):
    question   = models.ForeignKey('category.Question', on_delete=models.SET_NULL, null=True)
    answer     = models.ForeignKey('category.Answer', on_delete=models.SET_NULL, null=True)
    order      = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'requests_survey'

class ProviderInfoOrder(models.Model):
    provider_info = models.ForeignKey('account.ProviderInfo', on_delete=models.SET_NULL, null=True)
    order         = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    price         = models.DecimalField(max_digits=12, decimal_places=2)
    is_selected   = models.BooleanField(default=False)

    class Meta:
        db_table = 'provider_infos_orders'

