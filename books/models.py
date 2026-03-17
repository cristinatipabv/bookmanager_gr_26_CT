from django.contrib.auth.models import User
from django.db import models
from accounts.models import CustomUser


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, default="No Author")

    image = models.ImageField(upload_to="book_images/",
                              null=True,
                              blank=True,
                              )

    # one-to-many relationship
    user = models.ForeignKey(
        CustomUser,
        related_name="books",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,

    #     sau se poate folosi si models.SET_NULL


    )
    # elated_name="books" -> parametru adaugat automat fiecarui obiect CustomUser, unde avem acces la o lista cu cartile care apartin user-ului.

    def __str__(self):
        return f"{self.title}, {self.content}, {self.author}"

