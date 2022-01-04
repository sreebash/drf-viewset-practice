from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Example = USD, BRL, BDT
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.code


class Category(models.Model):
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='transactions')
    date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.amount} {self.currency.code} {self.date}"

