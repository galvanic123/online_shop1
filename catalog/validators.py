from django.core.exceptions import ValidationError


def validate_positive_price(value):
    """Проверяет, что цена не отрицательная."""
    if value < 0:
        raise ValidationError("Цена не может быть отрицательной!")
