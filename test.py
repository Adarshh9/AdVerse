# Use of test.py 
# Its used for testing the backend codes . Please dont consider this Files as the main backend file.

from flask import Flask, request, jsonify, send_file
from io import BytesIO

app = Flask(__name__)

# Variable to store the image
stored_image = None

# Endpoint to receive and store the uploaded image
@app.route('/api/upload', methods=['POST'])
def upload_image():
    global stored_image

    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        image = request.files['image']
        print("Images entered")
        
        # Storing the image in a global variable (for demonstration purposes)
        stored_image = BytesIO()
        image.save(stored_image)
        stored_image.seek(0)  # Reset the stream position

        return jsonify({'message': 'Image uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid request method'}), 405

# Endpoint to display the stored image
@app.route('/api/display', methods=['GET'])
def display_image():
    global stored_image

    if stored_image:
        stored_image.seek(0)  # Reset the stream position
        return send_file(stored_image, mimetype='image/png')  # Change mimetype as per your image type
    else:
        return jsonify({'message': 'No image available'}), 404

if __name__ == '__main__':
    app.run(debug=True)
