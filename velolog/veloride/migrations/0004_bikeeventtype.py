# Generated by Django 4.1.2 on 2022-11-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veloride', '0003_bike'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeEventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Описание')),
                ('archived', models.BooleanField(default=False, verbose_name='Архив')),
            ],
            options={
                'verbose_name': 'Тип велозаезда',
                'verbose_name_plural': 'Типы велозаездов',
            },
        ),
    ]
