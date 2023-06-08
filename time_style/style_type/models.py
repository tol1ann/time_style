from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Outfit", max_length=150, default='Default Category')
    photo = models.ImageField("Изображение", null=True, blank=True, upload_to="categories_of_outfits/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Outfit(models.Model):
    """Аутфиты"""
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)
    photo = models.ImageField("Изображение", upload_to="outfits/")
    name = models.CharField('Название', max_length=34, default='Default Outfit')

    def __str__(self):
        return self.name


class Thing(models.Model):
    outfit = models.ForeignKey(
        Outfit, on_delete=models.CASCADE, verbose_name='Аутфит')
    photo = models.ImageField("Изображение", upload_to="things/")
    name = models.CharField('Название', max_length=34, default='Default Thing')

    def __str__(self):
        return self.name