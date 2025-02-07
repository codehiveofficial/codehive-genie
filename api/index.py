from flask import Flask, request, jsonify, Response
from groq import Groq
from dotenv import load_dotenv
import os
import logging
from langdetect import detect, DetectorFactory
from flask_cors import CORS


DetectorFactory.seed = 0


load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

AUTH_SECRET = os.getenv('AUTH_SECRET')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY is missing. Please check your .env file.")

client = Groq(api_key=GROQ_API_KEY)


app = Flask(__name__)
CORS(app)

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
    auth_secret_fetched = request.headers.get('Authorization') or request.headers.get('authorization') or request.json.get('authorization') or request.json.get('Authorization')
    if not auth_secret_fetched:
        return jsonify({'error': 'Authorization header is required.'}), 401
    
    if auth_secret_fetched != AUTH_SECRET:
        return jsonify({'error': 'Invalid authorization secret.'}), 401
    
    try:
       
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({'error': 'Query parameter is required.'}), 400

        
        # detected_language = detect(user_query)
        # if detected_language != 'en':
        #     return jsonify({'error': 'Only English language input is supported.', 'detected_language': detected_language}), 400

        
        logging.info(f"Processing query: {user_query}")

        
        temperature = 0.6
        max_tokens = 1500
        top_p = 0.9

        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an advanced AI assistant specializing in generating and explaining high-quality code. "
                        "You can write and analyze code in Python, C, JavaScript, Java, TypeScript, and CPP (C plus plus). "
                        "When responding, adhere to the following rules:\n"
                        "- Always include comments to explain the code.\n"
                        "- Include concise explanations for how the code works.\n"
                        "- Use proper formatting and structure for clarity.\n"
                        "- Anything you generate should be high-quality and production-ready.\n"
                        "- Anything not related to coding or Programming should be ignored and  your reply should be formal that you are AI Assistant tuned for coding and programming purpose only and you cannot assist that just on point dont extend it.\n"
                        "- Response should be in English only.\n Response should be concise and to the point."
                        "- Say sorry to assist for irrelevant queries that are not related to coding or programming."
                        "- Do not Generate code for languages other than Python, C, JavaScript, Java, TypeScript, and CPP (C plus plus)."
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
