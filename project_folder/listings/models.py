from django.db import models
from django.contrib.auth.models import User # NEW: Import Django's User model

# Create your models here.

class ItemListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # automatically sets the timestamp when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='item_images/', blank=True, null=True) # NEW: Image field

    # This method defines how an object of this model is represented as a string
    def __str__(self):
        return self.name