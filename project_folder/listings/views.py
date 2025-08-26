# D:\Coding arena\python_codes\project_folder\listings\views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemListing
from .forms import ItemListingForm

from .models import ItemListing
from .forms import ItemListingForm
from django.contrib.auth.forms import UserCreationForm # NEW: Import UserCreationForm
from django.contrib.auth import login # NEW: Import login function

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # NEW: Import login_required

# Read: List all items
def item_list(request):
    items = ItemListing.objects.all().order_by('-created_at') # Order by most recent
    # print("Items fetched for list view:", items) # <--- ADDING LINE TEMPORARILY
    return render(request, 'listings/item_list.html', {'items': items})

# Read: Display details of a single item
def item_detail(request, pk):
    item = get_object_or_404(ItemListing, pk=pk) # Get item by primary key (pk) or raise 404
    return render(request, 'listings/item_detail.html', {'item': item})

# Create: Add a new item (only by authenticated users)
@login_required
def item_create(request):
    if request.method == 'POST':
        # NEW: Pass request.FILES to the form
        form = ItemListingForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemListingForm()
    return render(request, 'listings/item_form.html', {'form': form})

# Update: Edit an existing item (only by authenticated owner)
@login_required
def item_update(request, pk):
    item = get_object_or_404(ItemListing, pk=pk)
    if request.user != item.user:
        return redirect('item_detail', pk=item.pk)

    if request.method == 'POST':
        # NEW: Pass request.FILES to the form, along with existing instance
        form = ItemListingForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemListingForm(instance=item)
    return render(request, 'listings/item_form.html', {'form': form})

# Delete: Remove an item
@login_required
def item_delete(request, pk):
    item = get_object_or_404(ItemListing, pk=pk) # Get the item to delete
    if request.method == 'POST': # If the delete confirmation form has been submitted
        item.delete()            # Delete the item
        return redirect('item_list') # Redirect to the list view
    return render(request, 'listings/item_confirm_delete.html', {'item': item}) # Show confirmation page

# User Registration (Signup) View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user
            login(request, user) # Log the user in immediately after registration
            return redirect('item_list') # Redirect to the item list page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form}) # Renders the signup form