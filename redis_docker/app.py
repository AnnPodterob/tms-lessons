from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    # Обработка полученных данных
    return 'Data added successfully'

if __name__ == '__main__':
    app.run()
