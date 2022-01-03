from django.contrib import admin

from core.models import Currency, Category, Transaction

admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Transaction)
