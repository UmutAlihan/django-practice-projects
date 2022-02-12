from django.db import models

# Create your models here.

class Salon(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class Mutfak(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class KucukOda(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class YatakOda(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

class Tuvalet(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
