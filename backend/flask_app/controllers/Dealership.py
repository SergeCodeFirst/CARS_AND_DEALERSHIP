from flask_app import app
from flask_app import jsonify

@app.route("/api")
def Home():
    greet = {
        "home": "Welcome home : )"
    }
    return jsonify(greet)