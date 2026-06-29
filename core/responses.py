from rest_framework.response import Response


class SuccessResponse(Response):
    def __init__(self,message="Success",data=None,status=200):
        super().__init__({"success": True,"message": message,"data": data},status=status)


class ErrorResponse(Response):
    def __init__(self,message="Error",errors=None,status=400):
        super().__init__({"success": False,"message": message,"errors": errors},status=status)