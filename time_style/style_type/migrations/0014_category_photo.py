# Generated by Django 4.1.7 on 2023-06-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style_type', '0013_remove_category_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/images/', verbose_name='Изображение'),
        ),
    ]
