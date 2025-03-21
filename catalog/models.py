from django.db import models
from catalog.validators import validate_positive_price
from users.models import CustomUser


class Category(models.Model):
    # наименование, описание
    name = models.CharField(
        max_length=150, verbose_name="Наименование категории", unique=True
    )
    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name",]


class Product(models.Model):

    # наименование, описание, изображение, категория, цена за покупку,
    # дата создания (created_at), дата последнего изменения (updated_at)

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание продукта",
    )
    picture = models.ImageField(
        upload_to="catalog/media/images/",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="Категории",
    )
    price = models.DecimalField(
        help_text="Введите стоимость покупки",
        max_digits=100,
        decimal_places=2,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )
    owner = models.ForeignKey(
        CustomUser,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    status = models.BooleanField(default=False, verbose_name="Статус публикации")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price", "category"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

