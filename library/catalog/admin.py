from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
