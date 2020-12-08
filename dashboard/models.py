from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import ModelForm
from django import forms


class RangerTeam(models.Model):
    position_x = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9)])
    position_y = models.IntegerField(default=9, validators=[MinValueValidator(1), MaxValueValidator(9)])
    num_morphs = models.IntegerField(default=0)
    turn_count = models.IntegerField(default=0)

    def __str__(self):
        return 'Ranger Team'


class MorphSuit(models.Model):
    suit_name = models.CharField(max_length=20, blank=True)
    suit_x = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    suit_y = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    is_found= models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.suit_name)


class Map(models.Model):
    drawMap = models.CharField(max_length=90)


class Movement(models.Model):
    movement_x = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    movement_y = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])


class MoveForm(ModelForm):
    mov_x = forms.IntegerField(label="x", validators=[MinValueValidator(1), MaxValueValidator(9)])
    mov_y = forms.IntegerField(label="y", validators=[MinValueValidator(1), MaxValueValidator(9)])

    class Meta:
        model = Movement
        fields = [
            'mov_x',
            'mov_y'
        ]
        exclude = [
            'movement_x',
            'movement_y'
        ]
