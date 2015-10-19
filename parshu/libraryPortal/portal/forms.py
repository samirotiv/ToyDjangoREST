from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User   # fill in custom user info then save it
from portal.models import UserProfile , Book , Author

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
         model = User
         fields = '__all__'
         fields = ('username' , 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = {'currentBook' , 'user' }
        widgets = {
            'userType' : forms.RadioSelect
        }



class AddBookForm(forms.ModelForm):
    publisher = forms.CharField(label='Publisher', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    noBooks = forms.CharField(label='Books Count', max_length=100)


    class Meta:
        model = Book

        fields = '__all__'
        fields = ( 'title' , 'publisher' , 'noBooks' , 'authors')
        

class AuthorForm(forms.ModelForm):
    authorName = forms.CharField(max_length=200)

    class Meta:
        model = Author
        fields = '__all__'
        fields = ('authorName',)
