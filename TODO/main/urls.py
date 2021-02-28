from django.contrib import admin
from django.urls import path, include
from main.views import todos, todosCompleted
urlpatterns = [
    path('', todos),
    # path('<int:id>/', todos),
    path('<int:id>/completed', todosCompleted)
]