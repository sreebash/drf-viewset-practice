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
    queryset = Transaction.objects.all()

    # serializer_class = WriteTransactionSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer

        return WriteTransactionSerializer
