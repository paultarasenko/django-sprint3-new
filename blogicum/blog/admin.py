from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'slug')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'pub_date', 'author', 'category', 'location', 'is_published'
    )
