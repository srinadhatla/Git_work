import csv

from io import TextIOWrapper, StringIO

from .models import Employee, Department


def import_csv(file):
    decoded_file = TextIOWrapper(file.file,encoding="utf-8")
    reader = csv.DictReader(decoded_file)
    required_headers = [
        "Employee ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Department",
        "Designation",
        "Salary",
        "Joining Date"
    ]

    if reader.fieldnames != required_headers:
        return {"error":"Invalid CSV headers"}
    total = 0
    created = 0
    failed = 0
    errors = []

    for row in reader:
        total += 1
        try:
            if Employee.objects.filter(email=row["Email"]).exists():
                raise Exception("Duplicate email")
            
            dept, _ = Department.objects.get_or_create(name=row["Department"])
            Employee.objects.create(
                
                employee_id=row["Employee ID"],
                first_name=row["First Name"],
                last_name=row["Last Name"],
                email=row["Email"],
                phone=row["Phone"],
                department=dept,
                designation=row["Designation"],
                salary=row["Salary"],
                joining_date=row["Joining Date"]
            )

            created += 1
        except Exception as e:
            failed += 1
            errors.append({"row": total,"error": str(e)})

    return {"total_rows": total,"created": created,"failed": failed,"errors": errors}
    
def export_csv():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "Employee ID",
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Department",
            "Designation",
            "Salary",
            "Joining Date"
        ]
    )

    employees = Employee.objects.all()
    for emp in employees:
        writer.writerow(
            [
                emp.employee_id,
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.phone,
                emp.department.name
                if emp.department else "",
                emp.designation,
                emp.salary,
                emp.joining_date
            ]
        )
    return output.getvalue()

def export_csv():
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(
        [
            "Employee ID",
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Department",
            "Designation",
            "Salary",
            "Joining Date"
        ]
    )

    employees = Employee.objects.all()
    for emp in employees:
        writer.writerow(
            [
                emp.employee_id,
                emp.first_name,
                emp.last_name,
                emp.email,
                emp.phone,
                emp.department.name
                if emp.department else "",
                emp.designation,
                emp.salary,
                emp.joining_date
            ]
        )
    return output.getvalue()