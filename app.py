import streamlit as st
from transformers import pipeline

# Load pre-trained model for text generation
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def main():
    st.title("Simple AI Chatbot")
    st.write("Chat with the AI chatbot below!")

    # Get user input
    user_input = st.text_input("You:", "")

    if user_input:
        # Generate a response from the chatbot
        response = chatbot(user_input, max_length=1000, num_return_sequences=1)
        st.write(f"Chatbot: {response[0]['generated_text']}")

if __name__ == "__main__":
    main()
