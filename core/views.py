from django.shortcuts import render
from rest_framework import viewsets

from core.models import Category, Transaction, Currency
from core.serializers import CategorySerializer, WriteTransactionSerializer, CurrencySerializer, \
    ReadTransactionSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related('currency', 'category')

    # serializer_class = WriteTransactionSerializer
    print()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer

        return WriteTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
