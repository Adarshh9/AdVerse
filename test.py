from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://vighnesh97531:vighnesh@cluster0.ghyrbpj.mongodb.net/?retryWrites=true&w=majority')
db = client['image_database']
collection = db['images']

@app.route('/')
def welcome():
    print ("Endpoint Hit")
    return "Hello"

# Create operation - Add a new image
@app.route('/api/images', methods=['POST'])
def add_image():
    if request.method == 'POST':
        image_data = request.files['image']
        image_name = image_data.filename
        image_id = collection.insert_one({'image_name': image_name}).inserted_id
        
        # Save the image file to a folder or cloud storage
        image_data.save(f'uploads/{image_id}_{image_name}')

        return jsonify({'message': 'Image added successfully', 'image_id': str(image_id)}), 201

# Read operation - Get all images
@app.route('/api/images', methods=['GET'])
def get_all_images():
    images = list(collection.find({}, {'_id': 1, 'image_name': 1}))
    return jsonify({'images': images}), 200

# Update operation - Update image details
@app.route('/api/images/<image_id>', methods=['PUT'])
def update_image(image_id):
    if request.method == 'PUT':
        new_image_name = request.json.get('new_image_name')
        collection.update_one({'_id': ObjectId(image_id)}, {'$set': {'image_name': new_image_name}})
        return jsonify({'message': 'Image updated successfully'}), 200

# Delete operation - Delete an image
@app.route('/api/images/<image_id>', methods=['DELETE'])
def delete_image(image_id):
    if request.method == 'DELETE':
        image = collection.find_one({'_id': ObjectId(image_id)})
        if image:
            # Delete the image from the folder or cloud storage if needed
            collection.delete_one({'_id': ObjectId(image_id)})
            return jsonify({'message': 'Image deleted successfully'}), 200
        else:
            return jsonify({'message': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
