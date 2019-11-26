from django.db import models

class Branch(models.Model):
    branch_name = models.CharField(max_length = 40)
    branch_location = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__ (self):
        return f"{self.branch_name} | {self.branch_location}"


class Customer(models.Model):
    branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )
    customer_name = models.CharField(max_length = 100)
    
    def __str__ (self):
        return f"{self.branch.branch_name} | {self.customer_name}"

class Account(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete = models.CASCADE
    )
    account_balance = models.CharField(max_length = 40)

    def __str__ (self):
        return f"{self.customer.customer_name} | $ {self.account_balance}"