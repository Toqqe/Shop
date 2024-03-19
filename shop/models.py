from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField(max_length=250)
    slug = models.SlugField(unique=True, max_length=150, null=True, db_index=True, blank=True)
    image = models.ImageField(upload_to="product_images", default="blank-product.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(default=99.99, decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
