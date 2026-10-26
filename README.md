# Vehicle Lookup API

A small FastAPI service that returns vehicle and owner details for a registration number, deployed as a serverless function on Vercel.

**Live:** https://vehicle-api-nine.vercel.app

> All data is fictional demo data: made-up names, placeholder ID numbers and generic avatars.

## Endpoint

`GET /vehicle/{car_number}` returns the owner's name, ID number, photo (base64), car model, year and province. Unknown numbers return `404`.

```bash
curl https://vehicle-api-nine.vercel.app/vehicle/ABC-101
```

Interactive docs: `/docs`

## Run locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## Stack

Python · FastAPI · Pydantic · Vercel
