from django.core.mail import send_mail


def send_email(subject, message, recipient):
    return send_mail(
        subject,
        message,
        "noreply@example.com",
        [recipient]
    )