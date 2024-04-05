# HR Management System

## Overview
This project is a comprehensive HR management system built using Django and Django Rest Framework (DRF). It provides functionalities for managing employee information, generating automated payslips, and facilitating communication between HR and employees.

## Features
- Employee Management: Allows HR staff to add, update, and delete employee details such as name, employee ID, designation, bank information, and more.
- Payslip Generation: Generates automated payslips for each employee based on their earnings, deductions, and other relevant details. Payslips are available in PDF format for easy download.
- Customizable Payslip Generator: Includes a customizable payslip generator that dynamically generates payslips based on company-specific parameters and employee data.
- Compliance: Ensures compliance with tax regulations and company policies regarding salary, deductions, and other financial aspects.
- RESTful API: Provides a RESTful API for seamless integration with other systems or applications.

## Installation
1. Clone the repository:
git clone <repository_url>

2. Install dependencies:

pip install -r requirements.txt

3. Run migrations:
python manage.py migrate

4. Start the development server:
python manage.py runserver


## Usage
1. Access the admin panel at `http://localhost:8000/admin/` to manage employee details.
2. Use the API endpoints for employee and payslip management:
   - Employees: `/api/employees/`
   - Payslips: `/api/payslips/`
3. To generate a payslip for a specific employee, use the payslip download endpoint:
   - Example: `/api/payslips/<payslip_id>/download/`

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

