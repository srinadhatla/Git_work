from rest_framework.throttling import UserRateThrottle


class EmployeeThrottle(UserRateThrottle):
    rate = '100/min'

class LoginThrottle(UserRateThrottle):
    rate = '5/min'