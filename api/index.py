from flask import Flask, request, jsonify, Response
from groq import Groq
from dotenv import load_dotenv
import os
import logging
from langdetect import detect, DetectorFactory


DetectorFactory.seed = 0


load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY is missing. Please check your .env file.")

client = Groq(api_key=GROQ_API_KEY)


app = Flask(__name__)

@app.route('/')
def home():
    """Home route for health check."""
    return 'Hello, World!'

@app.route('/genie', methods=['POST'])
def genie():
    """
    Endpoint to interact with the Groq AI model.
    Accepts a JSON payload with 'query' and validates that it's in English.
    """
    try:
       
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({'error': 'Query parameter is required.'}), 400

        # Check if the input is in English
        # detected_language = detect(user_query)
        # if detected_language != 'en':
        #     return jsonify({'error': 'Only English language input is supported.', 'detected_language': detected_language}), 400

        # Log the query
        logging.info(f"Processing query: {user_query}")

        
        temperature = 0.6
        max_tokens = 1500
        top_p = 0.9

        
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an advanced AI code assistant. Generate clear, efficient code tailored to the user's request. "
                        "You can write in Python, C, JavaScript, Java, TypeScript, and C#. Provide detailed comments and explanations "
                        "when appropriate."
                    )
                },
                {"role": "user", "content": user_query}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=True,
        )

        
        def stream_response():
            response = ""
            for chunk in completion:
                delta = chunk.choices[0].delta.content or ""
                response += delta
                yield delta
            logging.info("Response fully generated.")
        
        return Response(stream_response(), content_type='text/plain')

    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        return jsonify({'error': 'An error occurred while processing the request.', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
