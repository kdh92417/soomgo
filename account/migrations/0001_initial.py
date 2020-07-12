<<<<<<< HEAD
# Generated by Django 3.0.7 on 2020-07-15 10:45
=======
# Generated by Django 3.0.8 on 2020-07-14 07:03
>>>>>>> dbac424... [Fix] migrate models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_provider', models.BooleanField(default=False)),
                ('kakao_id', models.IntegerField(default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('x_position', models.DecimalField(decimal_places=16, max_digits=22)),
                ('y_position', models.DecimalField(decimal_places=16, max_digits=22)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dong',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Gu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'gu',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduce', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=6000)),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'profile_images',
            },
        ),
        migrations.CreateModel(
            name='ProviderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='01000000000', max_length=50)),
                ('career', models.IntegerField()),
                ('employee', models.IntegerField()),
                ('is_business', models.BooleanField(default=False)),
                ('is_identity', models.BooleanField(default=False)),
                ('is_certificate', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Address')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Gender')),
            ],
            options={
                'db_table': 'provider_infos',
            },
        ),
        migrations.CreateModel(
            name='Si',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'si',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField()),
                ('last_time', models.IntegerField()),
            ],
            options={
                'db_table': 'times',
            },
        ),
        migrations.CreateModel(
            name='SubImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('provider_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo')),
            ],
            options={
                'db_table': 'sub_images',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('comment', models.CharField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
                ('provider_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ProviderTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo')),
=======
                ('provider_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo')),
>>>>>>> dbac424... [Fix] migrate models
                ('time_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Time')),
            ],
        ),
        migrations.CreateModel(
            name='ProviderInfoPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Payment')),
                ('provider_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.ProviderInfo')),
            ],
            options={
                'db_table': 'provider_infos_payments',
            },
        ),
    ]
