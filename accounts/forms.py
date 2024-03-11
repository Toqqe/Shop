from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User

from accounts.models import Address, Profile

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'login',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'password',
        })

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'login',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'password1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'password2',
        })

class UserProfileUpdateForm(forms.ModelForm):
    email = forms.CharField(required=True)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if email:
    #         if User.objects.filter(email=email).exclude(username=self.instance.user.username).exists():
    #             raise forms.ValidationError("Podany adres e-mail jest już zajęty.")
    #     return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'email',
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'number',
        })


class HomeAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "address",
            "city",
            "state",
            "postal_code",
            "country",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'number',
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "address",
            "city",
            "state",
            "postal_code",
            "country",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        self.fields['postal_code'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'number',
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'text',
        })
        
    # username = forms.CharField(max_length=20, required=True)
    # password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    # username.widget.attrs['class'] = "form-control"
    # username.widget.attrs['id'] = "floatingInput"
    # username.widget.attrs['placeholder'] = "login"
    # password.widget.attrs['class'] = "form-control"
    # password.widget.attrs['id'] = "floatingInput"
    # password.widget.attrs['placeholder'] = "password"