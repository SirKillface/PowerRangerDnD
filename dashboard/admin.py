from django.contrib import admin
from .models import MorphSuit, RangerTeam, Movement, Map

models_list = [MorphSuit, RangerTeam, Movement, Map]
admin.site.register(models_list)

# Register your models here.
