from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    biography = models.TextField()
    class Meta:
        unique_together = ['first_name', 'last_name', 'patronymic']
    def __str__(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        return f"{self.last_name} {self.first_name}"

class Book(models.Model):

    CATEGORY_CHOICES = [
        ('fiction', 'Художественная литература'),
        ('textbook', 'Учебник'),
    ]

    title = models.CharField(max_length=100)
    year_release = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_covers/')
    text_file = models.FileField( upload_to='book_texts/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['title', 'author', 'year_release', 'publisher']

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year_release})"