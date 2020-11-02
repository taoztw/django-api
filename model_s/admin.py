from django.contrib import admin

# Register your models here.
from model_s import models

admin.site.register(models.Book)
admin.site.register(models.Press)
admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
admin.site.register(models.User)
