from pydantic import BaseModel

class userBaseModel(BaseModel): 
    emp_id:int
    emp_role: str
