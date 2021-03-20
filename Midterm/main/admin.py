from django.contrib import admin

# Register your models here.

from main.models import Journal, Book
admin.site.register(Journal),
admin.site.register(Book)