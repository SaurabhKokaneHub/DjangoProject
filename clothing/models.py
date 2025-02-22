# Create your models here.
from django.db import models

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('White', 'White'),
        ('Black', 'Black'),
    ]

    name = models.CharField(max_length=200)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    colour = models.CharField(max_length=10, choices=COLOR_CHOICES, default='Red')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_img/')

    def __str__(self):
        return self.name  # This will return the product name when printed
 