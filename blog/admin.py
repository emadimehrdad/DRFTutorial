from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
