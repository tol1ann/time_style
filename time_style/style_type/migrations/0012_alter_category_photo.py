# Generated by Django 4.1.7 on 2023-06-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style_type', '0011_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='media/images/', verbose_name='Изображение'),
        ),
    ]