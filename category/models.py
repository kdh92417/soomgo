from django.db import models

class FirstCategory(models.Model):
    name = models.CharField(max_length = 100)
<<<<<<< HEAD
    image_url = models.URLField(max_length = 300, null=True)
=======
>>>>>>> dbac424... [Fix] migrate models

    class Meta:
        db_table = 'first_categories'

class SecondCategory(models.Model):
    first_category = models.ForeignKey('FirstCategory', on_delete=models.SET_NULL, null=True)
    name           = models.CharField(max_length = 100)

    class Meta:
        db_table = 'second_categories'

class ThirdCategory(models.Model):
    second_category = models.ForeignKey('SecondCategory', on_delete=models.SET_NULL, null=True)
    name            = models.CharField(max_length = 100)
    image_url       = models.URLField(max_length = 2000)
    campaign        = models.ForeignKey('account.Campaign', on_delete=models.SET_NULL, null=True)
<<<<<<< HEAD
    is_popular      = models.BooleanField(default=False)
=======
>>>>>>> dbac424... [Fix] migrate models

    class Meta:
        db_table = 'third_categories'

class Question(models.Model):
    category        = models.ForeignKey('ThirdCategory', on_delete=models.SET_NULL, null=True)
    question        = models.CharField(max_length=1000)
    answer_question = models.ManyToManyField('Answer', through='order.RequestSurvey')

    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    question_answer = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    answer          = models.CharField(max_length=2000)

    class Meta:
        db_table = 'answers'

class TypeName(models.Model):
    name = models.CharField(max_length=100)
    answer_type = models.ManyToManyField('Answer', through='AnswerType')

    class Meta:
        db_table = 'types'

class AnswerType(models.Model):
    answer_id = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)
    type_id   = models.ForeignKey('TypeName', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'answer_types'

class ProviderInfoThirdCategory(models.Model):
    third_category = models.ForeignKey('ThirdCategory', on_delete=models.SET_NULL, null=True)
    provider_info  = models.ForeignKey('account.ProviderInfo', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'provider_infos_first_categories'

