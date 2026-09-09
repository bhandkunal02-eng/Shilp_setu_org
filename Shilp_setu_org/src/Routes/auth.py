#----------Auth------
from src.app.Main import app


# 1) Signup
@app.post("/signup")
def signup():
    return {"Status":"SignUP done Sucessfully","DATA":" "}


# 2)Login
@app.post("/login")
def signup():
    return {"Status":"Login done Sucessfully","DATA":" "}


