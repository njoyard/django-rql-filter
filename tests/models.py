from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200)


class Child(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    parent = models.ForeignKey('Parent', related_name='children')
