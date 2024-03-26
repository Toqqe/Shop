from django.contrib import admin
from .models import Product, Category, Images
from django import forms
from django.forms import Select

from ckeditor.widgets import CKEditorWidget
# Register your models here.


# class PhotoSelect(Select):
#     def __init__(self, attrs=None, choices=(), renderer=None):
#         self.choices = choices
#         super().__init__(attrs)

# class ProductAdminForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'image']

#     def __init__(self, *args, **kwargs):
#         super(ProductAdminForm, self).__init__(*args, **kwargs)
#         # Pobierz wszystkie obiekty Photo i stwórz listę do wyboru
#         self.fields['image'].widget = PhotoSelect(choices=[(p.id, str(p)) for p in Product.objects.all()])


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
    
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    readonly_fields = ['img_preview']
    list_display = ['img_preview' ,'name','id', 'price']
    inlines = [PictureInline,]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print("eo")
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            image_instance = Images(image=image_file)
            image_instance.save()
            obj.image.add(image_instance)
            
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Images)


