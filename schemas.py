from pydantic import BaseModel
from typing import Optional


class PasswordResetRequest(BaseModel):
    email: str

class UserOut(BaseModel):
    username: str
    email: str

class Profile(BaseModel):
    occupation: str
    house_address: str
    phone_number: str
    # image: str

class Profiles(BaseModel):
    email:str

class UserCreate(BaseModel):
    first_name: str
    last_name:str
    email: str
    password: str

class UserCreates(BaseModel):
    id: int
    first_name:str
    last_name:str
    email: str
    password: str
 
# Login model
class UserLogin(BaseModel):
    email: str
    password: str

# Login response model
class UserResponse(BaseModel):
    # email: str
    status: str
    class Config:
        orm_mode = True  

class Feedbacks(BaseModel):
    message1: str
    message2: str
    message3: str

class Reminder(BaseModel):
    date: str
    message: str
    email: str        


class model_input(BaseModel):
    preg : int
    glu : int
    bp : int
    skin : int
    insulin : int
    bmi : float
    dpf : float
    age : int    
class prediction_history(BaseModel):   
    preg : int
    glu : int
    bp : int
    skin : int
    insulin : int
    bmi : float
    dpf : float
    age : int   
    result : int

class Token(BaseModel):
    access_token: str
    token_type: str   
    status: str

class TokenData(BaseModel):
    id: Optional[str] = None       

class tok(BaseModel):
    token: str

    