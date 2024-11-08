import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# SQLite Database Connection
def create_connection():
    return sqlite3.connect("vehicle_database.db")

# Fetch data function
def fetch_data(car_number: str):
    with create_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM registered_vehicles WHERE car_number = ?", (car_number,))
            row = cursor.fetchone()
            if row:
                user_pic = row[3]
                if isinstance(user_pic, bytes):
                    user_pic = user_pic.hex()  # Convert binary data to a hex string for JSON serialization
                data = {
                    "id": row[0],
                    "user_name": row[1],
                    "user_cnic": row[2],
                    "user_pic": user_pic,
                    "car_number": row[4],
                    "car_name": row[5]
                }
            else:
                data = None
        except sqlite3.Error as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        finally:
            cursor.close()
    
    return data

# Define the POST request body model
class CarData(BaseModel):
    car_number: str

# GET request to fetch vehicle data
@app.get("/")
async def get_vehicle(car_number: str):
    data = fetch_data(car_number)
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Car number not found")

# POST request to fetch vehicle data
@app.post("/")
async def post_vehicle(car_data: CarData):
    data = fetch_data(car_data.car_number)
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Car number not found")

# Function to send internal requests for testing purposes
@app.on_event("startup")
async def test_internal_api():
    async with httpx.AsyncClient() as client:
        # Simulate a GET request to the FastAPI app
        response_get = await client.get("http://127.0.0.1:8000/?car_number=MNO-5678")
        print(f"GET request response: {response_get.status_code} - {response_get.text}")

        # Simulate a POST request to the FastAPI app
        data_post = {"car_number": "MNO-5678"}
        response_post = await client.post("http://127.0.0.1:8000/", json=data_post)
        print(f"POST request response: {response_post.status_code} - {response_post.text}")
