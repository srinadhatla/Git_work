from pydantic import BaseModel
from .users import userBaseModel

class employeeBaseModel(BaseModel):
    emp_id: int 
    emp_name: str
    emp_email: str
    department:str
    salary:int
    experience:int
    emp_role:str
