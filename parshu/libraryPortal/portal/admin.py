from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from portal.models import UserProfile , Book ,Author
# Register your models here.

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

    # Define a new User admin
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.register(Book)
admin.site.register(Author)

# Re-register UserAdmin
admin.site.register(User, UserProfileAdmin)
