from fastapi import APIRouter


orders_Route=APIRouter(prefix="/orders")


#1)post/order
@orders_Route.post("/neworder")
def add_new_order():
    return {"Status":"SignUP done Sucessfully","DATA":" "}







#2)get/orders/id
@orders_Route.get("/neworder/{id}")
def get_order(id:int):
    return {"Status":"order details obtained  Sucessfully","DATA":" "}




#3)put/orders/id
@orders_Route.put("/neworder/{id}")
def add_new_order():
    return {"Status":"Order updated sucessfully done Sucessfully","DATA":" "}

