# FastAPI MongoDB Products API

A sample backend application built using **FastAPI** and **MongoDB (Atlas)**. This project exposes an API to list products with optional query parameters like filtering and sorting.

## 🚀 Features

- Built using FastAPI (Python)
- Uses MongoDB Atlas (Free M0 Cluster) for data storage
- One API Endpoint: `/products` with optional filters
- Fully deployable on Render.com (Free Plan)
- Environment variable (`MONGO_URI`) managed securely via Render Dashboard

## 🗂️ Project Structure

fastapi-mongo-app/
│
├── main.py # Entry point for FastAPI app
├── models/ # Pydantic models for request/response
│ └── product_model.py
├── database/ # MongoDB connection logic
│ └── connection.py
├── routes/ # API route definitions
│ └── product_routes.py
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
└── README.md # Project description


## 📦 API Endpoint

### `GET /products`

Returns a list of products. Supports optional filters:

#### ✅ Query Parameters:
- `category` — filter by product category
- `min_price` — filter by minimum price
- `max_price` — filter by maximum price
- `sort_by` — sort by field (e.g., `price`)
- `order` — `asc` or `desc`

#### 🧪 Example Usage:

```bash
GET /products?category=electronics&min_price=100&sort_by=price&order=asc
