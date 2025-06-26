from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key")

# ✅ Enable CORS with credentials support
CORS(app,
     resources={r"/*": {"origins": "https://productcatalog-frontend-r2j4.onrender.com"}},
     supports_credentials=True,
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

# ✅ Connect to MongoDB
mongo_uri = "mongodb+srv://Kusumita:Kusumita%402005@cluster1.yhsaoaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
client = MongoClient(mongo_uri)
db = client["shop"]

# ✅ MongoDB collections
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


# ✅ Get current user route
const user_id = "kusumita123" // Get this from login/session ideally

window.addEventListener('DOMContentLoaded', () => {
    fetch(`https://catalog12.onrender.com/get_cart?user_id=${user_id}`)
        .then(res => res.json())
        .then(data => {
            if (data.cart && data.cart.length > 0) {
                cart = data.cart;
                saveCart();  // save to localStorage
            }
            renderCart();
        })
        .catch(err => {
            console.error('Error loading saved cart:', err);
            renderCart(); // fallback to empty localStorage
        });
});



# ✅ Add to cart route - user specific
@app.route('/add_to_cart', methods=['POST', 'OPTIONS'])
def add_to_cart():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        data = request.get_json()
        print("Received cart:", data)
        # Save to MongoDB
        return jsonify({"message": "Cart received successfully"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong"}), 500


# ✅ Get user-specific cart
@app.route('/get_cart', methods=['GET'])
def get_cart():
    try:
        email = session.get("email")
        if not email:
            return jsonify({"message": "User not logged in"}), 401

        items = list(cart_collection.find({"email": email}, {'_id': 0, 'email': 0}))
        return jsonify(items), 200

    except Exception as e:
        return jsonify({"message": "Cart retrieval error", "error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
