from ORMapp.models import Rating,Restaurent,Order
from django import forms

class ProductStockException(Exception) :
    pass

class ProductOrderForm(forms.ModelForm) :
    class Meta :
        model=Order
        fields=('product','number_of_items')
    def save(self,commit=True) :
        order=super().save(commit=False)
        if order.product.number_in_stock < order.number_of_items :
            raise ProductStockException(f'Product out of stock for {order.product}')
        if commit :
            order.save()
        return order
# class RestaurentForm(forms.ModelForm) :
#     class Meta :
#         model=Restaurent
#         fields=('name','restaurent_type')

# class RatingForm(forms.ModelForm) :
#     class Meta :
#         model=Restaurent
#         fields=('name',)

