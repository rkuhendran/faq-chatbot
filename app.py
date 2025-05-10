import streamlit as st

st.title("Very Basic Chatbot")

def simple_bot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye!"
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need?"
    else:
        return "I'm not sure how to respond to that."

user_input = st.text_input("You:")
if user_input:
    response = simple_bot(user_input)
    st.write(f"Bot: {response}")
