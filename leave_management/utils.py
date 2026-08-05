import csv
from datetime import timedelta
from openpyxl import Workbook
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
)
from audit_logs.audit_service import AuditService

def export_leave_history_pdf(queryset, response):
    document = SimpleDocTemplate(response)
    elements = []
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Employee Leave History",styles["Heading1"],))
    data = [
        [
            "Employee",
            "Leave Type",
            "Start",
            "End",
            "Days",
            "Status",
        ]
    ]

    for leave in queryset:
        data.append([
            str(leave.employee),
            leave.leave_type.name,
            str(leave.start_date),
            str(leave.end_date),
            str(leave.total_days),
            leave.status,
        ])
    table = Table(data)
    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ])
    )
    elements.append(table)
    document.build(elements)
    return response

def export_leave_register_excel(queryset):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Annual Leave Register"
    headers = [
        "Employee",
        "Leave Type",
        "Start Date",
        "End Date",
        "Days",
        "Status",
    ]
    sheet.append(headers)
    for leave in queryset:
        sheet.append([
            str(leave.employee),
            leave.leave_type.name,
            leave.start_date,
            leave.end_date,
            float(leave.total_days),
            leave.status,
        ])
    return workbook

def export_leave_transactions_csv(queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="leave_transactions.csv"'
    writer = csv.writer(response)
    writer.writerow([
        "Employee",
        "Leave Type",
        "Start Date",
        "End Date",
        "Days",
        "Status",
    ])

    for leave in queryset:

        writer.writerow([
            leave.employee,
            leave.leave_type.name,
            leave.start_date,
            leave.end_date,
            leave.total_days,
            leave.status,
        ])

    return response

def log_leave_action(user, action, leave_request):

    AuditService.create_log(
        user=user,
        action=action,
        model_name="LeaveRequest",
        object_id=leave_request.id,
        description=(
            f"{action} - "
            f"{leave_request.employee.employee_id}"
        ),
    )

def calculate_working_days(start_date, end_date):
    total_days = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            total_days += 1
        current_date += timedelta(days=1)
    return total_days