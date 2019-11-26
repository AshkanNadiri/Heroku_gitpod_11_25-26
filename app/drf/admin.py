from django.contrib import admin
from drf.models import Branch, Customer, Account

# Register your models here.
admin.site.register((
    Customer,
    Account,
))

class CustomerInline(admin.StackedInline):
    model  = Customer

@admin.register(Branch)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        CustomerInline
    ]