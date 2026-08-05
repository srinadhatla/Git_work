from django.db import models
from employees.models import Employee


class Document(models.Model):
    DOCUMENT_TYPES = (
        ("RESUME", "Resume"),
        ("OFFER", "Offer Letter"),
        ("ID_PROOF", "ID Proof"),
        ("CERTIFICATE", "Certificate"),
        ("OTHER", "Other"),
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="documents")
    document_type = models.CharField(max_length=20,choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to="employee_documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.document_type}"