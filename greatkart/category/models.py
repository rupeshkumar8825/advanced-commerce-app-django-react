from django.db import models

# Create your models here.
# we will create the class for this category model
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload='photos/categories', blank=True)

    def str (self):
        return self.category_name

