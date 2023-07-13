from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError

class Profile(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        WEB = 'web'
        STOCK = 'stock'
        MEMBRE = 'membre'
    
    role = models.CharField(choices=Role.choices, max_length=20, default=Role.MEMBRE)
    
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('shoes', 'Shoes'),
        ('clothing', 'Clothing'),
    ]

    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    availability = models.BooleanField()
    quantity = models.IntegerField()
    ranking_user = models.IntegerField(null=True, blank=True)
    ranking_global = models.DecimalField(max_digits=3, decimal_places=2)
    image_url = models.URLField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        if self.category.filter(name='men').exists() and self.category.filter(name='women').exists():
            raise ValidationError("An article cannot be both 'Men' and 'Women'.")
        
        if self.category.filter(name='shoes').exists() and self.category.filter(name='clothing').exists():
            raise ValidationError("An article cannot be both 'Shoes' and 'Clothing'.")



# XXXXX CONTACT BACK XXXXX
class ContactInfo(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    fax = models.CharField(max_length=20)

    def __str__(self):
        return self.location
    