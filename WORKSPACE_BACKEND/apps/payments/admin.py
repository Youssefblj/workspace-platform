from django.contrib import admin
from .models import Payment, PaymentLog

admin.site.register(Payment)
admin.site.register(PaymentLog)
