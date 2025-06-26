from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key")  # ✅ Needed for session

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

# ✅ Collections
cart_collection = db["cart_items"]
user_collection = db["users"]

@app.route('/')
def home():
    return "✅ Flask backend is live. POST to /signup or /login to manage users."


# ✅ Signup route
@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        return '', 204  # Preflight
    try:
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if user_collection.find_one({'email': email}):
            return jsonify({"message": "Email already registered."}), 409

        user_collection.insert_one({
            "email": email,
            "username": username,
            "password": password  # ❗ Don't forget to hash this in production!
        })

        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"message": "Signup error", "error": str(e)}), 500


# ✅ Login route — sets session['email']
@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204  # Preflight
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = user_collection.find_one({'email': email, 'password': password})
        if user:
            session['email'] = email  # ✅ Store in session
            return jsonify({
                "message": "Login successful",
                "username": user['username'],
                "email": user['email']
            }), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    except Exception as e:
        return jsonify({"message": "Login error", "error": str(e)}), 500


# ✅ Add to cart route with user session
@app.route('/add_to_cart', methods=['POST', 'OPTIONS'])
def add_to_cart():
    if request.method == 'OPTIONS':
        return '', 204  # Preflight

    if 'email' not in session:
        return jsonify({"message": "Unauthorized. Please log in."}), 401

    try:
        email = session['email']
        data = request.get_json()

        for item in data:
            cart_collection.insert_one({
                "email": email,
                "product_name": item['name'],
                "price": float(item['price']),
                "quantity": int(item['quantity']),
                "subtotal": float(item['price']) * int(item['quantity']),
                "image": item.get('image', '')
            })

        return jsonify({"message": "Cart items added to MongoDB successfully!"}), 201
    except Exception as e:
        return jsonify({"message": "Cart saving error", "error": str(e)}), 500


# ✅ Optional: Get cart route (for future use)
@app.route('/get_cart', methods=['GET'])
def get_cart():
    if 'email' not in session:
        return jsonify({"message": "Unauthorized"}), 401

    email = session['email']
    items = list(cart_collection.find({'email': email}, {'_id': 0}))
    return jsonify(items), 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
