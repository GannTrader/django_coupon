from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart, Discount
from django.contrib import messages


def index(request):
	products = Product.objects.all()
	return render(request, 'products.html', {'products':products})

def add_to_cart(request, id):
	product = Product.objects.get(id = id)
	check_cart = Cart.objects.filter(user = request.user, product = product)

	if not check_cart:
		cart = Cart.objects.create(
			user = str(request.user),
			product = product,
			quantity = 1,
			price = product.price,
			)
		cart.save()
	else:
		check_cart.update(quantity = int(Cart.objects.get(user = request.user, product = product).quantity) + 1)
	return redirect('sales:index')

def view_cart(request):
	total = 0
	cart = Cart.objects.filter(user = request.user)

	for item in cart:
		total += item.quantity * item.price

	if request.POST.get('coupon_code'):
		check_code = Discount.objects.filter(code = request.POST.get('coupon_code'))
		
		if check_code.exists():
			sale_off = Discount.objects.get(code = request.POST.get('coupon_code')).percent
			total = total * (1 - sale_off)
			messages.success('Bạn được giảm ')
		else:
			messages.info('code không tồn tại hoặc hết hạn!')

	return render(request, 'cart.html', {'cart': cart, 'total': total})



def payment(request):
	pass