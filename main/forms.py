from django import forms
from . import models
from main.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            "user",
            "city"
        ]
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title of the book"}),
            "city": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "title",
            "price",
            "description",
        ]

        widgets = {
            "title": forms.Textarea(attrs={"class": "form-control", "placeholder": "Title"}),
            "price": forms.Textarea(attrs={"class": "form-control", "placeholder": "Price..."}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"})
        }