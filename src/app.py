from flask import Flask, jsonify, request 

app = Flask(__name__)

todos = [ {"label": "My First task", "done": False}]
todos = [ {"label": "My Second task", "done": False}]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print(todos)
    todos.append(request_body)
    print(todos)            
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position - 1)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)