from django.contrib import admin
from .models import MorphSuit

models_list = [MorphSuit]
admin.site.register(models_list)

# Register your models here.
