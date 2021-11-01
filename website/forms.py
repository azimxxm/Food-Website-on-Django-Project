from django.forms import *

from .models import *

class Received_OrdersForm(ModelForm):
    class Meta:
        model = Received_Orders
        fieald = '__all__'
        widgets = {
            "name":TextInput(attrs={
                'class':'inputBox',
                'placeholder':'name'
            }),
            "phone":NumberInput(attrs={
                'class':'inputBox',
                'placeholder':'phone'

            }),
            "email":EmailInput(attrs={
                'class':'inputBox',
                'placeholder':'email'

            }),
            "food_name":TextInput(attrs={
                'class':'inputBox',
                'placeholder':'food_name'

            }),
            "adress":Textarea(attrs={
                'class':'inputBox',
                'placeholder':'adress'

            }),
        }
        exclude = ['is_published']