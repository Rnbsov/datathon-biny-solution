from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DataModel(BaseModel):
    order_id: str
    status: str
    location: str


# class User(BaseModel):
#     uid : UUID
#     tg_id: str
#     username : str = None
#     name: str
#     surname: str
#     avatar_url: str = None
    

# class User_data(BaseModel):
#     uid : UUID
#     user_id: str
#     height: int
#     weight: int
#     age: datetime
#     sex: str
#     symptoms: str


# class OpenAI_Answer(BaseModel):
#     uid: UUID
#     user_id: str
#     created_at: datetime
#     answer: str
#     emergence: str
#     language: str


# class Doctors(BaseModel):
#     uid: UUID
#     doctor_id: str
#     name: str
#     surname: str
#     avatar_url: str = None
#     speciality: str
#     experience: int
#     rating: float
#     price: float
#     description: str
#     email: str