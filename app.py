import streamlit as st
from transformers import pipeline

# Use a lightweight model that works well in Streamlit Cloud
chatbot = pipeline("text-generation", model="distilgpt2")

st.title("Basic AI Chatbot")
st.write("Ask anything!")

user_input = st.text_input("You:")

if user_input:
    response = chatbot(user_input, max_length=100, do_sample=True, top_k=50)
    st.write(f"Bot: {response[0]['generated_text']}")
