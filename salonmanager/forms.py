from fileinput import FileInput
from django import forms

from .models import Product,Service,Package
from djmoney.forms.widgets import MoneyWidget
from customerapp.models import Customer





class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': MoneyWidget(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category','name','price','duration','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': MoneyWidget(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'price', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': MoneyWidget(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'price']
        widgets = {
            'price': MoneyWidget(),
            
        }

class PackageUpdateForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'price']
        widgets = {
            'price': MoneyWidget(),
            
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'email', 'address']