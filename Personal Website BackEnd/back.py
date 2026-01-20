from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

MONGO_URI = "...."

client = MongoClient(MONGO_URI)
db = client["my_database"]  
collection = db["messages"] 

@app.route('/')
def home():
    return "Flask backend is running!"

@app.route('/submit', methods=['POST'])
def receive_message():
    data = request.json  
    message = data.get('message')  

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400
    collection.insert_one({"message": message})
    
    return jsonify({"status": "success", "message": "Message stored in database!"})

if __name__ == '__main__':
    app.run(debug=True)
