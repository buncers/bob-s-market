from django.shortcuts import render, redirect
from . import models





def home(request):

    all_products = models.Product.objects.all()

    all_categories = models.Category.objects.all()

    context = {'products': all_products, 'categories': all_categories}

    return render(request, 'index.html', context)



# Create your views here.
def about_product(request, pk):

    current_product = models.Product.objects.get(product_name=pk)
    context = {'product': current_product}
    return  render(request, 'about.html', context)
def category_products(request, pk):
    product_from_category = models.Category.objects.get(category_name=pk)

    context = {'products': product_from_category.products_set()}
    return render (request, 'index.html', context)

def search_for_products(request):
    product_from_front = request.GET.get ('search')
    find_product_from_db = models.Product.objects.filter(product_name__contains = product_from_front)
    print(product_from_front)
    context = {'products': find_product_from_db}
    return render(request, 'index.html', context )



def add_product_to_cart(request, pk):
    current_product = models.Product.objects.get(id=pk)
    checker = models.Usercart.objects.filter(user_id=None, user_product=current_product)


    if checker:
        checker[0].quantity = request.POST.get('pr_count')
        checker[0].total_for_product = current_product.product_price * checker[0].quantity


        models.UserCart().save()




        return  redirect(f'/product-detail/{current_product.product_name} ')

    else:
        models.UserCart.objects.create(user_id=request.user.id,
                                       user_product=current_product,
                                       quantity = request.POST.get('pr_count'),
                                       total_product=current_product.product_price * request.POST.get('pr_count'))
        return redirect