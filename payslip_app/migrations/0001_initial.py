# Generated by Django 4.2.11 on 2024-04-05 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('PAN', models.CharField(max_length=20)),
                ('LOP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('basic', models.DecimalField(decimal_places=2, max_digits=10)),
                ('HRA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('income_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('provident_fund', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telephone_reimbursements', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('professional_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('LTA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('special_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payslip_app.employee')),
            ],
        ),
    ]
