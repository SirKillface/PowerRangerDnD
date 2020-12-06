from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import random


# Create your models here.
class MorphSuit(models.Model):
    suit_name = models.CharField(max_length=20, blank=True)
    suit_x = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    suit_y = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    is_found= models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.suit_name)

