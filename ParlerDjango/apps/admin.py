from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import MyModel



@admin.register(MyModel)
class MyModelAdmin(TranslatableAdmin ):
    search_fields = ('translations__title',)