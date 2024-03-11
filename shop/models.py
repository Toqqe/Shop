from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="product_images", default="blank-product.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(default=99.99, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.name}'
