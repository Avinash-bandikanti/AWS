from flask import Flask, jsonify

import json

app = Flask(__name__)

# Read the courses data from config.json
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    courses = config_data.get("courses",{})

@app.route('/')
def index():
    return "Welcome to the course API"

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify({'courses': courses})

@app.route('/courses/<string:course_id>', methods=['GET'])
def get_course(course_id):
    course = courses.get(course_id)
    if course:
        return jsonify({'course': course})
    else:
        return jsonify({'error': 'Course not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
