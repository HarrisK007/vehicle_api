from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import base64

app = FastAPI()

# Dummy data in memory (no separate database)
def convert_to_binary(image_name):
    with open(image_name, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

data = [
    {
        "user_name": 'Dr Asghar Chandio',
        "user_cnic": '34567-8901234-5',
        "user_pic": convert_to_binary("chairman.jpg"),
        "car_number": 'BLV-977',
        "car_name": 'Cultus',
        "year" : "2018",
        "province": ' Sindh '
        
    },
    {
        "user_name": 'Sahil',
        "user_cnic": '45678-9012345-6',
        "user_pic": convert_to_binary("sahil.jpeg"),
        "car_number": 'GS-3270',
        "car_name": 'Cultus',
        "year" : "2018",
        "province": ' Sindh '
    },
    {
        "user_name": 'Harris',
        "user_cnic": '56789-0123456-7',
        "user_pic": convert_to_binary("Harris.jpeg"),
        "car_number": 'BPE-917',
        "car_name": 'Alto',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'Sarah Wilson',
        "user_cnic": '67890-1234567-8',
        "user_pic": convert_to_binary("Harris.jpeg"),
        "car_number": 'RST-7890',
        "car_name": 'Hyundai Elantra',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'Chris Miller',
        "user_cnic": '78901-2345678-9',
        "user_pic": convert_to_binary("sahil.jpeg"),
        "car_number": 'UVW-4567',
        "car_name": 'Kia Optima',
        "year" : "2019",
        "province": ' Sindh '
        
    },
    {
        "user_name": 'Amanda Taylor',
        "user_cnic": '89012-3456789-0',
        "user_pic": convert_to_binary("Harris.jpeg"),
        "car_number": 'XYZ-0123',
        "car_name": 'Mazda 3',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'James Anderson',
        "user_cnic": '90123-4567890-1',
        "user_pic": convert_to_binary("sahil.jpeg"),
        "car_number": 'DEF-6789',
        "car_name": 'Tesla Model 3',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'Emma Thomas',
        "user_cnic": '01234-5678901-2',
        "user_pic": convert_to_binary("Harris.jpeg"),
        "car_number": 'GHI-3456',
        "car_name": 'Volkswagen Jetta',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'Olivia Martinez',
        "user_cnic": '23456-7890123-3',
        "user_pic": convert_to_binary("sahil.jpeg"),
        "car_number": 'JKL-1234',
        "car_name": 'BMW 3 Series',
        "year" : "2019",
        "province": ' Sindh '
    },
    {
        "user_name": 'William Lee',
        "user_cnic": '34567-8901234-4',
        "user_pic": convert_to_binary("Harris.jpeg"),
        "car_number": 'MNO-5678',
        "car_name": 'Mercedes-Benz C-Class',
        "year" : "2019",
        "province": ' Sindh '
    },
]

# Data model for the response
class VehicleInfo(BaseModel):
    user_name: str
    user_cnic: str
    user_pic: str
    car_number: str
    car_name: str
    year: str
    province:str

# GET endpoint to retrieve data by car_number
@app.get("/vehicle/{car_number}", response_model=VehicleInfo)
def get_vehicle_info(car_number: str):
    for vehicle in data:
        if vehicle["car_number"] == car_number:
            return vehicle
    raise HTTPException(status_code=404, detail="Vehicle not found")

# Run with: uvicorn <filename>:app --reload
