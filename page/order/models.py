from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name=_("Название"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"


class Car(models.Model):
    number = models.CharField(
        max_length=20,
        verbose_name=_("Номер"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Client(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name=_("Название"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class PlaceImpl(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name=_("Название"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Место прибытия"
        verbose_name_plural = "Места прибытия"


class PlaceFrom(models.Model):
    title = models.CharField(
        max_length=20,
        verbose_name=_("Название"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Откуда"
        verbose_name_plural = "Откуда"


class Order(models.Model):
    count = models.PositiveIntegerField(
        verbose_name=_("Название"),
        null=True,
        blank=True,
    )

    product =  models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Продукция')
    )

    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Клиент')
    )

    placeImpl = models.ForeignKey(
        'PlaceImpl',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Куда')
    )

    car = models.ForeignKey(
        'Car',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Машина')
    )

    placeFrom = models.ForeignKey(
        'PlaceFrom',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Откуда')
    )

    date_of_create = models.DateTimeField(editable=False, null=True, blank=True, verbose_name='Дата создания заказа')

    def save(self, *args, **kwargs):
        if not self.date_of_create:
            self.date_of_create = timezone.localtime(timezone.now())


    def __str__(self):
        return f"{self.id, self.client, self.date_of_create}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"