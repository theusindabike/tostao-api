from django.db import models
from rest_framework import serializers


class Person(models.Model):
    name = models.CharField('nome', max_length=255)
    email = models.EmailField('e-mail')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    last_login = models.DateTimeField('último login', blank=True)


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'email', 'created_at')
