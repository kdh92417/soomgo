# Generated by Django 3.0.7 on 2020-07-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20200715_1045'),
        ('order', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_question',
            field=models.ManyToManyField(through='order.RequestSurvey', to='category.Answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.ThirdCategory'),
        ),
        migrations.AddField(
            model_name='providerinfothirdcategory',
            name='provider_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo'),
        ),
        migrations.AddField(
            model_name='providerinfothirdcategory',
            name='third_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.ThirdCategory'),
        ),
        migrations.AddField(
            model_name='answertype',
            name='answer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Answer'),
        ),
        migrations.AddField(
            model_name='answertype',
            name='type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.TypeName'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Question'),
        ),
    ]
