from fastapi import APIRouter
from src.controler.profile_controler import get_user_profile, update_user_profile
from src.schema.schema_profile import ProfileUpdate

profile_route=APIRouter(prefix="/profile")

#-----------1) Get / Profile

@profile_route.put("/{id}")
def update_profile(id: int, payload: ProfileUpdate):
    return update_user_profile(id, payload)



#-----------2)PUT / profile
@profile_route.get("/{id}")
def get_profile(id:int):
    return get_user_profile(id)
