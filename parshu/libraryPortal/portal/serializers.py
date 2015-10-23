from rest_framework import serializers
from portal.models import Author,Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('title','publisher','authors','noBooks')
        
# class LibraryUserSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
#     class Meta:
#         model = LibraryUser
#         fields = ('username','usertype','books')

class AuthorSerializer(serializers.ModelSerializer):
	"""docstring for AuthorSerializer"""
	class Meta:
		model = Author
		#fields=('authorName','date_added',)