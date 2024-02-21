from django.db import models

# Create your models here.
"""
1. category 
2. subcategory
3. transcation -> payment method ->choices -> credit , cash, cheque
   status -> choices -> cleared ,  uncleared ,  void
""" 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subcategories"

PAYMENT_CHOICES = [
    ('credit', 'Credit'),
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
]

STATUS_CHOICES = [
    ('cleared', 'Cleared'),
    ('uncleared', 'Uncleared'),
    ('void', 'Void'),
]

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    end_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def _str_(self):
        return f"Transaction ID: {self.id}"
    # f for formatting