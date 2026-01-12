from django.contrib import admin
from models import Category
# Register your models here.

# we will have to register here to be able to see the 
# model in the admin panel for this purpose

# registering the category model in the admin panel 
admin.site.register(Category)
