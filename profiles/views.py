from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product, Wishlist

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
        
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(pk=product_id)
            wishlist.products.add(product)
            messages.success(request, f'Product "{product.name}" added to your wishlist.')
            return redirect('profile') 
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(user=request.user)

    if request.method == 'POST':
        # Adding a product to the wishlist
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.get(pk=product_id)
            wishlist.products.add(product)

        # Removing a product from the wishlist
        remove_product_id = request.POST.get('remove_product_id')
        if remove_product_id:
            product = Product.objects.get(pk=remove_product_id)
            wishlist.products.remove(product)

        return redirect('profile')

    return render(request, 'profile.html', {'profile': profile})

