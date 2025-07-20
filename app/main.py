from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.schemas import Product, ProductResponse
import os

app = FastAPI()

#  Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB app!"}

#  MongoDB connection URI
MONGO_URI = "mongodb+srv://jhaanurag332:jHa3GgmLvvpD79Mz@cluster0.tee8ejv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#  Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client["product_db"]
collection = db["products"]

# Helper function to convert MongoDB document
def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product.get("description"),
        "price": product["price"],
        "in_stock": product["in_stock"]
    }

#  POST - Create a product
@app.post("/products", response_model=ProductResponse)
async def create_product(product: Product):
    result = await collection.insert_one(product.dict())
    new_product = await collection.find_one({"_id": result.inserted_id})
    return product_helper(new_product)

# GET- List all products
@app.get("/products", response_model=list[ProductResponse])
async def list_products():
    products = []
    async for product in collection.find():
        products.append(product_helper(product))
    return products

# GET - Single product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_helper(product)

#PUT - Update product
@app.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product: Product):
    result = await collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = await collection.find_one({"_id": ObjectId(product_id)})
    return product_helper(updated_product)

#delete product
@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = await collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
