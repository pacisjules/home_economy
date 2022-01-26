from datetime import date
from pydantic import BaseModel, Field
from sqlalchemy import Float


class SavingCreate(BaseModel):
    user_id: str = Field(..., example="User_Id")
    saving_name: str = Field(..., example="Saving name")
    description: str = Field(..., example="description")
    currency:str = Field(..., example="Currency Used")
    income: float    = Field(..., example="Money you save")
    target: str    = Field(..., example="your target")


class SavingList(BaseModel):
    id: str
    user_id: str
    saving_name: str 
    description: str 
    currency:str
    income: float  
    target: str 
    status: str
    created_at: str
