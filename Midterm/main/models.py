from django.db import models


# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return self.name

    price = models.IntegerField(verbose_name="Price")

    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Created At')


class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name="Number Of Pages")
    genre = models.TextField(verbose_name="Genre")


class Journal(BookJournalBase):
    type = models.TextField(verbose_name="Type")

    publisher = models.TextField(max_length=100, verbose_name="Publisher")
