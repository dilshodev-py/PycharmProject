from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    pass
