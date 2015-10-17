from django.contrib import admin
from .forms import LibraryUserForm
# Register your models here.
from .models import Book,LibraryUser,Borrower
class LibraryUserAdmin(admin.ModelAdmin):
    form = LibraryUserForm
admin.site.register(Book)
admin.site.register(LibraryUser,LibraryUserAdmin)
admin.site.register(Borrower)