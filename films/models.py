from django.db import models


# Create your models here.
# class Movie(models.Model):
name = models.CharField(verbose_name= 'Nombre de la película', max_length=80)
description = models.TextField(verbose_name= 'Descripción', max_length=800)


def __str__(self,):
    return self.name


    class Meta:_
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'


