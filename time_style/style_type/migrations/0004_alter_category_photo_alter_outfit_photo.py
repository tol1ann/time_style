# Generated by Django 4.1.6 on 2023-06-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style_type', '0003_thing_name_thing_photo_alter_outfit_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='media/outfits/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='photo',
            field=models.ImageField(upload_to='staticfiles/', verbose_name='Изображение'),
        ),
    ]
