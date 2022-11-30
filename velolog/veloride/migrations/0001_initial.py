# Generated by Django 4.1.2 on 2022-11-25 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('fullname', models.CharField(blank=True, max_length=512, null=True, verbose_name='Полное наименование')),
                ('phone1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Контактный телефон')),
                ('phone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Доп. телефон')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('org_email', models.CharField(blank=True, max_length=128, null=True, verbose_name='Эл. почта')),
                ('org_site', models.CharField(blank=True, max_length=255, null=True, verbose_name='Официальный сайт')),
                ('org_type', models.CharField(blank=True, max_length=128, null=True, verbose_name='Тип')),
                ('archived', models.BooleanField(default=False, verbose_name='Архив')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
