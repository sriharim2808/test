from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Read a book"}
]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask ToDo API!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
