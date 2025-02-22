from django.shortcuts import render
from .models import Product
from .forms import ProductForm

USD_TO_INR = 83  # Conversion rate

def fashion_view(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()  # Reset the form after saving

    return render(request, 'clothing/fashion.html', {'products': products, 'form': form})
