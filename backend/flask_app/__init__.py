from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "Not_YoUr_KEy"