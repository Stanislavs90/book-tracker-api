from django.contrib import admin
from .models import Book, Character, Author

admin.site.register(Book)
admin.site.register(Character)
admin.site.register(Author)