from src.schema.schema_profile import ProfileUpdate


def get_user_profile(user_id: int) -> dict:
    """Return a user's profile.

    Database reading can be added here later.
    """
    return {
        "user_id": user_id,
        "message": "Profile fetched successfully",
    }


def update_user_profile(user_id: int, payload: ProfileUpdate) -> dict:
    """Update a user's profile.

    For now, return the data received from the API request.
    """
    return {
        "user_id": user_id,
        "message": "Profile updated successfully",
        "profile": payload.model_dump(exclude_none=True),
    }
