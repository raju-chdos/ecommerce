from django.contrib import admin
from .models import category, book, product
# Register your models here.

admin.site.register(category)
admin.site.register(book)
admin.site.register(product)

