# Generated by Django 3.0.13 on 2021-03-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languauge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Языки программирования',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Название населенного пункта', 'verbose_name_plural': 'Название населенных пунктов'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название населенного пункта'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
