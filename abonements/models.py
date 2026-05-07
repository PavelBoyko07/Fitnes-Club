from django.db import models


class SubscriptionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    period = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'

    def __str__(self):
        return self.name