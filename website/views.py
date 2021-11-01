from django.shortcuts import render
from .models import *
from .forms import *


def home(request):
    our_opecialty = Our_Specialty.objects.all()
    popular = Orders.objects.all()
    gallery = Gallarey.objects.all()
    comments = Comments.objects.all()
    form_order_now = Received_OrdersForm()
    context = {
        'our_opecialty':our_opecialty,
        'popular':popular,
        'gallery':gallery,
        'comments':comments,
        'form_order_now':form_order_now,
    }
    template_name = 'index.html'
    return render(request, template_name, context)
