from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Categorie(models.Model):         # Category jadvalini ochdik
    title = models.CharField(max_length=150, verbose_name='Название')

    def get_absolute_url(self):            # aqilli ssilka
        return reverse('category_list', kwargs={'pk': self.pk})



    def __str__(self):       # admin panelda maqola ochilmagan paytda ismi ko'rinib turish uchun
        return self.title

    class Meta:
        verbose_name = 'Категория'           # admin panelda retseptlar degan kak papka ochilyapdi
        verbose_name_plural = 'Категории'    # bu ko'plikda


class Recipe(models.Model):     # Recipe jadvalini ochdik. id ni avtomatik tarzda django yaratadi
    title = models.CharField(max_length=150, verbose_name='Название')    # max_length-> varchar yani nechta harf ketishi
    content = models.TextField(blank=True, verbose_name='Описание')      # blank-> agar content berilmagan bolsa ishkal chiqmaslik uchun
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')   # malumot kiritilgan vaqti avtomatik beriladi
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')     # bu obnovleniya qilish uchun
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображение')    # photos papkasi avtomatik ochiladi va bosh bosa parot qimasin va null True-> bosh bolishi munkin
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано ли')    # Chop etilishiga ruxsat beruvchi ptichka
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Категория')     # Recipe ni category bilan ulayapdi. Kategoriyalar o'chirilib tashlanganda, unga tegishli maqolalar xam o'chib ketsin
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор') # models bog'liq bo'sin User ga (User djangodan import qilingan)

    def get_absolute_url(self):            # aqilli ssilka
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):      # admin panelda maqola ochilmagan paytda ismi ko'rinib turish uchun
        return self.title

    class Meta:
        verbose_name = 'Рецепт'  # admin panelda retseptlar degan kak papka ochilyapdi
        verbose_name_plural = 'Рецепты'  # bu ko'plikda
        ordering = ['-created_at']  # ma'lumot "kirgizilgan vaqti" bo'yicha sartirovka qilinsin
