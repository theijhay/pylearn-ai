from quart import Quart, request, jsonify
from logging.handlers import RotatingFileHandler
import logging

from quart_cors import cors
from dotenv import load_dotenv
import os
import sys
from models import Base, UserProgress, session
from logging_config import setup_logging
from rasa_utils import load_specific_model
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import asyncio

# Initialize Quart app
app = Quart(__name__)

app = cors(app, allow_origin="*")

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('App startup')

# Load environment variables from .env file
load_dotenv()

# Setup the logging
setup_logging()

# Specify model name
model_name = '20240623-115655-level-pond.tar.gz'

# Load the Rasa model
try:
    nlu_agent = load_specific_model(model_name)
except FileNotFoundError as e:
    logging.error(e)
    nlu_agent = None

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
async def home():
    return "Welcome to the Python Teaching Bot!"

# Define a webhook endpoint that listens for POST requests
@app.route('/webhook', methods=['POST'])
async def webhook():
    """
    Webhook endpoint to receive messages from users.
    
    Returns:
    - json: The status of the message processing.
    """
    # Parse the incoming JSON data
    data = await request.get_json()
    # Extract the 'message' field from the JSON data
    message = data.get('message')
    sender_id = data.get('sender_id')

    # If no message is provided, return a failure response with status code 400
    if not message:
        return jsonify({"status": "failed", "reason": "No message provided"}), 400
    
    # Handle the user message asynchronously
    response_text = await handle_user_message(message, sender_id)
    
    # Return a response indicating that the message has been processed
    return jsonify({"status": "processed", "response": response_text})

async def handle_user_message(message, sender_id):
    # Log the received message
    logger.info(f"Received message: {message}")
    
    # Define an asynchronous function to process the message
    async def process_message(message, sender_id):
        # Call the NLU agent to parse the message and generate a response
        try:
            responses = await nlu_agent.handle_text(message, sender_id=sender_id)
            response_text = responses[0].get("text") if responses else "Sorry, I didn't understand that."
            logger.info(f"Rasa NLU response: {response_text}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            response_text = "There was an error processing your message."
        
        # Log the generated response
        logger.info(f"Generated response: {response_text}")

        # Simulate a database operation to save user progress
        user_progress = UserProgress(user_id=1, progress_info=response_text)
        session.add(user_progress)
        session.commit()
        # Log the successful saving of user progress to the database
        logger.info("User progress saved to the database.")
        return response_text
    
    # Run the asynchronous process_message function and return the result
    response_text = await process_message(message, sender_id)
    return response_text

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("App startup")
    app.run(debug=True, port=5000)