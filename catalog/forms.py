from django import forms
from catalog.models import Product
from django.conf import settings
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)


        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите стоимость"}
        )

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if any(word in name.lower() for word in self.wrong_words):
    #         raise forms.ValidationError("Найдено запрещенное слово")
    #     return name

    def clean_name(self):
        data = self.cleaned_data['name']
        forbidden_words = getattr(settings, 'FORBIDDEN_WORDS')
        for word in forbidden_words:
            if word.lower() in data.lower():
                raise ValidationError(f"Запрещённое слово: '{word}'!")
        return data

    # def clean_description(self):
    #     description = self.cleaned_data.get("description")
    #     if any(word in description.lower() for word in self.wrong_words):
    #         raise forms.ValidationError("Найдено запрещенное слово")
    #     return description

    def clean_description(self):
        data = self.cleaned_data['description']
        forbidden_words = getattr(settings, 'FORBIDDEN_WORDS')
        for word in forbidden_words:
            if word.lower() in data.lower():
                raise ValidationError(f"Запрещённое слово: '{word}'!")
        return data


    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")

        if price is None:
            raise forms.ValidationError("Цена должна быть указана.")

        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")

        return price

    def clean_image(self):
        cleaned_data = super().clean()
        if "image" in cleaned_data:
            image = cleaned_data.get("image")
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")
            if not image.name.endswith(("jpg", "jpeg", "png")):
                raise forms.ValidationError(
                    "Недопустимый формат файла. Загрузите JPEG или PNG."
                )
            return image
        else:
            raise forms.ValidationError("Изображение должно быть указано.")