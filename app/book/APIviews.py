from rest_framework.generics import ListAPIView
from .models import *
from .Serializers import *
from .Permissions import *


class APIBook(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (TokenPermission, )

    def get_queryset(self):
        if self.kwargs.get('pk') is not None:
            return Product.objects.filter(pk=self.kwargs.get('pk'))
        elif self.kwargs.get('slug') is not None:
            return Product.objects.filter(slug=self.kwargs.get('slug'))
        return Product.objects.all()


class APIBookAuthor(ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (TokenPermission, )

    def get_queryset(self):
        return Product.objects.filter(author=self.kwargs.get('pk'))


class APIAuthor(ListAPIView):
    serializer_class = AuthorsSerializer
    permission_classes = (TokenPermission, )

    def get_queryset(self):
        if self.kwargs.get('pk') is not None:
            return Authors.objects.filter(pk=self.kwargs.get('pk'))
        return Authors.objects.all()


