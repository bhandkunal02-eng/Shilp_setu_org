from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    email: str
    password: str = Field(min_length=8)
    confirm_password: str = Field(min_length=8)
    first_name: str
    last_name: str
    phone_number: str


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    status: str
    data: str = ""