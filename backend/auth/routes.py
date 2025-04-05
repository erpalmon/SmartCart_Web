# backend/auth/routes.py
from flask import Blueprint, request, jsonify
import firebase_admin # type: ignore
from firebase_admin import auth # type: ignore
from firebase_admin._auth_utils import EmailAlreadyExistsError # type: ignore
from firebase_admin.exceptions import FirebaseError # type: ignore

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    try:
        user = auth.create_user(email=email, password=password)
        return jsonify({"message": "User created", "uid": user.uid}), 201
    except EmailAlreadyExistsError:
        return jsonify({"error": "Email already in use"}), 409
    except FirebaseError as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({
        "message": "Login should be handled on the client using Firebase Auth SDK.",
        "note": "Verify tokens here if needed."
    }), 200

