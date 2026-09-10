#----------Auth------
from fastapi import APIRouter

from src.controler.auth_controler import login_user, signup_user
from src.schema.schema_auth import AuthResponse, LoginRequest, SignupRequest

auth_route = APIRouter()


# 1) Signup
@auth_route.post("/signup", response_model=AuthResponse)
def signup(payload: SignupRequest):
    return signup_user(payload)


# 2)Login
@auth_route.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest):
    return login_user(payload)
