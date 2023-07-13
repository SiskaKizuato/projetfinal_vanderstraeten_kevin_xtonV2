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
        men_count = self.category.filter(name='men').count()
        women_count = self.category.filter(name='women').count()
        clothing_count = self.category.filter(name='clothing').count()
        shoes_count = self.category.filter(name='shoes').count()

        if men_count > 0 and women_count > 0:
            raise ValidationError("An article cannot be both 'Men' and 'Women'.")
        
        if clothing_count > 0 and shoes_count > 0:
            raise ValidationError("An article cannot be both 'Clothing' and 'Shoes'.")





# XXXXX CONTACT BACK XXXXX
class ContactInfo(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    fax = models.CharField(max_length=20)


    def __str__(self):
        return self.location
    