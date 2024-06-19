from flask import Flask, request
#Why does the name have to be "app"
app = Flask(__name__)

stores = [
    {
        "name": "My Store", 
        "items": [{
            "name": "chair",
            "price": 69.96
            }

        ]
    }
]
@app.get("/store")
#you have to access "http://127.0.0.1:5000/store"
#JSONis a string in JavaScript Object Notation
def get_stores():
    return {"stores": stores}
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

#"The first implementation used the JSON below"
#"Note even commas affect in the slightest"
#{"name":"Proxi"} is correct 
#{"name":"Proxi",} raises an error

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores: 
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
#query string: /store?name=Proxi or/store?name=My Store 

#the method below only returns the store
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores: 
        #make sure to never have redundancies
        if store["name"] == name:
            return store, 201
    return {"message": "Store not found"}, 404

#the method below returns the items in store
@app.get("/store/<string:name>/item")
def get_all_items_in_store(name):
    for store in stores: 
        #make sure to never have redundancies
        if store["name"] == name:
            return {"items": store["items"]}, 201
    return {"message": "Store not found"}, 404

