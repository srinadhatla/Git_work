from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer


def generate_employee_profile_pdf(employee):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph("<b>Employee Profile</b>",styles["Title"]))
    
    story.append(Spacer(1, 20))
    
    story.append(Paragraph(f"<b>Employee ID:</b> {employee.employee_id}", styles["Normal"]))

    story.append(Paragraph(f"<b>Name:</b> {employee.first_name} {employee.last_name}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Email:</b> {employee.email}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Phone:</b> {employee.phone}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Department:</b> {employee.department.name}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Designation:</b> {employee.designation}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Salary:</b> {employee.salary}",styles["Normal"]))
    
    story.append(Paragraph(f"<b>Joining Date:</b> {employee.joining_date}",styles["Normal"]))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

