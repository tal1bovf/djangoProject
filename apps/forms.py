from django import forms
from apps.models import Product, Post


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

