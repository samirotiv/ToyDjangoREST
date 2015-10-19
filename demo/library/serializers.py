from rest_framework import serializers
from library.models import LibraryUser,Borrower,Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Book
        fields=('pk','title','publisher','author','count','date_added','owner')
        
class LibraryUserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    class Meta:
        model = LibraryUser
        fields = ('username','usertype','books')