# Generated by Django 3.0.8 on 2020-07-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('account', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerinfo',
            name='order',
            field=models.ManyToManyField(related_name='order_provider', through='order.ProviderInfoOrder', to='order.Order'),
        ),
        migrations.AddField(
            model_name='providerinfo',
            name='payment',
            field=models.ManyToManyField(related_name='payment_provider', through='account.ProviderInfoPayment', to='account.Payment'),
        ),
        migrations.AddField(
            model_name='providerinfo',
            name='provider_info_third_category',
            field=models.ManyToManyField(related_name='category_provider', through='category.ProviderInfoThirdCategory', to='category.ThirdCategory'),
        ),
        migrations.AddField(
            model_name='providerinfo',
            name='provider_time',
            field=models.ManyToManyField(through='account.ProviderTime', to='account.Time'),
        ),
        migrations.AddField(
            model_name='profileimage',
            name='provider_info_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='provider_info_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo'),
        ),
        migrations.AddField(
            model_name='gu',
            name='si',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Si'),
        ),
        migrations.AddField(
            model_name='dong',
            name='gu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Gu'),
        ),
        migrations.AddField(
            model_name='address',
            name='dong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Dong'),
        ),
        migrations.AddField(
            model_name='address',
            name='gu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Gu'),
        ),
        migrations.AddField(
            model_name='address',
            name='si',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Si'),
        ),
    ]
