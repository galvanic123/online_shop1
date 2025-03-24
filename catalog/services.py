from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLE
from django.db.models import Q


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает из бд."""
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = "home"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_id=None):
    return Product.objects.filter(category_id=category_id)

