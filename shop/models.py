from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
# Create your models here.

from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
            
class Images(models.Model):
    image = models.ImageField(upload_to="product_images/%Y-%m-%d/", default="blank-product.png")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='product_images/thumbnails/%Y-%m-%d/', blank=True)

    def __str__(self):
        return self.image.url
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            self.create_thumbnail()

    def create_thumbnail(self):
        if not self.thumbnail:
            image = Image.open(self.image)
            thumbnail = ImageOps.pad(image, (200, 200), color=(255, 255, 255))
            thumbnail = thumbnail.convert('RGB')
            thumbnail_io = BytesIO()
            thumbnail.save(thumbnail_io, format='JPEG', quality=85)
            self.thumbnail.save(self.image.name, InMemoryUploadedFile(
                thumbnail_io, None, self.image.name, 'image/jpeg', sys.getsizeof(thumbnail_io), None))


class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField(max_length=250)
    slug = models.SlugField(unique=True, max_length=150, null=True, db_index=True, blank=True)
    image = models.ManyToManyField(Images, blank=True, related_name="product_img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(default=99.99, decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


    def img_preview(self): #new
        first_image = self.image.last()
        
        if first_image:
            return mark_safe(f'<img src="{first_image.image.url}" width="100"/>')
        else:
            return 'No Image'
