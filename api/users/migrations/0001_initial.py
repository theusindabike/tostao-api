# Generated by Django 3.0.8 on 2020-07-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='último login')),
            ],
        ),
    ]