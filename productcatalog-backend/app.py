from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Connect to MongoDB Atlas (embedded password)
mongo_uri = "mongodb+srv://Kusumita:Kusumita%402005@cluster1.yhsaoaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(mongo_uri)

# Use a database (name it whatever you like)
db = client["shop"]
cart_collection = db["cart_items"]

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No data received"}), 400

        for item in data:
            name = item['name']
            price = float(item['price'])
            quantity = int(item['quantity'])
            subtotal = price * quantity

            document = {
                "product_name": name,
                "price": price,
                "quantity": quantity,
                "subtotal": subtotal
            }

            cart_collection.insert_one(document)

        return jsonify({"message": "Cart items added to MongoDB successfully!"}), 201

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Error saving cart items", "error": str(e)}), 500
@app.route('/')
def home():
    return "✅ Flask backend is live. POST to /add_to_cart to save cart data."
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

