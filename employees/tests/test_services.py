from django.test import TestCase
from unittest.mock import patch, Mock

from employees.models import Employee, Department

class EmailServiceTest(TestCase):

    @patch("employees.services.email_service.send_mail")
    def test_send_email_called(self, mock_send):

        mock_send.return_value = True

        result = mock_send(
            "Welcome Email",
            "Hello Employee",
            "from@test.com",
            ["employee@test.com"]
        )

        self.assertTrue(result)

        mock_send.assert_called_once()
        mock_send.assert_called_with(
            "Welcome Email",
            "Hello Employee",
            "from@test.com",
            ["employee@test.com"]
        )

class PDFServiceTest(TestCase):

    @patch("employees.views.generate_employee_profile_pdf")
    def test_pdf_generation(self, mock_pdf):
        mock_pdf.return_value = b"fake pdf data"
        result = mock_pdf("employee_object")

        self.assertEqual(result,b"fake pdf data")

        mock_pdf.assert_called_once()

class QRCodeTest(TestCase):

    @patch("employees.services.qr_service.generate_qrcode")
    def test_qrcode_generation(self, mock_qr):
        mock_qr.return_value = "qr_image.png"

        result = mock_qr("EMP00001")

        self.assertEqual(result,"qr_image.png")

        mock_qr.assert_called_once_with("EMP00001")

    def test_file_upload(self):
        fake_file = Mock()
        fake_file.name = "employee.xlsx"
        self.assertEqual(fake_file.name,"employee.xlsx")

@patch("requests.post")
def test_payroll_api(self, mock_post):
    mock_post.return_value.status_code = 200

    response = mock_post("https://payroll-api.com/generate")

    self.assertEqual(response.status_code,200)

@patch("employees.services.email_service.send_mail")
def test_email_exception(self, mock_send):
    mock_send.side_effect = Exception("Email server down")

    with self.assertRaises(Exception):
        mock_send()