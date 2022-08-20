from django.db import models
from django.core.validators import MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    photo = models.ImageField(
        max_length=200, upload_to="persons/",
        null=True, blank=True
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'