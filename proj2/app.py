from flask import Flask, request
#Why does the name have to be "app"
from db import stores, items
import uuid
from flask_smorest import abort
app = Flask(__name__)
"""
This should be in DB.py
stores = {}
items = {
    1: {
        "name": "X-Energy Sandiabite",
        "price": 2.55
    },
    2: {
        "name": "Avena Quaker",
        "price": 3.25

    }
}
"""
@app.get("/store")
#you have to access "http://127.0.0.1:5000/store"
#JSONis a string in JavaScript Object Notation
def get_stores():
    return {"stores": list(stores.values())}
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")
    store_id = str(uuid.uuid4()) #we use uuid b/c we don't have a db yet
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store,201

#"The first implementation used the JSON below"
#"Note even commas affect in the slightest"
#{"name":"Proxi"} is correct 
#{"name":"Proxi",} raises an error

@app.post("/item")
def create_item():
    item_data = request.get_json()
    #print(item_data)
    #check integrity of the payload
    if("store_id" not in item_data or 
       "price" not in item_data or
       "name" not in item_data
       ):
        abort(400, message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload")
    #check if the store id provided is in stores
    if(item_data["store_id"] not in stores):
        abort(404, message="Store not found.")
    item_id = str(uuid.uuid4())
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201
#query string: /store?name=Proxi or/store?name=My Store 

#the method below only returns the store
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try: 
        return stores[store_id],201
    except KeyError:
        abort(404, message="Store not found")


#the method below returns all items
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

#the method below returns the particular item  
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try: 
        return items[item_id]
    except KeyError: 
        abort(404, message="Item not found")

