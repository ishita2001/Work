from django import forms
# from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import(
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm
)
from django.core.validators import RegexValidator

class BuyerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, min_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(BuyerRegistrationForm, self).save(commit=False)
        user.is_buyer = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
            buyer = Buyer.objects.create(user=user)

        return user


class SellerRegistrationForm(UserCreationForm):
    
    firm_name = forms.CharField(required=True,max_length=100)
    website = forms.URLField(max_length=100, initial="https://www.")
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, min_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    

    class Meta:
        model = User
        fields = (
            'firm_name',
            'username',
            'website',
            'email',
            'phone',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(SellerRegistrationForm, self).save(commit=False)
        user.is_seller = True
        user.firm_name = self.cleaned_data['firm_name']
        user.website = self.cleaned_data['website']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
            seller = Seller.objects.create(user=user)

        return user

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
     
class BuyerEditProfileForm(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone'
        )

class SellerEditProfileForm(UserChangeForm):

    password = None

    class Meta:
        model = User
        fields = (
            'firm_name',
            'website',
            'email',
            'phone'
        )

class ProductForm(forms.ModelForm):
    name     = forms.CharField(required=True,
                    widget=forms.TextInput(attrs={"placeholder": "Your Product Name"}))
    category = forms.CharField(
                         required=True,
                        widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Your product category",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    price    = forms.CharField(required=True, validators=[RegexValidator(r'^\d{1,10}$')])
    quantity = forms.CharField(required=True, validators=[RegexValidator(r'^\d{1,10}$')])
    class Meta:
        model = Product
        fields = [
            'name','category','price','quantity','image']
            
class CommentForm(forms.ModelForm):  
    content = forms.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('content',)

class EditProductForm(forms.ModelForm):

    price    = forms.CharField(required=True, validators=[RegexValidator(r'^\d{1,10}$')])
    quantity = forms.CharField(required=True, validators=[RegexValidator(r'^\d{1,10}$')])

    class Meta:
        model = Product
        fields = (
            'price',
            'quantity',
        )