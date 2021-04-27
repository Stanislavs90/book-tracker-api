from django.db import models

class Book(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=36)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    published = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='authors')

    def __str__(self):
        return self.name