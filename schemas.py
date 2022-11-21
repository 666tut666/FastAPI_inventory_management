from pydantic import EmailStr, BaseModel
from datetime import date


class AdminCreate(BaseModel):
    email: EmailStr
    password: str


class ShowAdmin(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode=True
            ##orm object relationship mapper
            ##object lai dictionary banayo


class ItemCreate(BaseModel):
    title: str
    type: str
    category: str
    quantity: int

    class Config:
        orm_mode=True


class ShowItem(BaseModel):
    title: str
    type: str
    category: str
    quantity: int
    date_posted: date

    class Config:
        orm_mode=True
