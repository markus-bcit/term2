from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product
from models import Order
# from models import ProductsOrder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/")
def home():
    data = Product.query.all()
    return render_template("index.html", products=data)


@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    product = db.session.get(Product, name.lower())
    product_json = product.to_dict()
    return jsonify(product_json)


@app.route("/api/product", methods=["POST"])
def api_create_product():
    data = request.json
    # Check all data is provided
    for key in ("name", "price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )

    product = Product(
        name=data["name"],
        price=price,
        quantity=quantity,
    )
    db.session.add(product)
    db.session.commit()
    return "Item added to the database"

@app.route("/api/product/<string:name>", methods=["DELETE"])
def api_delete_product(name):
    product = db.session.get(Product, name.lower())
    db.session.delete(product)
    db.session.commit()
    return 'Product deleted from the database'

@app.route("/api/product/<string:name>", methods=["PUT"])
def api_update_product(name):
    data = request.json
    # Check all data is provided
    
    if 'price' not in data.keys() and 'quantity' not in data.keys():
        return f"The JSON provided is invalid", 400
    
    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )
    product = db.session.get(Product, name.lower())
    product.price = price
    product.quantity = quantity
    db.session.commit()
    return 'Product updated'

@app.route("/api/product/<int:order_id>", methods=["GET"])
def api_get_order(order_id):
    order = db.session.get(Order, order_id)
    order_json = order.to_dict()
    return jsonify(order_json)

if __name__ == "__main__":
    app.run(debug=True)
