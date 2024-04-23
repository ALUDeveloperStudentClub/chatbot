import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()  # loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Streamlit page configuration and session state early
st.set_page_config(page_title="Q&A Demo", layout="wide")
st.header("GDSC-ALU Chatbot Demo")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'input' not in st.session_state:
    st.session_state['input'] = ''

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

def handle_send():
    input_text = st.session_state.input  # Retrieve the input text from session state
    if input_text:
        st.session_state['chat_history'].append(("You", input_text))
        response = get_gemini_response(input_text)
        full_response = " ".join(chunk.text for chunk in response)  # Concatenate all chunks
        st.session_state['chat_history'].append(("Bot", full_response))
    st.session_state['input'] = ''  # Clear the input field for the next message

# Styling the input box and messages via CSS
st.markdown("""
    <style>
    input.stTextInput>div>div>input {
        background-color: #f2f2f2; /* Light grey background */
        border: 1px solid #ccc; /* Grey border */
        border-radius: 5px; /* Rounded borders */
    }
    div.stButton>button {
        width: 100%;
        height: 3em;
    }
    </style>
""", unsafe_allow_html=True)

# Chat history container
chat_container = st.container()

# User input at the bottom
with st.container():
    input = st.text_input("Type your question here...", value=st.session_state.input, key="input")
    submit = st.button("Send", on_click=handle_send)

# Display chat history
with chat_container:
    for role, text in st.session_state['chat_history']:
        if role == "You":
            st.info(f"{role}: {text}")
        else:
            st.success(f"{role}: {text}")
