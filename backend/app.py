# backend/app.py
from flask import Flask
from auth.routes import auth_bp
import firebase_config  # Ensure Firebase is initialized

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True)
