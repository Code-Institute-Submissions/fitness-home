from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart page"""
    return render(request, 'cart/shopping_cart.html')


def add_cart(request, item_id):
    """ Add quantity of specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product_type = request.POST.get('product_type')
    print(f"Product type in add_cart: {product_type}")
    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })

    if product_type == 'merchandise':
        if item_id in cart['merchandise_dic'].keys():
            cart['merchandise_dic'][item_id] += quantity
        else:
            cart['merchandise_dic'][item_id] = quantity
    elif product_type == 'excercise_plan':
        if item_id in cart['excercise_plans_dic'].keys():
            cart['excercise_plans_dic'][item_id] += quantity
        else:
            cart['excercise_plans_dic'][item_id] = quantity
    else:
        if item_id in cart['nutrition_plans_dic'].keys():
            cart['nutrition_plans_dic'][item_id] += quantity
        else:
            cart['nutrition_plans_dic'][item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
