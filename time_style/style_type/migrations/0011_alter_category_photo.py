# Generated by Django 4.1.6 on 2023-06-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style_type', '0010_alter_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
