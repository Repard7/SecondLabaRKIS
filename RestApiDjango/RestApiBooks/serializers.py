from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =  '__all__'

    def validate(self, data):
        data = super().validate(data)

        instance = self.instance
        title = data.get('title')
        author = data.get('author')
        category = data.get('category')
        year_release = data.get('year_release')
        publisher = data.get('publisher')

        existing_books = Book.objects.filter(title=title, author=author)

        if instance:
            existing_books = existing_books.exclude(pk=instance.pk)

        if existing_books.exists():
            if category == 'textbook':
                if existing_books.filter(year_release=year_release).exists():
                    existing_years = existing_books.values_list('year_release', flat=True)
                    raise serializers.ValidationError({
                        'year_release': f'Учебник с таким годом выпуска уже существует. ' f'Существующие годы выпуска: {list(existing_years)}. ' 'Для учебников разрешены только переиздания с новым годом выпуска.'
                    })

            elif category == 'fiction':
                if existing_books.filter(publisher=publisher).exists():
                    existing_publishers = existing_books.values_list('publisher', flat=True)
                    raise serializers.ValidationError({
                        'publisher': f'Художественное произведение от этого издательства уже существует. ' f'Существующие издательства: {list(existing_publishers)}. ' 'Для художественной литературы разрешены книги от разных издательств.'
                    })

        return data

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =  '__all__'