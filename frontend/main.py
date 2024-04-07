from fastapi import FastAPI

app = FastAPI()

food_items = {
    'Indian' : ['Samosa','Dosa','Idli'],
    'American' :['French fries', 'Pizza'],
    'Italian' : ['Pasta']
}


# Define a route at the root web address ("/")
@app.get("/get_items/{Cuisine}")

async def get_root(Cuisine):
    return food_items.get(Cuisine)