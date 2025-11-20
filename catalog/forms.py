from django import forms
from .models import Product
from django.core.exceptions import ValidationError

banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'select-option',
            'placeholder': 'Выберите категорию продукта'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продукта'
        })


    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in banned_words:
            if word in name:
                raise ValidationError(f'Запрещенные слова: {", ".join(banned_words)}')
            return name

    def clean_desc(self):
        desc = self.cleaned_data.get('description')
        for word in banned_words:
            if word in desc:
                raise ValidationError(f'Запрещенное слова: {", ".join(banned_words)}')
            return desc

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть меньше нуля')