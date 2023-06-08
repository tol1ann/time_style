from django.contrib import admin
from .models import Outfit, Category, Thing

admin.site.register(Category)
admin.site.register(Outfit)
admin.site.register(Thing)
