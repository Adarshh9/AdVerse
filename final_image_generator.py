from diffusers import DiffusionPipeline
import torch
import random


festival_name = 'Diwali'
wisher_name = 'SORT club'

def generate_images(festival_name, wisher_name):
    general_keywords = "celebration, joy, lights, happiness, festivities"
    emotion_keywords = "heartfelt, exhilarating, vibrant, unforgettable"
    visual_keywords = "sparkling lights, vivid colors, joyous moments, festive atmosphere"

    prompts = [
    f"festival wish for the {festival_name} celebration by {wisher_name}.Imagine the {visual_keywords} creating an {emotion_keywords} atmosphere of {general_keywords}.",
    f"festival wish for {festival_name} image from {wisher_name}.Capture the joy with {general_keywords} and {visual_keywords}.",
    f"festival wish for {festival_name} image from {wisher_name}.Capture the joy and celebrate with {general_keywords}.",
    f"festival wish for {festival_name} image from {wisher_name}.Infuse the scene with {general_keywords} and spread the festive joy!",#effective one
    f"festival wish a masterpiece for {festival_name} by {wisher_name}.Blend in the {general_keywords} and paint the canvas with vibrant celebrations!",#creative one
    f"festival wish post for {festival_name} image from {wisher_name}.Incorporate {general_keywords} and radiate festive cheer!"#precise one
    f"festival wish a captivating {festival_name} poster from {wisher_name}.Infuse it with the essence of {general_keywords} and let the festivities come to life!"
    ]


    prj_path = '' #"festival-model"
    model = '' #"stabilityai/stable-diffusion-xl-base-1.0"
    pipe = DiffusionPipeline.from_pretrained(
    model,
    torch_dtype=torch.float16,
    )
    pipe.to("cuda")
    pipe.load_lora_weights(prj_path, weight_name="pytorch_lora_weights.safetensors")
    
    seed = 42
    generator = torch.Generator("cuda").manual_seed(seed)
    
    images = []
    image_paths = []
    selected_numbers = random.sample(range(6), 3)
    for i in selected_numbers:
        prompt = prompts[i]
        image = pipe(prompt=prompt, generator=generator).images[0]
        image_path = f"generated_image{i}.png"
        image.save(image_path)
        images.append(image)
        image_paths.append(image_path)
        
    return images , image_paths
