# models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_account_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pan = models.CharField(max_length=10)
    lop = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.name

class Earnings(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='earnings')
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    telephone_reimbursements = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    lta = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


    def __str__(self) -> str:
        return self.employee.name

class Deductions(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='deductions')
    income_tax = models.DecimalField(max_digits=10, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=10, decimal_places=2)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return self.employee.name

    