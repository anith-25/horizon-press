# Generated by Django 5.0.1 on 2024-01-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textclassifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
