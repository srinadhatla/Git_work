import logging
import time


from django.http import HttpResponseForbidden


from .models import BlockedIP

request_logger = logging.getLogger("request_logger")
security_logger = logging.getLogger("security_logger")
application_logger = logging.getLogger("application_logger")


class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)
        user = "Anonymous"

        if hasattr(request, "user") and request.user.is_authenticated:
            user = request.user.username

        request_logger.info(
            f"""
URL : {request.path}
Method : {request.method}
User : {user}
IP : {request.META.get('REMOTE_ADDR')}
Response Time : {response_time} ms
"""
        )
        application_logger.info(f"Request: {request.method} {request.path} by {request.user}")
        return response
    
    
application_logger = logging.getLogger('application_logger')

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time  = time.time()
        response_time = (end_time - start_time) * 1000
        
        if response_time>500:
            application_logger.warning(f"Slow Response: {request.path} took {response_time:.2f} ms")
            
        return response
    
class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        
        if BlockedIP.objects.filter(ip_address=ip).exists():
            security_logger.warning(f"Blocked IP Access attempt: {ip} on {request.path}")
            return HttpResponseForbidden("403 Forbidden - Your IP is blocked.")
        return self.get_response(request)