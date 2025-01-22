from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the data
with open('data.json', 'r') as f:
    student_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [next((student['marks'] for student in student_data if student['name'] == name), None) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()
