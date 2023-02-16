from django.contrib import admin
from django.contrib import admin
from api.models.categories import Categories
from api.models.genres import Genre
from api.models.titles import Titles


admin.site.register(Categories)
admin.site.register(Genre)
admin.site.register(Titles)
