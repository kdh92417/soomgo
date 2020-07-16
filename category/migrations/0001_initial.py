# Generated by Django 3.0.8 on 2020-07-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='AnswerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'answer_types',
            },
        ),
        migrations.CreateModel(
            name='FirstCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'first_categories',
            },
        ),
        migrations.CreateModel(
            name='ProviderInfoThirdCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'provider_infos_first_categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='SecondCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.FirstCategory')),
            ],
            options={
                'db_table': 'second_categories',
            },
        ),
        migrations.CreateModel(
            name='TypeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('answer_type', models.ManyToManyField(through='category.AnswerType', to='category.Answer')),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='ThirdCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField(max_length=2000)),
                ('is_popular', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Campaign')),
                ('second_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.SecondCategory')),
            ],
            options={
                'db_table': 'third_categories',
            },
        ),
    ]
