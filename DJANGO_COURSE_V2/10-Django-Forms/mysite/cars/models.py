from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])



