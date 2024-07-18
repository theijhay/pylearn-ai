## Python Teaching Bot

## Project Overview
The Python Teaching Bot is an interactive chatbot designed to help users learn Python programming. It leverages natural language processing to understand user queries and provide relevant answers or guidance on Python-related topics. The bot is built using Rasa for the chatbot engine, Quart for the backend, and HTML/CSS/JavaScript for the frontend.


## Table of Contents
- Project Overview
- Technologies Used
- Installation
- Usage
- Contributors


## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Quart
- Chatbot Engine: `Rasa`
- Database: PostgreSQL
- Hosting: Local development server (e.g., Python HTTP server)


## Installation
To set up the Python Teaching Bot locally, follow these steps:

1. Clone the Repository:
```
git clone https://github.com/yourusername/python-teaching-bot.git
cd Py-teaching-bot
```
2. Set Up the Backend:
Create and activate a virtual environment:
```
python3 -m venv myenv
source myenv/bin/activate
```
- Install the required Python packages:
```
pip install -r requirements.txt
```
- Navigate to the backend directory:
```
cd backend
```
3. Set Up Rasa:

- Train the Rasa model:
```
rasa train
```
- Run the Rasa server:
```
rasa run --enable-api
```
4. Run the Backend:

- Start the Quart server:
```
python3 app.py
```
5. Set Up the Frontend:

- Navigate to the frontend directory:
```
cd ../frontend
```
- Start a local HTTP server:
```
python3 -m http.server 5500
```

## Usage
1. Access the Frontend:

- Open a web browser and go to `http://127.0.0.1:5500/index.html`.
2. Interact with the Bot:

- Type a message in the input field and press Enter or click the "Send" button.
- The bot will respond with relevant information or guidance on Python programming.



## Contributors
- [Olawale Isaac](https://github.com/theijhay) Project Lead, Backend Developer
- [Avellin](https://github.com/Avellin003) Frontend Developer
- [Amarachi Ogbonnaya](https://github.com/LoveCode20): Rasa Model Trainer


## Conclusion
The Python Teaching Bot is a comprehensive tool designed to assist users in learning Python programming through interactive conversations. With the integration of Rasa for natural language processing and a robust backend built with Quart, the bot provides accurate and helpful responses to user queries. Future improvements will focus on enhancing the user experience, expanding the knowledge base, and deploying the application for wider use.




- Feel free to contribute to this project by submitting issues or pull requests on the GitHub repository. 