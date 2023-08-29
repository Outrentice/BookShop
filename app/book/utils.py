from book.models import Product, Category, Authors, Basket
from book.forms import *


menu = [
    {'name': 'Home', 'url': 'home'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Магазин', 'url': 'shop'},
]


class DataMixin:
    def get_user_context(self, request):
        context = {}
        context['title'] = 'Book Shop'
        context['menu'] = menu
        context['search_form'] = SearchForm.SearchForm()

        if request.user.is_authenticated:
            context['Basket_product'] = Basket.objects.filter(user=self.request.user).select_related()
        else:
            context['Basket_product'] = None
        return context
