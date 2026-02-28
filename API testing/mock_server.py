from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load initial data from db.json
def load_initial_data():
    db_path = os.path.join(os.path.dirname(__file__), 'db.json')
    try:
        with open(db_path, 'r') as f:
            data = json.load(f)
            return data.get('studentdata', [])
    except FileNotFoundError:
        return []

# In-memory storage
students = load_initial_data()
student_id_counter = len(students) + 1 if students else 1

@app.route('/studentdata', methods=['POST'])
def create_student():
    global student_id_counter
    data = request.get_json()

    # Add ID to the student data
    student = {
        "id": student_id_counter,
        "name": data.get("name"),
        "Courses": data.get("Courses", [])
    }

    students.append(student)
    student_id_counter += 1

    return jsonify(student), 201

@app.route('/studentdata', methods=['GET'])
def get_students():
    return jsonify(students), 200

@app.route('/studentdata/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    print("Starting mock server on http://localhost:3000")
    app.run(host='0.0.0.0', port=3000, debug=False)
