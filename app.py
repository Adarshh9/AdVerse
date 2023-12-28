from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable to store received data
stored_data = {
    'companyName': '',
    'productDescription': '',
    'productImage': None,
    'taglineText': '',
    'theme': '',
    'adType': ''
}

@app.route('/')
def welcome():
    print ("Endpoint Hit")
    return "Hello"


# Endpoint to receive data from the frontend
@app.route('/api/endpoint', methods=['POST'])
def receive_data():
    global stored_data

    if request.method == 'POST':
        stored_data['companyName'] = request.form.get('companyName', '')
        stored_data['productDescription'] = request.form.get('productDescription', '')
       # stored_data['productImage'] = request.files.get('productImage')
        stored_data['taglineText'] = request.form.get('taglineText', '')
        stored_data['theme'] = request.form.get('theme', '')
        stored_data['adType'] = request.form.get('adType', '')

        return jsonify({'message': 'Data received and stored successfully'}), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 405

# Endpoint to retrieve stored data
@app.route('/api/retrieve', methods=['GET'])
def retrieve_data():
    global stored_data

    return jsonify(stored_data)

if __name__ == '__main__':
    app.run(debug=True)
