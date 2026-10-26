# Vehicle Lookup API

A small FastAPI service that returns vehicle and owner details for a registration number, set up to run as a serverless function on Vercel (`vercel.json`).

> All data is fictional demo data: made-up names, placeholder ID numbers and generic avatars.

## Endpoint

`GET /vehicle/{car_number}` returns the owner's name, ID number, photo (base64), car model, year and province. Unknown numbers return `404`.

## Run locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
curl http://127.0.0.1:8000/vehicle/ABC-101
```

Interactive docs: http://127.0.0.1:8000/docs

## Stack

Python · FastAPI · Pydantic · Vercel
