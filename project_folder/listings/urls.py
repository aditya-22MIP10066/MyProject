# D:\Coding arena\python_codes\project_folder\listings\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'), # Base URL for listing all items
    path('item/<int:pk>/', views.item_detail, name='item_detail'), # Detail view for a specific item
    path('item/new/', views.item_create, name='item_create'), # URL for creating a new item
    path('item/<int:pk>/edit/', views.item_update, name='item_update'), # URL for editing an item
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'), # URL for deleting an item

    path('signup/', views.signup, name='signup'), # Path for user registration
]