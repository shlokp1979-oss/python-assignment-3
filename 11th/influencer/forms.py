from django import forms
from .models import InfluencerProfile


class InfluencerProfileForm(forms.ModelForm):

    class Meta:
        model = InfluencerProfile

        fields = [
            'display_name',
            'bio',
            'profile_pic',
            'phone_number'
        ]

        widgets = {
            'display_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter display name'
                }
            ),

            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'Write your bio'
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Enter 10 digit phone number',
                    'maxlength': '10'
                }
            ),
        }

    def clean_phone_number(self):

        phone = self.cleaned_data['phone_number']

        if phone and (
            len(phone) != 10 or not phone.isdigit()
        ):
            raise forms.ValidationError(
                'Phone number must be exactly 10 digits.'
            )

        return phone