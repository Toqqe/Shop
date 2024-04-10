from django.contrib import admin
from .models import Product, Category, Images
from django import forms
from django.forms import Select

from ckeditor.widgets import CKEditorWidget
# Register your models here.


class ProductAdminForm(forms.ModelForm):
    image_file = forms.ImageField(label="Upload image", required=False)

    class Meta:
        model = Product
        exclude = ('image',)
        
    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        self.fields['image_file'].required = False



class PictureInline(admin.TabularInline):
    model = Product.image.through
    extra = 1
    template = 'admin/shop/product/product_inline.html'
     
class ProductAdmin(admin.ModelAdmin):
    
    form = ProductAdminForm
    readonly_fields = ['img_preview']
    list_display = ['img_preview' ,'name','id', 'price']
    inlines = [PictureInline,]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            image_instance = Images(image=image_file)
            image_instance.save()
            obj.image.add(image_instance)
            
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['thumb_preview']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Images, ImagesAdmin)


