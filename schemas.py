from pydantic import EmailStr, BaseModel


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
