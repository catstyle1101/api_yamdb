from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User
from reviews.models import (
    Title, Genre, Categories, Review, Comments, GenreCategories)


class GenreCategoriesInline(admin.TabularInline):
    model = GenreCategories
    extra = 1


class TitleAdmin(admin.ModelAdmin):
    inlines = (GenreCategoriesInline,)


class GenreAdmin(admin.ModelAdmin):
    inlines = (GenreCategoriesInline,)


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Categories)
admin.site.register(Review)
admin.site.register(Comments)
