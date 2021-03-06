# Generated by Django 2.1.7 on 2020-11-01 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_s', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'ts_login_user',
            },
        ),
    ]
