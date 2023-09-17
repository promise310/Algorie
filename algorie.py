import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        # Retrieve JSON data sent from the front-end form
        data = request.get_json()

        # Extract coding_description and user_code from JSON
        coding_description = data.get('coding_description', '')
        user_code = data.get('user_code', '')

        # Validate if both fields are provided
        if not coding_description or not user_code:
            return jsonify({'error': 'Both coding_description and user_code are required'}), 400

        # Perform some backend processing if needed
        result = f"Processed data: {coding_description}, {user_code}"

        # Generate a hint using OpenAI
        hint = generate_hint(coding_description, user_code)

        # Send a response back to the front-end
        return jsonify({'result': result, 'hint': hint})

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(e)
        return jsonify({'error': 'An error occurred'}), 500


# Hard coded api key.
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_hint(coding_description, user_code):
    prompt = f"Given the coding description: '{coding_description}', and user's current code: '{user_code}', please give a hint."

    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n = 1,
        stop=None,
        temperature=0.5
    )

    hint = response.choices[0].text.strip()
    return hint

if __name__ == '__main__':
    app.run(debug=True)