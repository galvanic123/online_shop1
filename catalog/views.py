from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/base.html", context=context)


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context=context)


def product_list(request):
    products = Product.objects.all()
    context = {"product": products}
    return render(request, "catalog/product_list.html", context=context)