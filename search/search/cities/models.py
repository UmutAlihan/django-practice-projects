from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

# when done writing models
# run python manage.py makemigrations cities
# to generate it on DB
