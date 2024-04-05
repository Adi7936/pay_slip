from io import BytesIO
from reportlab.pdfgen import canvas

def generate_payslip_pdf(payslip):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Write payslip content
    p.drawString(100, 750, f"Name: {payslip.employee.name}")
    p.drawString(100, 730, f"Employee ID: {payslip.employee.employee_id}")
    p.drawString(100, 710, f"Designation: {payslip.employee.designation}")
    p.drawString(100, 690, f"Bank Name: {payslip.employee.bank_name}")
    p.drawString(100, 670, f"Department: {payslip.employee.department}")
    p.drawString(100, 650, f"Bank Account Number: {payslip.employee.bank_account_number}")
    p.drawString(100, 630, f"Location: {payslip.employee.location}")
    p.drawString(100, 610, f"PAN: {payslip.employee.PAN}")
    p.drawString(100, 590, f"LOP: {payslip.employee.LOP}")
    
    p.drawString(100, 560, "Earnings")
    p.drawString(150, 540, f"Basic: ₹ {payslip.basic}")
    p.drawString(150, 520, f"HRA: ₹ {payslip.HRA}")
    # Add other earnings
    
    p.drawString(100, 480, "Deductions")
    p.drawString(150, 460, f"Income Tax: ₹ {payslip.income_tax}")
    p.drawString(150, 440, f"Provident Fund: ₹ {payslip.provident_fund}")
    # Add other deductions

    p.drawString(100, 400, f"Total Earnings: ₹ {payslip.basic + payslip.HRA}")  # Calculate total earnings
    p.drawString(100, 380, f"Total Deductions: ₹ {payslip.income_tax + payslip.provident_fund}")  # Calculate total deductions

    p.drawString(100, 350, f"Net Pay for the month: ₹ {payslip.net_pay}")

    p.drawString(100, 320, "This is a system generated payslip and does not require signature.")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
