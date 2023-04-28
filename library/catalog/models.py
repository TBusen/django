from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    # this is a model representing a book genre

    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
    )

    def __str__(self):
        # string for representing the Model object
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
    )

    def __str__(self):
        # string for representing the Model object
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    # if the pk author value is deleted, then in the book table the author is set to null instead of deleting the book
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # string for representing the Model object
        return self.title

    def get_absolute_url(self):
        # returns the url to access a particular book instance
        return reverse("book_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # date of birth and death are optional
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        # returns the url to access a particular author instance
        return reverse("author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        # string for representing the Model object
        return f"{self.last_name}, {self.first_name}"


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        # string for representing the Model object
        return f"{self.id} ({self.book.title})"
