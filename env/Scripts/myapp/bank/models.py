from django.db import models

class AdType(models.TextChoices):
    SAVINGS = 'SAV', 'Savings'
    CURRENT = 'CUR', 'Current'
    SALARY = 'SAL', 'Salary'
    BUSINESS = 'BUS', 'Business'

class ad(models.Model):
    name=models.CharField(max_length=25)
    number=models.CharField(max_length=14)
    type=models.CharField(max_length=3,choices=AdType.choices,default=AdType.SAVINGS,)
    balance=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class stock(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.name

