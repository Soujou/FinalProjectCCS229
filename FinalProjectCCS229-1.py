#Angelica Villar BSCS3A
#Final Project in CCS229

import os
import streamlit as st
import openai

#Configure your OpenAI API key
openai.api_key = "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"

#Function to get a response from OpenAI's language model

def get_openai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        if response.choices:
            return response.choices[0].message['content'].strip()
        else:
            return "No response from the model."
    except Exception as e:
        return f"An error occurred: {str(e)}"

#Streamlit app layout
st.title("Hola! I'm June Chatbot")
user_input = st.text_input("What would you like to ask?")
if st.button("Submit"):
    if user_input:
        chatbot_response = get_openai_response(user_input)
        st.write(f"Chatbot: {chatbot_response}")
    else:
        st.write("Please enter a question or message to get a response.")
