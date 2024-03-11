from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username
    

class Address(models.Model):
    ADDR_TYPE = [
        (1, 'Home'),
        (2, 'Delivery')
    ]
    postal_code_validator = RegexValidator(
        regex=r'^\d{2}-\d{3}$',
        message = "Postal code must be in format XX-XXX"
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, default="Warsaw")
    state = models.CharField(max_length=30, default="Mazowieckie")
    postal_code = models.CharField(max_length=6, validators=[postal_code_validator] ,default="00-000")
    country = models.CharField(max_length=50)
    type = models.IntegerField(choices=ADDR_TYPE, default=1)

    def __str__(self):
        return f'{self.profile} - {self.type}'