AdVerse
Overview

The Ad Generation Project aims to create personalized advertisements using user inputs for products. The key feature of this project is the ability to generate ads in the user's native language with the help of our AI models.
Features

    Dynamic Ad Creation: Allows users to input product details such as company name, product name, theme, and product descriptions.
    Language Customization: Generates ad content in the user's native language based on provided inputs.
    AI-Powered Image Generation: Utilizes AI models to create images with product information and taglines.
    Future Scope - Audio Integration: Future plans involve converting images into videos and adding ad slogans or audio in the user's native language.

Technologies Used

    AI Models: Utilizes natural language processing (NLP) and image generation models to create personalized ad content.
    Programming Languages: Python, JavaScript (for potential web integration).
    Frameworks/Libraries: TensorFlow, PyTorch, OpenCV.
    Version Control: Git/GitHub.

Folder Structure

    Final_Image.png,Final_Image_2.png : Which stores the final image of the products produced by our Model.
    License : GNU General Public License v3.0
    Main.ipynb : It consists :-
        OpenAI : It helps for creatting prompts to produce images from the Sttable Difussion
        Stable Difussion : It a pretrained model which generatees images on prompts and we fine tunes those to enhance the ads precision.
        Google Translator : Its used for translating English Tagline to Natives Language Taglines
        Forground Image Model - Text to image generator which is a text in a png format to add the text on the images generated.
        Merger Model : Its the model thats used to take the image generated from Stable Difusion and Foreground Image Model and create a final images as an ad.

Future Enhancements

    Video Ad Generation It would create Video Ads (for eg. 5 - 15 sec ads)
    Audio Integration: Adding voiceovers or audio elements to ads in the user's native language.
    Size Customization: The User would be able to customizze sizes for the posts or banner.

License

This project is licensed under the GNU General Public License v3.0.
