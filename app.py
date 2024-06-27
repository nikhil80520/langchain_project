from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

KEY = os.getenv('GOOGLE_API_KEY')

def get_response(question):
    if not KEY:
        raise ValueError("GOOGLE_API_KEY is not set in the environment variables")
    
    # Initialize the ChatGoogleGenerativeAI object with the correct parameters
    llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=KEY)
    
    # Prepare the input in the expected format
    messages = [{"role": "user", "content": question}]
    
    # Get the response from the model
    try:
        response = llm.predict(messages)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

st.set_page_config(page_title='Q&A Demo')

st.header('Langchain Application')

input = st.text_input('Input: ', key='input')

submit = st.button('Ask the question')

if submit:
    response = get_response(input)
    if response:
        st.subheader('The Response is')
        st.write(response)
    else:
        st.subheader('There was an error in processing your request.')
