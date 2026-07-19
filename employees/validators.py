from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 5 * 1024 * 1024
    
    if file.size > max_size:
        raise ValidationError("Maximum file size allowed 5 mb.")
    
def validate_image_extension(file):
    valid_extensions = ['jpg','jpeg','png']
    extension = file.name.split('.')[-1].lower()
    
    if extension not in valid_extensions:
        raise ValidationError("Image can be only in formats JPEG, JPG and PNG")

def validate_pdf_extension(file):
    extension = file.name.split('.')[-1].lower()
    if extension != "pdf":
        raise ValidationError("Only PDF files are allowed")
        