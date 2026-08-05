from django.core.mail import send_mail

class LeaveNotificationService:

    @staticmethod
    def leave_applied(leave_request):
        print(f"Leave applied: {leave_request.id}")

    @staticmethod
    def manager_approved(leave_request):
        print(f"Manager approved: {leave_request.id}")

    @staticmethod
    def hr_approved(leave_request):
        print(f"HR approved: {leave_request.id}")

    @staticmethod
    def leave_rejected(leave_request):
        print(f"Leave rejected: {leave_request.id}")

    @staticmethod
    def leave_cancelled(leave_request):
        print(f"Leave cancelled: {leave_request.id}")