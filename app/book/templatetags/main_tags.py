from django import template


register = template.Library()


@register.simple_tag
def sale_price(price, sale):
    return int(int(price) - (int(price) * (sale / 100)))


@register.simple_tag
def pairs_products(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


@register.simple_tag
def multiply(a, b):
    return a * b


@register.simple_tag
def division(a, b):
    return a / b


@register.simple_tag
def minus(a, b):
    return a - b


@register.simple_tag
def total_price(basket):
    return sum(i.count_product * sale_price(i.product.price, i.product.sale) for i in basket)


