from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.decorators import login_required


class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')


    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')



def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();


    customer = Customer.get_customer_by_id(request.session.get('customer'))

    data = {}
    data['products'] = products
    data['categories'] = categories

    if customer:
        data['usuario'] = customer.first_name

    return render(request, 'index.html', data)
