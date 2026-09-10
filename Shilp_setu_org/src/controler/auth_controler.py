from src.schema.schema_auth import AuthResponse, LoginRequest, SignupRequest


def signup_user(payload: SignupRequest) -> AuthResponse:
    """Create a new user.

    Database saving can be added here later. For now, return a simple message.
    """
    return AuthResponse(status="SignUP done Sucessfully")


def login_user(payload: LoginRequest) -> AuthResponse:
    """Log a user in.

    Password checking can be added here later. For now, return a simple message.
    """
    return AuthResponse(status="Login done Sucessfully")
