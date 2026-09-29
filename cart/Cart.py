from home.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        products_dict = {str(product.id): product for product in products}

        for product_id, item in self.cart.items():
            item['product'] = products_dict[product_id]
            yield product_id, item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.session.modified = True