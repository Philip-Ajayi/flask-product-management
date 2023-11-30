from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    with open("products.json") as f:
        products = json.load(f)

    return render_template("products.html", products=products)

@app.route("/product/<product_id>")
def product(product_id):
    with open("products.json") as f:
        products = json.load(f)

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product is None:
        return render_template("404.html")

    return render_template("product.html", product=product)

@app.route("/add-product", methods=["POST"])
def add_product():
    product_name = request.form["product_name"]
    product_price = request.form["product_price"]

    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "price": product_price,
    }

    with open("products.json", "w") as f:
        products.append(new_product)
        json.dump(products, f)

    return render_template("add-product.html", message="Product added successfully!")

if __name__ == "__main__":
    app.run(debug=True)
