from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'slug', 'preview', 'made_date', 'is_published', 'views_count')
    list_filter = ('title',)