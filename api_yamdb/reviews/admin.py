from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User
from reviews.models import Title, Genre, Categories, Review, Comments

admin.site.register(User, UserAdmin)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Categories)
admin.site.register(Review)
admin.site.register(Comments)
