# D:\Coding arena\python_codes\project_folder\listings\admin.py
from django.contrib import admin
from .models import ItemListing # Import your ItemListing model

# Register your models here.
admin.site.register(ItemListing) # This line makes your model visible in the admin