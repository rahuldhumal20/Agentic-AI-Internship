# FastAPI Day 6 Assignment – Search, Sort & Pagination

This folder contains the implementation of the **FastAPI Day-6 Assignment** completed during the **Agentic AI Internship – February 2026**.

The goal of this assignment was to build **real-world API features** like **Search, Sorting, and Pagination**, and combine them into a single powerful endpoint.

---

# How to Run the Project

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

# Implemented Endpoints

## 1. Search Products

```
GET /products/search
```

Example:

```
/products/search?keyword=mouse
```

Features:

* Case-insensitive search
* Partial matching supported
* Friendly message if no products found

---

## 2. Sort Products

```
GET /products/sort
```

Example:

```
/products/sort?sort_by=price&order=asc
```

Features:

* Sort by **price** or **name**
* Ascending / Descending order
* Default sorting: price (asc)
* Error handling for invalid parameters

---

## 3. Paginate Products

```
GET /products/page
```

Example:

```
/products/page?page=1&limit=2
```

Features:

* Pagination using page & limit
* Returns total pages
* Handles empty pages gracefully

---

## 4. Search Orders

```
GET /orders/search
```

Example:

```
/orders/search?customer_name=rahul
```

Features:

* Case-insensitive search
* Finds all matching orders
* Returns total count
* Friendly message if no results found

---

## 5. Sort Products by Category + Price

```
GET /products/sort-by-category
```

Features:

* First sorts by **category (A–Z)**
* Then sorts by **price (low → high)** within each category

Output order:

* Electronics → cheaper first
* Stationery → cheaper first

---

## 6. Browse Products (Search + Sort + Pagination)

```
GET /products/browse
```

Example:

```
/products/browse?keyword=e&sort_by=price&order=asc&page=1&limit=2
```

Features:

* Combines:

  * Search
  * Sorting
  * Pagination
* All parameters optional
* Industry-level API design

---

# Bonus Endpoint – Orders Pagination

```
GET /orders/page
```

Example:

```
/orders/page?page=1&limit=3
```

Features:

* Pagination applied to orders list
* Same logic as product pagination
* Useful for admin dashboards

---

# Output Screenshots

Screenshots of API responses are included for evaluation.

Example files:

* Q1.1_Output.png
* Q1.2_Output.png
* Q1.3_Output.png
* Q1.4_Output.png
* Q2.1_Output.png
* Q2.2_Output.png
* Q2.3_Output.png
* Q2.4_Output.png
* Q2.5_Output.png
* Q3.1_Output.png
* Q3.2_Output.png
* Q3.3_Output.png
* Q3.4_Output.png
* Q3.5_Output.png
* Q4_Output.png
* Q5_Output.png
* Q6.1_Output.png
* Q6.2_Output.png
* Q6.3_Output.png
* Bonus_Output.png

All endpoints were verified using **Swagger UI**.

---



