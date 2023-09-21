# Generated by Django 4.2.4 on 2023-08-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
            ],
        ),
    ]