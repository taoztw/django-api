from django.contrib import admin

# Register your models here.
from test_app import models

admin.site.register(models.User)