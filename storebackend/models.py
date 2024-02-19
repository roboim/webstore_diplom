from django.db import models


class Shop(models.Model):
    """Информация о магазине"""
    name = models.CharField(max_length=60, unique=True)
    state = models.BooleanField()

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return '{0}'.format(self.name)


class Product(models.Model):
    """Информация о товаре"""
    name = models.CharField(max_length=60, unique=True)
    category = models.CharField(max_length=60, default='не указана')
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return '{0}_{1}_{2}_{3}_{4}'.format(self.name, self.category, self.description, self.quantity, self.price)
