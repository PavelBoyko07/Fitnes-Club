from django.db import models
from django.forms import forms


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории', help_text='Максимум 200 символов')

    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-адрес',
                            help_text='URL-friendly название (латинские буквы, цифры, дефисы)')

    description = models.TextField(blank=True, null=True, verbose_name='Описание',
                                   help_text='Необязательное описание категории')

    is_active = models.BooleanField(default=True, verbose_name='Активна',
                                    help_text='Отображается ли категория на сайте')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    updated_at = models.DateTimeField(auto_now=True, )

    class Meta:
        verbose_name = "каталог"
        verbose_name_plural = "каталог"

    def __str__(self):
        return self.name


class SubscriptionType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название типа')
    period = models.TimeField(verbose_name='Период действия')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = "Тип расписания"
        verbose_name_plural = "Типы расписания"

    def __str__(self):
        return self.name


class Stock(models.Model):
    promo_code = models.CharField(max_length=50, verbose_name='Промокод')
    name = models.CharField(max_length=255, verbose_name='Название акции')
    is_percent = models.BooleanField(default=True, verbose_name='В процентах')
    amount = models.IntegerField(verbose_name='Размер скидки')

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    purchase_date = models.DateField(verbose_name='Дата покупки')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    visit_total = models.IntegerField(default=0, verbose_name='Общее кол-во посещений')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    sub_type = models.ForeignKey(SubscriptionType, on_delete=models.PROTECT, verbose_name='Тип расписания')
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Акция')

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"


class Review(models.Model):
    reviews = models.TextField(verbose_name='Отзыв')
    first_name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class User(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    gender = models.CharField(max_length=10, null=True, blank=True, verbose_name='Пол')
    role = models.IntegerField(default=1, verbose_name='Роль пользователя')
    reviews = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отзыв')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Workout(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тренировки')
    category = models.CharField(max_length=50, verbose_name='Категория')
    workout_id = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='ID тренировки')
    scheduled_date = models.DateField(verbose_name='Запланированная дата')
    status = models.IntegerField(default=0, verbose_name='Статус')
    trainer_notes = models.TextField(null=True, blank=True, verbose_name='Заметки тренера')
    checked_in_at = models.DateTimeField(null=True, blank=True, verbose_name='Время начала')

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"


class Schedule(models.Model):
    time = models.TimeField(verbose_name='Время')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 2}, verbose_name='Тренер')
    schedule_type = models.ForeignKey(SubscriptionType, on_delete=models.PROTECT, verbose_name='Тип расписания')
    occupation_type = models.IntegerField(verbose_name='Тип занятия')
    favourites = models.BooleanField(default=False, verbose_name='Избранное')

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Visit(models.Model):
    check_time = models.DateTimeField(verbose_name='Время входа')
    check_out_time = models.DateTimeField(null=True, blank=True, verbose_name='Время выхода')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, verbose_name='Абонемент')

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещение"
