# Generated by Django 2.1.7 on 2020-11-01 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_s', '0002_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '登陆用户', 'verbose_name_plural': '登陆用户'},
        ),
    ]
