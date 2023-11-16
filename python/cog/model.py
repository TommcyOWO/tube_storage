from pydantic import BaseModel, EmailStr

class Item(BaseModel):
    id: int
    quantity: int


class User(BaseModel):
    email: EmailStr
    username: str
    password: str


class coupons(BaseModel):
    coupons: str | None = None