from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView

from book.models import Product, Category, Authors, Basket
from book.forms import *
from book.utils import DataMixin


class HomePage(DataMixin, ListView):
    model = Product
    template_name = 'book/index.html'
    context_object_name = 'Products'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(self.request)
        context['reverse_prod'] = self.object_list[::-1]

        return dict(list(context.items()) + list(c_def.items()))


class BookCard(DataMixin, DetailView):
    model = Product
    template_name = 'book/product.html'
    queryset = Product.objects.all().select_related()
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(self.request)

        context['new_book'] = Product.objects.all().order_by('-id')[::-1][:6]
        context['book_this_author'] = Product.objects.filter(author=self.object.author)

        return dict(list(context.items()) + list(c_def.items()))


class ShopPage(DataMixin, ListView):
    model = Product
    template_name = 'book/shop.html'
    context_object_name = 'Products'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(self.request)

        context['categorys'] = Category.objects.all()
        context['form'] = self.get_form()
        context['authors'] = Authors.objects.all()[:5]

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        model = self.model.objects.all()
        if self.request.GET.get('cat'):
            model = model.filter(category=self.request.GET.get('cat'))
        if self.request.GET.get('sort'):
            model = model.order_by(self.request.GET.get('sort'))
        if self.request.GET.get('start_price'):
            model = model.filter(price__gte=self.request.GET.get('start_price'))
        if self.request.GET.get('end_price'):
            model = model.filter(price__lte=self.request.GET.get('end_price'))
        if self.request.GET.get('author'):
            model = model.filter(author_id=self.request.GET.get('author'))
        return model.select_related()

    def get_form(self):
        return PriceFilter.PriceFilter(self.request.GET)


class BasketPage(DataMixin, LoginRequiredMixin, ListView):
    model = Basket
    context_object_name = 'Basket_product'
    template_name = 'book/cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list(self.get_user_context(self.request).items()))

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).select_related()


class LoginPage(DataMixin, LoginView):
    template_name = 'book/login.html'
    form_class = LoginForm.LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list(self.get_user_context(self.request).items()))

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')


class RegisterPage(DataMixin, CreateView):
    template_name = 'book/register.html'
    form_class = RegisterForm.RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()) + list(self.get_user_context(self.request).items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def basket_add(request, book_id):
    prod = Product.objects.get(id=book_id)
    basket = Basket.objects.filter(product=book_id, user=request.user.id)

    if not basket:
        if prod.count_product > 0:
            Basket.objects.create(product=prod, user=request.user)
    else:
        if basket[0].count_product < prod.count_product:
            basket[0].count_product += 1
            basket[0].save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_change(request, basket_id, count):
    basket = Basket.objects.get(id=basket_id)

    if count > 0:
        if count > basket.product.count_product:
            basket.count_product = basket.product.count_product
        else:
            basket.count_product = count
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_delete(request, basket_id):
    Basket.objects.get(id=basket_id).delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def search(request):
    prod = Product.objects.all().select_related()
    search = request.POST.get('search_input')
    print(search)

    for item in prod:
        auth = item.author
        if search in item.name or search in auth.first_name or search in auth.last_name or search in auth.middle_name:
            return redirect('card', book_slug=item.slug)

    return redirect('shop')
