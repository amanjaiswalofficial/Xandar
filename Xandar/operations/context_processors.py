from Xandar import settings
from core.models import Cart, ProductCategory, Product, Attribute


def cart_count(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user, is_ordered=False)
            return {'count': len(cart.cartitems_set.all())}
        except Cart.DoesNotExist:
            return {'count': 0}
    else:
        request.session[settings.CART_SESSION_ID] = request.session.get(settings.CART_SESSION_ID, {})
        if request.session[settings.CART_SESSION_ID] is None:
            return {'count': 0}
        return {'count': len(request.session[settings.CART_SESSION_ID])}

def categories(request):
    return {'category': ProductCategory.objects.order_by().distinct()}

def sub_category(request):
    category = request.session.get("category", None)
    sub_categories = None
    if category:
        category = ProductCategory.objects.get(category=category)
        sub_categories = category.productsubcategory_set.all()
    return {"sub_category": sub_categories}

def price(request):
    return {'product_count': Product.objects.all().count()}

def brand(request):
    return {'brands': Attribute.objects.order_by().distinct().values('value')}
