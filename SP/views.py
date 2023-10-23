from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def products(request):
    categorys=Machine_category.objects.all
    context={"categorys":categorys}
    return render(request,'products.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')