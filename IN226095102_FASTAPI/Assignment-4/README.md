# FastAPI Day 5 Assignment – Cart System 

This folder contains the implementation of the **FastAPI Day-5 Cart System Practice** completed during the **Agentic AI Internship – February 2026**.

The goal of this assignment was to build a **shopping cart workflow using FastAPI APIs**, connecting multiple endpoints such as adding products to the cart, viewing the cart, removing items, and completing checkout.

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

## 1️⃣ Add Product to Cart

```
POST /cart/add
```

Example:

```
/cart/add?product_id=1&quantity=2
```

Features:

* Adds item to cart
* Calculates subtotal automatically
* Updates quantity if product already exists in cart

---

## 2️⃣ View Cart

```
GET /cart
```

Returns:

* Cart items
* Number of unique items
* Grand total of cart

Example response:

```
{
 "items": [...],
 "item_count": 2,
 "grand_total": 1097
}
```

---

## 3️⃣ Remove Product from Cart

```
DELETE /cart/{product_id}
```

Removes a product from the cart.

Example response:

```
{
 "message": "Notebook removed from cart"
}
```

---

## 4️⃣ Checkout Cart

```
POST /cart/checkout
```

Creates orders from cart items.

Request body example:

```
{
 "customer_name": "Rahul",
 "delivery_address": "Pune ,Maharashtra "
}
```

Example response:

```
{
 "message": "Checkout successful",
 "orders_placed": [...],
 "grand_total": 1497
}
```

After checkout:

* Cart becomes empty
* Orders are stored in the orders list

---

# ⭐ Bonus Case – Empty Cart Checkout

If checkout is attempted when the cart is empty:

```
POST /cart/checkout
```

Response:

```
{
 "error": "Cart is empty — add items first"
}
```

Status Code: **400 Bad Request**

---

# 📸 Output Screenshots

Screenshots of API responses are included for evaluation.

Example files:

* Q1.1_Output.png
* Q1.2_Output.png
* Q2_Output.png
* Q3.1_Output.png
* Q3.2_Output.png
* Q3.3_Output.png
* Q4.1_Output.png
* Q4.2_Output.png
* Q5.1_Output.png
* Q5.2_Output.png
* Q5.3_Output.png
* Q5.4_Output.png
* Q5.5_Output.png
* Q6.1_Output.png
* Q6.2_Output.png
* Bonus_1_Output.png
* Bonus_2_Output.png
* Bonus_3_Output.png

All endpoints were verified using **Swagger UI**.

---
