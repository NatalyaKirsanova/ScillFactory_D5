from django.contrib import admin
from p_library.models import Book, Author, Redaction, Reader, BookReading


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price',)
    pass

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass

@admin.register(BookReading)
class BookReadingAdmin(admin.ModelAdmin):
    pass