from logs.models import SecurityLog


def log_security_event(user, request, action, status):
    ip = request.META.get("REMOTE_ADDR")
    SecurityLog.objects.create(
        user=user,
        ip_address=ip,
        action=action,
        status=status
    )