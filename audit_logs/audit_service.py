from audit_logs.models import AuditLog

class AuditService:
    @staticmethod
    def create_log(
        user,
        action,
        model_name,
        object_id,
        description=None,
    ):
        return AuditLog.objects.create(
            user=user,
            action=action,
            model_name=model_name,
            object_id=object_id,
            description=description,
        )