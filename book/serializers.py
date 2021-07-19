from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import Book


class BookSerializer(HyperlinkedModelSerializer):
    # book = serializers.HyperlinkedRelatedField(
    #     view_name='book-detail', many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')


