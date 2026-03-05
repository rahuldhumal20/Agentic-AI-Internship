# FastAPI Day 1 Assignment 

This repository contains my solutions for the **FastAPI Day 1 Practice Tasks** as part of the **Agentic AI Internship – February 2026**.

The assignment focuses on building basic REST APIs using **FastAPI**, working with endpoints, filtering data, and performing simple operations on a product dataset.

---

##  Technologies Used

* Python 3
* FastAPI
* Uvicorn
* Swagger UI (API Testing)

---

##  Project Structure

```
Agentic-AI-Internship
│
└── ASSIGNMENT 1
      ├── main.py
      ├── Q1_Output.png
      ├── Q2_Output.png
      ├── Q3_Output.png
      ├── Q4_Output.png
      ├── Q5_Output.png
      |── Swagger_UI.png
      └── Bonus_Output.png
```

---

##  How to Run the Project

1. Clone the repository

```
git clone https://github.com/rahuldhumal20/Agentic-AI-Internship.git
```

2. Navigate to the assignment folder

```
cd "Agentic AI Internship/IN226095102_FASTAPI/Assignment-1"
```

3. Create virtual environment

```
python -m venv venv
```

4. Activate virtual environment

Windows:

```
venv\Scripts\activate
```

5. Install dependencies

```
pip install fastapi uvicorn
```

6. Run the FastAPI server

```
uvicorn main:app --reload
```

7. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

##  Implemented Endpoints

### 1. Get All Products

```
GET /products
```

Returns all products and total count.

---

### 2. Filter Products by Category

```
GET /products/category/{category_name}
```

Examples:

```
/products/category/Electronics
/products/category/Stationery
```

Returns products belonging to a specific category.

---

### 3. Get In-Stock Products

```
GET /products/instock
```

Returns only available products and their count.

---

### 4. Store Summary

```
GET /store/summary
```

Returns:

* Total products
* In-stock products
* Out-of-stock products
* Available categories

---

### 5. Search Products by Name

```
GET /products/search/{keyword}
```

Example:

```
/products/search/mouse
/products/search/book
```

Search is **case-insensitive**.

---

##  Bonus Endpoint

### Product Deals

```
GET /products/deals
```

Returns:

* Cheapest product (Best Deal)
* Most expensive product (Premium Pick)

---