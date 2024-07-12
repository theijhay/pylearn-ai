import os
from rasa.core.agent import Agent
import logging

def load_specific_model(model_name):
    """
    Load a specific Rasa model given the model name.

    Args:
    - model_name (str): The name of the model file.

    Returns:
    - Agent: An agent object that can be used to parse messages.
    """
    # Construct the model path
    model_path = os.path.join('..', 'py_rasa_bot', 'models', model_name)
    logging.info(f"Looking for model at: {model_path}")
    
    # Check if the model file exists
    if os.path.exists(model_path):
        logging.info(f"Loading model from {model_path}")
        agent = Agent.load(model_path)
        logging.info("Model loaded successfully")
        return agent
    else:
        logging.error(f"Model {model_name} not found in the models directory.")
        raise FileNotFoundError(f"Model {model_name} not found in the models directory.")
