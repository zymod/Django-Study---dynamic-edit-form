from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
import json

from .models import Product
from .forms import ProductForm


def product_all_view(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_id = request.POST.get('id')
            product_note = request.POST.get('note')
            product = Product.objects.get(id=product_id)
            product.note = product_note
            product.save()
            return redirect(reverse(
                'warehouse:product_all'
            ))

    return render(
        request,
        'warehouse/product.html', {
            'product_all': Product.objects.all()
        }
    )

def product_note_edit(request):
    product_id = json.load(request)['productId']
    obj = Product.objects.get(id=product_id)

    data = {

        'product_id': product_id,
        'obj_note': obj.note,

    }

    return JsonResponse(data)