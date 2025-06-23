from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Update these with your XAMPP MySQL credentials
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"  # replace with actual DB name
)
cursor = db.cursor()

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()

    for item in data:
        name = item['name']
        price = float(item['price'])
        quantity = int(item['quantity'])
        subtotal = price * quantity

        query = "INSERT INTO cart_items (product_name, price, quantity, subtotal) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, price, quantity, subtotal))

    db.commit()
    return jsonify({"message": "Cart items added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
