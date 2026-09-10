from pydantic import BaseModel


class ProfileUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    address: str | None = None
    profile_image: str | None = None
    artist_details: str | None = None
    gender: str | None = None


class ProfileResponse(ProfileUpdate):
    user_id: str
    email: str