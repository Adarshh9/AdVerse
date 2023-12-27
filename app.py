from flask import Flask, request, jsonify

app = Flask(__name__)

# Define variables to store received data
company_name = ""
product_description = ""
tagline_text = ""
theme = ""
ad_type = ""

# Endpoint to receive data from React frontend
@app.route('/api/endpoint', methods=['POST'])
def receive_data():
    global company_name, product_description, tagline_text, theme, ad_type
    
    if request.method == 'POST':
        # Retrieving data from the request
        company_name = request.form.get('companyName')
        product_description = request.form.get('productDescription')
        tagline_text = request.form.get('taglineText')
        theme = request.form.get('theme')
        ad_type = request.form.get('adType')


        print("Company name : " , company_name)
        print("Product Description : " ,product_description )
        print("Tagline : " ,tagline_text )
        print("Theme : " ,theme )
        print("Ad Type : " ,ad_type)


        # Returning a success message or data
        return jsonify({'message': 'Data received and stored successfully'}), 200
    else:
        return jsonify({'message': 'Invalid request method'}), 405

# Endpoint to retrieve stored data
@app.route('/api/retrieve', methods=['GET'])
def retrieve_data():
    global company_name, product_description, tagline_text, theme, ad_type

    # Returning the stored data
    data = {
        'companyName': company_name,
        'productDescription': product_description,
        'taglineText': tagline_text,
        'theme': theme,
        'adType': ad_type
    }
    print("Company name : " , company_name)
    print("Product Description : " ,product_description )
    print("Tagline : " ,tagline_text )
    print("Theme : " ,theme )
    print("Ad Type : " ,ad_type)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)  # Running the Flask app in debug mode