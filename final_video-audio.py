from moviepy.editor import VideoFileClip, AudioFileClip
from IPython.display import Audio, display
import google.generativeai as palm
from translate import Translator
from pydub import AudioSegment
from gtts import gTTS
import numpy as np
import cv2

#
def generate_content_for_audio(festival, wish_from):
    PALM_API_KEY = "AIzaSyC9C5e3RlBDGxMUS79VdXcyE4FapZ4EnQM"

    palm.configure(api_key = PALM_API_KEY)

    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    prompt = f'Generate a content for wishing {festival} video by {wish_from}.It should be small but sweet(10-15 words only)'

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=30,
    )

    content_for_audio = completion.result
    return content_for_audio

#
def translate_to_language(text, target_language):
    translator= Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

#
def text_to_audio(translated_text,target_language, output_path="output_audio.mp3"):
    full_text = " ".join(translated_text)
    tts = gTTS(full_text, lang=target_language, tld='co.in')
    tts.save(output_path)
    return tts

#
def get_audio_duration(audio_path):
    audio = AudioSegment.from_file(audio_path)
    duration_in_seconds = len(audio) / 1000.0
    return duration_in_seconds

#
def eng_text_to_native_audio(text, target_language):
    translated_text = translate_to_language(text, target_language)
    cleaned_translated_text = ''.join([char for char in translated_text if char != '*'])
    print([cleaned_translated_text])
    audio = text_to_audio([cleaned_translated_text],target_language, "output_audio.mp3")
    duration = get_audio_duration("output_audio.mp3")
    
    display(Audio("output_audio.mp3"))
    return audio , duration

#
def fade_in_effect(frame, frame_count, fade_factor=0.02):
    alpha = min(1.0, fade_factor * frame_count)
    
    # Apply fade-in effect to the frame
    return cv2.addWeighted(frame, alpha, np.zeros_like(frame), 0, 0)

#
def image_to_video_with_fade_in(image_path, duration, frame_rate=24, fade_factor=0.02):
    # Load the image
    img = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = img.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter("temp_output_video.mp4", fourcc, frame_rate, (width, height))

    # Repeat the image to create frames for the specified duration
    for frame_count in range(int(duration * frame_rate)):
        frame_fade_in = fade_in_effect(img, frame_count, fade_factor)
        video_writer.write(frame_fade_in)

    # Release the VideoWriter object
    video_writer.release()

    # Read the generated video
    generated_video = cv2.VideoCapture("temp_output_video.mp4")
    
    return generated_video

#
def merge_video_audio(generated_video, generated_audio, output_path):
    # Load the video clip
    video_clip = VideoFileClip(generated_video)

    # Set the audio for the video clip
    audio_clip = AudioFileClip(generated_audio)
    video_clip = video_clip.set_audio(audio_clip)

    # Write the result to a new file
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

#
def final_output( festival, wish_from, target_language, image_path ):
    
    content_for_audio = generate_content_for_audio(festival, wish_from)
    
    generated_audio , duration_of_audio = eng_text_to_native_audio(content_for_audio, target_language)
    
    duration_of_video = duration_of_audio

    generated_video = image_to_video_with_fade_in(image_path, duration_of_video)
    
    merge_video_audio('temp_output_video.mp4', 'output_audio.mp3', 'output1.mp4')
    

indian_lang_with_code = {
    'English': 'en',
    'Hindi': 'hi',
    'Telugu': 'te',
    'Tamil': 'ta',
    'Bengali': 'bn',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Urdu': 'ur'
}


#
festival = input("Enter the festival name : ")
wish_from = input("Enter the wisher name : ")
target_language = input("Enter the language in which video should be : ")
image_path = 'image1.png'

for i in indian_lang_with_code:
    if target_language == i:
        target_language = indian_lang_with_code[i]
        print('changed!')
final_output( festival, wish_from, target_language, image_path)