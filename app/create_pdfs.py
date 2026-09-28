from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def create_pdf(file_path, title, sections):
    pdf = canvas.Canvas(str(file_path), pagesize=A4)

    width, height = A4
    y = height - 50

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, title)

    y -= 40

    for heading, content in sections:
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, y, heading)

        y -= 25

        pdf.setFont("Helvetica", 11)

        for line in content:
            pdf.drawString(60, y, line)
            y -= 18

        y -= 15

        if y < 80:
            pdf.showPage()
            y = height - 50

    pdf.save()


company_policies = [
    (
        "Leave Policy",
        [
            "Employees are eligible for 12 days of paid leave per year.",
            "Leave requests should be submitted to the reporting manager.",
            "Planned leave should be requested at least 3 working days in advance."
        ]
    ),
    (
        "Work From Home Policy",
        [
            "Employees can work from home up to 2 days per week.",
            "Work from home requires manager approval.",
            "Employees must remain available during normal working hours."
        ]
    ),
    (
        "Working Hours",
        [
            "Standard working hours are 9:00 AM to 6:00 PM.",
            "Working days are Monday to Friday."
        ]
    )
]


employee_handbook = [
    (
        "Office Timings",
        [
            "The office operates from 9:00 AM to 6:00 PM.",
            "Office working days are Monday to Friday."
        ]
    ),
    (
        "Attendance",
        [
            "Employees are expected to maintain regular attendance.",
            "Employees should inform their manager when they cannot attend work."
        ]
    ),
    (
        "Reimbursement",
        [
            "Employees can submit eligible business expense claims.",
            "Receipts should be provided for reimbursement claims."
        ]
    ),
    (
        "Employee Benefits",
        [
            "Employees are eligible for company benefits.",
            "Benefits depend on employment category and company policy."
        ]
    )
]


create_pdf(
    DATA_DIR / "company_policies.pdf",
    "Company Policies",
    company_policies
)

create_pdf(
    DATA_DIR / "employee_handbook.pdf",
    "Employee Handbook",
    employee_handbook
)

print("PDF files created successfully!")