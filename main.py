from flask import Flask
from flask_cors import CORS
from sending_req import send_req_bp

app=Flask(__name__)

CORS(app)

@app.route("/")
def homepage():
    return "Welecome to my chatboat"


app.register_blueprint(send_req_bp)

if __name__=="__main__":
    app.run(debug=True)

