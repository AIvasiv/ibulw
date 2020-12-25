from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=60, blank="false")

class Expense_Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=60)
