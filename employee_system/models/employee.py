from pydantic import BaseModel

class employeeBaseModel(BaseModel):
    emp_id: int 
    emp_name: str
    emp_email: str
    department:str
    salary:int
    experience:int
