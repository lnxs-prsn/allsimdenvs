from django.contrib import admin
from .models import Book, Review, UserProfile
# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(UserProfile)