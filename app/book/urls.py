from django.conf.urls.static import static
from django.urls import path

from app import settings
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('', HomePage.as_view(), name='about'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('shop/<slug:book_slug>', BookCard.as_view(), name='card'),
    path('shop/basket_add/<int:book_id>', basket_add, name='basket_add'),  # Добавление товара в корзину
    path('basket/', BasketPage.as_view(), name='basket'),
    path('basket/change/<int:basket_id>/<int:count>', basket_change, name='basket_change'),  # Изменение количества товара
    path('basket/del/<int:basket_id>', basket_delete, name='basket_delete'),  # Удаление товара из корзины
    path('search/', search, name='search'),  # Поиск
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

