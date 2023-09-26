from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/endpoint1', methods=['GET'])
def endpoint1():
    return jsonify({'message': 'You have reached endpoint 1'}), 200

@app.route('/endpoint2', methods=['GET'])
def endpoint2():
    return jsonify({'message': 'You have reached endpoint 2'}), 200

@app.route('/endpoint3', methods=['GET', 'POST'])
def endpoint3():
    if request.method == 'GET':
        app.logger.info("Received GET on endpoint3")
        return jsonify({'message': 'You have reached endpoint 3 via GET'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.info(f"Received POST on endpoint3 with data: {data}")
        return jsonify({'message': 'You have reached endpoint 3 via POST', 'received_data': data}), 200

@app.route('/endpoint4', methods=['GET', 'POST'])
def endpoint4():
    if request.method == 'GET':
        app.logger.info("Received GET on endpoint4")
        return jsonify({'message': 'You have reached endpoint 4 via GET'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.info(f"Received POST on endpoint4 with data: {data}")
        return jsonify({'message': 'You have reached endpoint 4 via POST', 'received_data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
