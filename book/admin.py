from django.contrib import admin

# Register your models here.

from .models import Book
from .forms import BookForm


admin.site.register(Book)
# admin.site.register(Api)
