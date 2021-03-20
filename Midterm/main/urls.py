from django.contrib import admin
from django.urls import path, include

from main.views import books_view, journals_view

urlpatterns = [
    path('books/', books_view),
    path('journals/', journals_view),
]
