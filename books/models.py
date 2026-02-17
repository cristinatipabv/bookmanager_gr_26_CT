from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, default="No Author")

    def __str__(self):
        return f"{self.title}, {self.content}, {self.author}"

