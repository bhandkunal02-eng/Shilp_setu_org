
from fastapi import APIRouter

product_route=APIRouter(prefix="/product")


#1)Get all Product 
@product_route.get("/allproduct")
def all_product():
    return 

#2)Post/Product
@product_route.post("/newproduct")
def add_product():
    return


# 3)Get/Product{id}
@product_route.get("/newproduct/{id}")
def single_product(id:int):
    return


# 4)put/product
@product_route.get("/updateproduct/{id}")
def update_product(id:int):
    return



# 5)Delete/product{id}
@product_route.delete("/deleteproduct/{id}")
def delete_product(id:int):
    return









