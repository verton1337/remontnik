from django import forms 
from ordersapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ("status","worker", "description")

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'pure-input-1'
            if field_name == "phone":
                field.widget.attrs['pattern'] = "\d{10,11}"
     


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('worker',)

    def __init__(self, *args, **kwargs):
        super(UpdateOrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'pure-input-1'
            if field_name =="userName" or field_name =="phone" :
                field.widget.attrs['readonly'] = ''