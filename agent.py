import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Muhammad whose goal is to aid users with their translation in other languages. 
        Make sure to introduce yourself in your initial message."""})
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Muhammad whose goal is to aid users to translate their messages in English message. 
        If a user messages you anything, you just need to transalate that message in to Arabic Language.
         Do not respond to off-topic inquiries"""})
    stream = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream