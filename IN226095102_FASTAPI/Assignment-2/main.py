from fastapi import FastAPI, Query
from typing import List , Optional

from pydantic import BaseModel, Field


app = FastAPI()


# ── Temporary data — acting as our database for now ──────────

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True },
    {'id': 2, 'name': 'Notebook',       'price':  99,  'category': 'Stationery',  'in_stock': True },
    {'id': 3, 'name': 'USB Hub',         'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set',         'price':  49, 'category': 'Stationery',  'in_stock': True },
    {'id': 5, 'name':'Laptop Stand',        'price':1299,'category':'Electronics', 'in_stock': True },
    {'id': 6, 'name':'Mechanical Keyboard', 'price':2499,'category':'Electronics', 'in_stock': True },
    {'id': 7, 'name':'Webcam',              'price':1899,'category':'Electronics', 'in_stock': False }
]

orders = []

order_counter = 1


# ── Endpoint 0 — Home ────────────────────────────────────────

@app.get('/')
def home():

    return {'message': 'Welcome to our E-commerce API'}

# ── Endpoint 1 — Return all products ──────────────────────────

@app.get('/products')
def get_all_products():

    return {'products': products, 'total': len(products)}

@app.get('/products/filter')

# ______________ filter products _______________________________________________

def filter_products(

    category:  str  = Query(None, description='Electronics or Stationery'),
    max_price: int  = Query(None, description='Maximum price'),
    min_price: int = Query(None, description = 'Minimum Price'),
    in_stock:  bool = Query(None, description='True = in stock only')

):
    result = products          # start with all products
    if category:
        result = [p for p in result if p['category'] == category]
    if max_price:
        result = [p for p in result if p['price'] <= max_price]
    if min_price :
        result = [p for p in result if p['price'] >= min_price ]
    if in_stock is not None:
        result = [p for p in result if p['in_stock'] == in_stock]

    return {'filtered_products': result, 'count': len(result)}


# -------------- Q3.Show Only In-Stock Products Ass-1 ------------------

@app.get("/products/instock")
def get_instock_products():

    instock_products = [
        product for product in products
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }

#---------- Cheapest & Most Expensive Product------------

@app.get("/products/deals")
def get_deals():

    cheapest = min(products, key=lambda x: x["price"])
    Expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": Expensive
    }
#----------------Q 4 Product Summary Dashboard Ass -2 ----------------

@app.get("/products/summary")
def product_summary():
    in_stock = [p for p in products if      p["in_stock"]]
    out_stock = [p for p in products if not p["in_stock"]]
    expensive = max(products, key = lambda p: p["price"])
    cheapest  = min(products, key = lambda p: p["price"])
    categories = list(set(p["category"] for p in products))

    return {
        "total_products":   len(products),
        "in_stock_products": len(in_stock),
        "out_of__stock_products": len(out_stock),
        "most_expencive":       {"name":expensive["name"],"price":expensive["price"]},
        "chepest":              {"name":cheapest["name"],"price":cheapest["price"]},
        "categories":           categories
    }



# ---------- Q5 Search Products by Name Ass- 1 ----------

@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [
        p for p in products
        if keyword.lower() in p["name"].lower()
    ]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }
#--------Q 2 Get only Peoduct Price Ass-2----------------------

@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"name": product["name"], "price":product["price"]}
    return {"error":"Product not found"}

# ── Endpoint 2 — Return one product by its ID ──────────────────

@app.get('/products/{product_id}')
def get_product(product_id: int):

    for product in products:

        if product['id'] == product_id:

            return {'product': product}

    return {'error': 'Product not found'}


# ── Endpoint 3 — Q2 — Filter by Category ──────────────────

@app.get("/products/category/{category_name}")
def get_product_by_category(category_name: str):

    filtered = [
        product for product in products
        if product["category"].lower() == category_name.lower()

    ]
    if not filtered :
        return{"error": "No product found in this category"}
    return {
        "category": category_name ,
        "products": filtered,
        "total": len(filtered)
    }

#-----------Q4 Store info Endpoint Ass -1 --------------------

@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    instock = len([p for p in products if p["in_stock"]])
    out_of_stock = total_products - instock

    categories = list({p["category"] for p in products})

    return {
        "Store_name": "My E-commerce store",
        "total_products": total_products,
        "in_stock": instock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }
#--------------Q3 Accept Customer Feedback Ass-2------------------------------------------------
 


class CustomerFeedback(BaseModel):
    customer_name: str = Field(..., min_length=2)
    product_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = Field(None, max_length=300)


feedback = []

@app.post("/feedback")
def submit_feedback(data: CustomerFeedback):
    feedback.append(data.dict())
    return {
        "message":        "Feedback submitted successfully",
        "feedback":       data.dict(),
        "total_feedback": len(feedback),
    }

#---------------------------------Orders-------------------------


class OrderRequest(BaseModel):

    customer_name:    str = Field(..., min_length=2, max_length=100)

    product_id:       int = Field(..., gt=0)

    quantity:         int = Field(..., gt=0, le=100)

    delivery_address: str = Field(..., min_length=10)

#-----------------Q 5  Validate & Place a Bulk Order Ass -2 ---------------------

class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=1, le=50)

class BulkOrder(BaseModel):
    company_name: str = Field(..., min_length= 2)
    company_email: str = Field(..., min_length= 2)
    items: list[OrderItem]


@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):
    confirmed, failed, grand_total = [], [], 0
    for item in order.items:
        product = next((p for p in products if p["id"] == item.product_id), None)
        if not product:
            failed.append({"product_id": item.product_id, "reason": "Product not found"})
        elif not product["in_stock"]:
            failed.append({"product_id": item.product_id, "reason": f"{product['name']} is out of stock"})
        else:
            subtotal = product["price"] * item.quantity
            grand_total += subtotal
            confirmed.append({"product": product["name"], "qty": item.quantity, "subtotal": subtotal})
    return {"company": order.company_name, "confirmed": confirmed,
            "failed": failed, "grand_total": grand_total}


# ══ HELPER FUNCTIONS ══════════════════════════════════════════════

 

def find_product(product_id: int):

    """Search products list by ID. Returns product dict or None."""

    for p in products:

        if p['id'] == product_id:

            return p

    return None

 

def calculate_total(product: dict, quantity: int) -> int:

    """Multiply price by quantity and return total."""

    return product['price'] * quantity

 

def filter_products_logic(category=None, min_price=None,

                          max_price=None, in_stock=None):

    """Apply filters and return matching products."""

    result = products

    if category  is not None:

        result = [p for p in result if p['category'] == category]

    if min_price is not None:

        result = [p for p in result if p['price'] >= min_price]

    if max_price is not None:

        result = [p for p in result if p['price'] <= max_price]

    if in_stock  is not None:

        result = [p for p in result if p['in_stock'] == in_stock]

    return result

 
#---------------------orders -----------------------------------

@app.post('/orders')

def place_order(order_data: OrderRequest):

    global order_counter

 

    product = find_product(order_data.product_id)

    if not product:

        return {'error': 'Product not found'}

 

    if not product['in_stock']:

        return {'error': f"{product['name']} is out of stock"}

 

    total = calculate_total(product, order_data.quantity)

 

    order = {

        'order_id':         order_counter,

        'customer_name':    order_data.customer_name,

        'product':          product['name'],

        'quantity':         order_data.quantity,

        'delivery_address': order_data.delivery_address,

        'total_price':      total,

        'status':           'pending',

    }

    orders.append(order)

    order_counter = order_counter + 1

    return {'message': 'Order placed successfully', 'order': order}


#------------------------- new GET by order ID--------------------------


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            return {"order": order}
    return {"error": "Order not found"}



@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = "confirmed"
            return {"message": "Order confirmed", "order": order}
    return {"error": "Order not found"}
