from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Replace with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://leonardolin9943:i5H3s#BX..U2H6e@lighttukko.n41fv.mongodb.net/?retryWrites=true&w=majority&appName=Lighttukko"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["my_database"]  # Replace with your database name
collection = db["messages"]  # Create a collection to store messages

@app.route('/')
def home():
    return "Flask backend is running!"

@app.route('/submit', methods=['POST'])
def receive_message():
    data = request.json  # Get the incoming JSON data
    message = data.get('message')  # Extract the message

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    # Store message in MongoDB
    collection.insert_one({"message": message})
    
    return jsonify({"status": "success", "message": "Message stored in database!"})

if __name__ == '__main__':
    app.run(debug=True)
#LBfEghMlGrtHQ5kz