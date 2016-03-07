from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    page = models.IntegerField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        self.title
