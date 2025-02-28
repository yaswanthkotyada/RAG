import os
from flask import Flask
from flask_cors import CORS
from sending_req import send_req_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def homepage():
    return "Welcome to my chatbot"

app.register_blueprint(send_req_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
