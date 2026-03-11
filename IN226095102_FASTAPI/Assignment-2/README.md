# FastAPI Day 2 Assignment 

This folder contains my solutions for **FastAPI Day 2 Practice Tasks** completed during the **Agentic AI Internship – February 2026**.

The assignment focuses on implementing **query parameters, POST APIs, Pydantic validation, and business logic in FastAPI**.



#  How to Run the Project

1️⃣ Activate virtual environment

```
venv\Scripts\activate
```

2️⃣ Install required packages

```
pip install fastapi uvicorn
```

3️⃣ Run the FastAPI server

```
uvicorn main:app --reload
```

4️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

#  Implemented Endpoints

## 1️⃣ Filter Products by Minimum Price

```
GET /products/filter
```

Example:

```
/products/filter?min_price=400
/products/filter?min_price=100&max_price=600
```

Filters products based on price range and category.

---

## 2️⃣ Get Product Price

```
GET /products/{product_id}/price
```

Returns only **product name and price**.

Example response:

```
{
  "name": "Wireless Mouse",
  "price": 499
}
```

---

## 3️⃣ Customer Feedback API

```
POST /feedback
```

Accepts customer feedback using **Pydantic validation**.

Fields:

* `customer_name`
* `product_id`
* `rating` (1–5)
* `comment` (optional)

Example response:

```
{
 "message": "Feedback submitted successfully",
 "feedback": {...},
 "total_feedback": 1
}
```

---

## 4️⃣ Product Summary Dashboard

```
GET /products/summary
```

Returns store statistics including:

* Total products
* In-stock count
* Out-of-stock count
* Most expensive product
* Cheapest product
* Product categories

---

## 5️⃣ Bulk Order API

```
POST /orders/bulk
```

Allows companies to place multiple orders at once.

Features:

* Validates order items
* Checks stock availability
* Calculates total price
* Returns confirmed and failed items separately

Example response:

```
{
 "company": "TechCorp",
 "confirmed": [...],
 "failed": [...],
 "grand_total": 1497
}
```

---

#  Bonus Feature – Order Status Tracking

### Place Order

```
POST /orders
```

Orders are initially created with status **pending**.

### Get Order by ID

```
GET /orders/{order_id}
```

Returns details of a specific order.

### Confirm Order

```
PATCH /orders/{order_id}/confirm
```

Updates order status from **pending → confirmed**.

---

#  Output Screenshots

Screenshots of API responses are included for evaluation.

Example files:

* Q1_Output.png
* Q2_Output.png
* Q3_Output.png
* Q4_Output.png
* Q5_Output.png
* Bonus - Patch confirm changes it to confirmed.png
* Bonus- status as pending

All endpoints were tested using **Swagger UI**.

---


