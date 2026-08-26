from django import forms
from django.core.validators import MinLengthValidator


class AddRestaurantForm(forms.Form):
    restaurant_name = forms.CharField(
        label="Restaurant Name",
        max_length=100,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter restaurant name'
        })
    )

    cuisine = forms.CharField(
        label="Cuisine Type",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter cuisine type'
        })
    )

    contact_email = forms.EmailField(
        label="Contact Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter contact email'
        })
    )