# Generated by Django 3.0.8 on 2020-07-19 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('I', 'Receita'), ('E', 'Despesa')], max_length=1, verbose_name='tipo')),
                ('description', models.CharField(max_length=255, verbose_name='descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='valor')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person')),
            ],
        ),
    ]
