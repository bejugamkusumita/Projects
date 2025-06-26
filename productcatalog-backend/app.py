from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key")

# ✅ Enable CORS with credentials
CORS(app,
     resources={r"/*": {"origins": "https://productcatalog-frontend-r2j4.onrender.com"}},
     supports_credentials=True,
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

# ✅ MongoDB connection
mongo_uri = "mongodb+srv://Kusumita:Kusumita%402005@cluster1.yhsaoaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(mongo_uri)
db = client["shop"]
user_collection = db["users"]
cart_collection = db["cart_items"]

@app.route('/')
def home():
    return "✅ Flask backend is live. POST to /signup or /login to manage users."


# ✅ Signup route
@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if user_collection.find_one({'email': email}):
            return jsonify({"message": "Email already registered."}), 409

        hashed_password = generate_password_hash(password)
        user_collection.insert_one({
            "email": email,
            "username": username,
            "password": hashed_password
        })

        return jsonify({"message": "User registered successfully!"}), 201

    except Exception as e:
        return jsonify({"message": "Signup error", "error": str(e)}), 500


# ✅ Login route with session support
@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = user_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['email'] = user['email']
            session['username'] = user['username']
            return jsonify({
                "message": "Login successful",
                "username": user['username'],
                "email": user['email']
            }), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401

    except Exception as e:
        return jsonify({"message": "Login error", "error": str(e)}), 500


# ✅ Add to cart (session-based)
@app.route('/add_to_cart', methods=['POST', 'OPTIONS'])
def add_to_cart():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        email = session.get("email")
        if not email:
            return jsonify({"message": "User not logged in"}), 401

        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({"message": "Invalid cart format"}), 400

        # Optional: Clear old items
        cart_collection.delete_many({"email": email})

        for item in data:
            item['email'] = email
            cart_collection.insert_one(item)

        return jsonify({"message": "Cart stored successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


# ✅ Get cart (session-based)
@app.route('/get_cart', methods=['GET'])
def get_cart():
    try:
        email = session.get("email")
        if not email:
            return jsonify({"message": "User not logged in"}), 401

        items = list(cart_collection.find({"email": email}, {'_id': 0, 'email': 0}))
        return jsonify({"cart": items}), 200

    except Exception as e:
        return jsonify({"message": "Cart retrieval error", "error": str(e)}), 500


# ✅ Optional: Clear cart
@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    try:
        email = session.get("email")
        if not email:
            return jsonify({"message": "User not logged in"}), 401

        cart_collection.delete_many({"email": email})
        return jsonify({"message": "Cart cleared successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Cart clear error", "error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
