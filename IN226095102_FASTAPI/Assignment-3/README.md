# FastAPI Day 4 Assignment-3 – CRUD Operations 

This folder contains the implementation of **FastAPI Day 4 Practice Tasks** completed during the **Agentic AI Internship – February 2026**.

The assignment focuses on implementing **CRUD APIs (Create, Read, Update, Delete)** and performing operations on product data using FastAPI.

---

#  How to Run the Project

1. Create virtual environment

```
python -m venv venv
```

2. Activate virtual environment

```
venv\Scripts\activate
```

3. Install dependencies

```
pip install fastapi uvicorn
```

4. Run FastAPI server

```
uvicorn main:app --reload
```

5. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

All APIs were tested using Swagger UI.

---

#  Implemented Endpoints

##  Product Inventory Audit

```
GET /products/audit
```

Returns a summary of store inventory.

Response includes:

* Total products
* In-stock count
* Out-of-stock product names
* Total stock value (price × 10 units)
* Most expensive product

Example response:

```
{
 "total_products": 4,
 "in_stock_count": 3,
 "out_of_stock_names": ["USB Hub"],
 "total_stock_value": 6470,
 "most_expensive": {
   "name": "USB Hub",
   "price": 799
 }
}
```

---

#  Bonus Feature – Category Discount

```
PUT /products/discount
```

Applies a price discount to all products within a category.

Example:

```
PUT /products/discount?category=Electronics&discount_percent=10
```

Features:

* Updates all products in the selected category
* Returns number of products updated
* Shows updated prices

Example response:

```
{
 "message": "10% discount applied to Electronics",
 "updated_count": 2,
 "updated_products": [...]
}
```

---

#  Output Screenshots

Screenshots of API responses are included for evaluation.

Example files:

* Q1.1_Output.png
* Q1.2_Output.png
* Q1.3_Output.png
* Q2.1_Output.png
* Q2.2_Output.png
* Q2.3_Output.png
* Q3.1_Output.png
* Q3.2_Output.png
* Q4.1_Output.png
* Q4.2_Output.png
* Q4.3_Output.png
* Q4.4_Output.png
* Q4.5_Output.png
* Q4.6_Output.png
* Q5_Output.png
* Bonus_Discount_Output.png

All endpoints were verified using **Swagger UI**.

---
