from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome иконка, например: fa-dumbbell')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubscriptionType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Старая цена')
    period_days = models.IntegerField(verbose_name='Срок (дней)')
    visits_count = models.IntegerField(default=0, verbose_name='Посещений')
    image = models.ImageField(upload_to='abonements/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False, verbose_name='Популярный')
    features = models.TextField(blank=True, help_text='Возможности через запятую')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    has_gym = models.BooleanField(default=True, verbose_name='Тренажерный зал')
    has_pool = models.BooleanField(default=False, verbose_name='Бассейн')
    has_group = models.BooleanField(default=False, verbose_name='Групповые')
    has_spa = models.BooleanField(default=False, verbose_name='СПА')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('abonement_detail', args=[self.id])

    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')] if self.features else []

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'
        ordering = ['price']


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='trainers/')
    experience_years = models.IntegerField(default=1)
    instagram = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.rating}★"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"