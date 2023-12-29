from flask import Flask, request, jsonify

from final_image_generator import generate_images
from diffusers import DiffusionPipeline
import torch
import random

# from final_video_audio import final_output
# from moviepy.editor import VideoFileClip, AudioFileClip
# from IPython.display import Audio, display
# import google.generativeai as palm
# from translate import Translator
# from pydub import AudioSegment
# from gtts import gTTS
# import numpy as np
# import cv2


app = Flask(__name__)

# Variable to store received data
# stored_data = {
#     'companyName': '',
#     'productDescription': '',
#     'productImage': None,
#     'taglineText': '',
#     'theme': '',
#     'adType': ''
# }

stored_data = {
    'festivalName' : '',
    'wisherName' : '',
    'languageForVideo' : ''
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
    #     stored_data['companyName'] = request.form.get('companyName', '')
    #     stored_data['productDescription'] = request.form.get('productDescription', '')
    #    # stored_data['productImage'] = request.files.get('productImage')
    #     stored_data['taglineText'] = request.form.get('taglineText', '')
    #     stored_data['theme'] = request.form.get('theme', '')
    #     stored_data['adType'] = request.form.get('adType', '')
    
    
        stored_data['festivalName'] = request.form.get('festivalName', '')
        stored_data['wisherName'] = request.form.get('wisherName', '')
        stored_data['languageForVideo'] = request.form.get('languageForVideo', '')
        
        generated_images , generated_image_paths = generate_images(festival_name=stored_data['festivalName'] ,wisher_name=stored_data['wisherName'])
        #generated_images & generated_image_paths both are array of 3 elements

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
