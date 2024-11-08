from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

# In-memory data array
vehicles = [
    { "user_name": "Michael Johnson", "user_cnic": "34567-8901234-5", "user_pic": "sahil.jpeg", "car_number": "LMN-2345", "car_name": "Ford Focus" },
    { "user_name": "Emily Davis", "user_cnic": "45678-9012345-6", "user_pic": "Harris.jpeg", "car_number": "JKL-6789", "car_name": "Chevrolet Malibu" },
    { "user_name": "David Brown", "user_cnic": "56789-0123456-7", "user_pic": "sahil.jpeg", "car_number": "OPQ-3456", "car_name": "Nissan Altima" },
    { "user_name": "Sarah Wilson", "user_cnic": "67890-1234567-8", "user_pic": "Harris.jpeg", "car_number": "RST-7890", "car_name": "Hyundai Elantra" },
    { "user_name": "Chris Miller", "user_cnic": "78901-2345678-9", "user_pic": "sahil.jpeg", "car_number": "UVW-4567", "car_name": "Kia Optima" },
    { "user_name": "Amanda Taylor", "user_cnic": "89012-3456789-0", "user_pic": "Harris.jpeg", "car_number": "XYZ-0123", "car_name": "Mazda 3" },
    { "user_name": "James Anderson", "user_cnic": "90123-4567890-1", "user_pic": "sahil.jpeg", "car_number": "DEF-6789", "car_name": "Tesla Model 3" },
    { "user_name": "Emma Thomas", "user_cnic": "01234-5678901-2", "user_pic": "Harris.jpeg", "car_number": "GHI-3456", "car_name": "Volkswagen Jetta" },
    { "user_name": "Olivia Martinez", "user_cnic": "23456-7890123-3", "user_pic": "sahil.jpeg", "car_number": "JKL-1234", "car_name": "BMW 3 Series" },
    { "user_name": "William Lee", "user_cnic": "34567-8901234-4", "user_pic": "Harris.jpeg", "car_number": "MNO-5678", "car_name": "Mercedes-Benz C-Class" }
]

# Endpoint to get vehicle data by car_number
@app.get("/api/vehicle")
async def get_vehicle(car_number: Optional[str] = None):
    if car_number is None:
        raise HTTPException(status_code=400, detail="Please provide a car_number")

    # Search for the vehicle with the specified car_number
    vehicle = next((v for v in vehicles if v["car_number"] == car_number), None)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle
