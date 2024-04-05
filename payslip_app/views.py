import io
from decimal import Decimal
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
 
    @action(detail=True, methods=['get'])
    def download_payslip(self, request, pk=None):
        employee = self.get_object()
        payslip_data = self.get_serializer(employee).data

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()

        # Define the column headers and data
        data = [
            ['Name', 'Employee ID', 'Designation', 'Bank Name', 'Bank Account Number', 'Department', 'Location', 'PAN', 'LOP'],
            [
                payslip_data['name'],
                payslip_data['employee_id'],
                payslip_data['designation'],
                payslip_data['bank_name'],
                payslip_data['bank_account_number'],
                payslip_data['department'],
                payslip_data['location'],
                payslip_data['pan'],
                str(payslip_data['lop'])
            ]
        ]

        # Create the table and set its style
        table = Table(data, colWidths=[1.2 * inch] * 2)  # Adjust the column widths
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        # Add more data to the table (earnings and deductions)
        data = [['SL NO', 'Earnings', 'Amount', 'Deductions', 'Amount']]
        for earning in payslip_data['earnings']:
            data.append(['1', 'basic', str(earning['basic']), '', ''])
            data.append(['2', 'hra', str(earning['hra']), '', ''])
            # data.append(['3', 'telephone_reimbursements', str(earning['telephone_reimbursements']), '', ''])
            data.append(['3', 'bonus', str(earning['bonus']), '', ''])
            data.append(['4', 'lta', str(earning['lta']), '', ''])
            data.append(['5', 'special_allowance', str(earning['special_allowance']), '', ''])

        for deduction in payslip_data['deductions']:
            data.append(['', '', '', 'Income Tax', str(deduction['income_tax'])])
            data.append(['', '', '', 'Provident Fund', str(deduction['provident_fund'])])
            data.append(['', '', '', 'Professional Tax', str(deduction['professional_tax'])])

        total_earnings = sum(Decimal(earning['basic']) + Decimal(earning['hra']) + Decimal(earning['telephone_reimbursements']) + Decimal(earning['bonus']) + Decimal(earning['lta']) + Decimal(earning['special_allowance']) for earning in payslip_data['earnings'])
        total_deductions = sum(Decimal(deduction['income_tax']) + Decimal(deduction['provident_fund']) + Decimal(deduction['professional_tax']) for deduction in payslip_data['deductions'])
        net_pay = total_earnings - total_deductions

        data.append(['', 'Total Earnings', str(total_earnings), 'Total Deductions', str(total_deductions)])
        data.append(['', '', '', 'Net Pay for the month', str(net_pay)])

        # Create the second table for earnings, deductions, and net pay
        table = Table(data, colWidths=[0.5 * inch, 1.5 * inch, 1 * inch, 1.5 * inch, 1 * inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        doc.build(elements)
        buffer.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="payslip.pdf"'
        response.write(buffer.getvalue())

        return response
