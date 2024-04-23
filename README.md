# AI Chatbot with Gemini API

Welcome to the AI Chatbot application using Gemini API. This application demonstrates how to build an interactive chatbot that can answer questions and assist users by leveraging the power of Google's Generative AI.

## Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

To get started with the chatbot application, you need to install the necessary Python libraries. Run the following command in your terminal:

```bash
pip install streamlit google-generativeai python-dotenv
```

## Configuration

After installation, you need to set up your environment variables. Obtain your [Gemini API key](https://aistudio.google.com/app/apikey) and store it in a `.env` file at the root of your project directory:

```makefile
GOOGLE_API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with the actual API key provided by Google. For now you cannot get an API key with your school google account, use a personal google account instead.

## Running the Chatbot

To run the chatbot application, use the following command:

```bash
streamlit run chatbot.py
```

Replace `chatbot.py` with the actual name of your chatbot code file if it's different.

## Usage

Once the application is running, open your web browser and navigate to the local server address provided by Streamlit (usually `http://localhost:8501`). You should see the chatbot interface where you can type your questions and interact with the Gemini AI.

## Features

- Interact with the Gemini AI in a conversational format.
- View the chat history in a text-message-like interface.

## Support

For any questions or issues, please consult the [Gemini API documentation](https://developers.google.com/generative-ai) or reach out in the GDSC Whatsapp groupchat.
