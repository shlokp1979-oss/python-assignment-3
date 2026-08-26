from django import forms


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email'
            }
        )
    )


class OTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        label="Enter OTP",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter 6-digit OTP'
            }
        )
    )