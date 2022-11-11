from django.contrib import admin
from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.home, name='home'),
    path('my-contacts/', views.contactList, name='contactList'),
    path('my-contacts/<id>', views.contactDetail, name='contactDetail'),
    path('create/', views.createCard, name="createCard"),
    path('edit/<id>', views.editCard, name="editCard"),
    path('delete/<id>', views.deleteCard, name="deleteCard")
]
