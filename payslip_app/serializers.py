# serializers.py
from rest_framework import serializers
from .models import Employee, Earnings, Deductions

class EarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earnings
        fields = '__all__'

class DeductionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deductions
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    earnings = EarningsSerializer(many=True, read_only=True)
    deductions = DeductionsSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'