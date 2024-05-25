
from django import forms
from .models import Category

class PostsForm (forms.Form):
    title=forms.CharField(max_length=150, label='Haзвание ', widget=forms.TextInput(attrs={"class": "form-control"}))
    slug= forms.SlugField(max_length=150, label='URL', widget=forms.TextInput (attrs = {"class": "form-control"}))
    content=forms.CharField(label='TekсT', required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    category = forms.ModelChoiceField(
        empty_label='Bыберите категориo',
        label='Kaтегоpия',
        queryset=Category.objects.all(),  # Исправленная строка
        widget=forms.Select(attrs={"class": "form-control"})
    )
