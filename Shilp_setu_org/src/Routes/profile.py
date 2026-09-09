from fastapi import APIRouter

profile_route=APIRouter(prefix="/profile")

#-----------1) Get / Profile

@profile_route.get("/{id}")
def get_profile(id:int):
    return



#-----------2)PUT / profile
@profile_route.get("/{id}")
def get_profile(id:int):
    return

