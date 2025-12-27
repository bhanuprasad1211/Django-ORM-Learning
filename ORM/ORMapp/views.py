from django.shortcuts import render,redirect
from .forms import ProductOrderForm #RestaurentForm
from .models import Restaurent,Rating,Product
from django.http import HttpResponse
from django.db import transaction
from functools import partial
import time
# Create your views here.

def email_user (email) :
    print(f'Dear {email}! Thank You for ordering')

def order_product(request) :
    if request.method=='POST' :
        form=ProductOrderForm(request.POST)
        if form.is_valid() :
            with transaction.atomic():
                book=Product.objects.select_for_update().get(
                    id=form.cleaned_data['product'].pk
                )
                time.sleep(30)
                order=form.save()
                
                #to demon strate system crash
                # import sys
                # sys.exit(1)
                
                order.product.number_in_stock-=order.number_of_items
                order.product.save()
            transaction.on_commit(partial(email_user,'banny@gmail.com'))
            return redirect('order_product')  
        else :
            return render(request,'order.html',{'form':form})
    context={'form':ProductOrderForm()}
    return render(request,'order.html',context)

def index(request) :
    return HttpResponse(request,"Home Page")
    # if request.method=='POST' :
    #     form=RestaurentForm(request.POST or None)
    #     if form.is_valid() :
    #         print(form.cleaned_data)
    #     else :
    #         return render(request,'index.html',{'form':form})
    # context={'form':RestaurentForm()}
    # restaurents=Restaurent.objects.prefetch_related('ratings')
    # ratings=Rating.objects.select_related('restaurent')
    # restaurents=Restaurent.objects.prefetch_related('ratings','sales').filter(ratings__rating=5)
    # print(restaurents)
    # context={'ratings':ratings}
    # return render(request,'index.html')
# def index(request) :
#     if request.method=='POST' :
#         form=RatingForm(request.POST or None)
#         if form.is_valid() :
#             form.save()
#         else :
#             return render(request,'index.html',{'form':form})
#     context={'form':RatingForm()}
#     return render(request,'index.html',context)