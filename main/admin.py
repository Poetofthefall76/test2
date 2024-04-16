from django.contrib import admin
from main import models

admin.site.register(models.UserProfile)
admin.site.register(models.Product)