from django.db import models
from rest_framework import serializers

from api.persons.models import Person


class Transaction(models.Model):
    INCOME = 'I'
    EXPENSE = 'E'

    KINDS = (
        (INCOME, 'Receita'),
        (EXPENSE, 'Despesa')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    description = models.CharField('descrição', max_length=255)
    value = models.DecimalField('valor', max_digits=16, decimal_places=2)
    created_at = models.DateTimeField('criado em', auto_now_add=True)


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('description', 'value', 'kind', 'created_at', 'person')
