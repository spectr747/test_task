from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = 'name', 'title', 'author', 'description', 'price'


admin.site.register(Book,BookAdmin)
