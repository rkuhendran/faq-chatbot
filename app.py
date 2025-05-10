import streamlit as st
from transformers import pipeline
import os

# --- Title and Instructions ---
st.set_page_config(page_title="FAQ Chatbot", layout="centered")
st.title("📚 AI-Powered FAQ Chatbot")
st.write("Ask a question based on our FAQ. Example questions:")
st.markdown("- How do I reset my password?\n- What is your return policy?\n- What payment methods are accepted?")

st.markdown("---")

# --- Load Hugging Face Question Answering Model ---
@st.cache_resource
def load_model():
    return pipeline("question-answering")

qa_pipeline = load_model()

# --- FAQ Context (Hardcoded) ---
faq_context = """
You can reset your password by clicking 'Forgot Password' on the login page.
Shipping typically takes 3–5 business days. We accept Visa, Mastercard, and PayPal.
Returns are accepted within 30 days of purchase with receipt.
Customer support is available via email from 9am to 6pm Monday to Friday.
"""

# --- User Input ---
question = st.text_input("❓ Your question:")

if question:
    with st.spinner("Generating answer..."):
        result = qa_pipeline({
            'question': question,
            'context': faq_context
        })
        answer = result['answer']
    st.success(f"💡 **Answer:** {answer}")

    # --- Feedback Buttons ---
    st.markdown("Was this answer helpful?")
    col1, col2 = st.columns(2)

    if col1.button("👍 Helpful"):
        with open("feedback.txt", "a") as f:
            f.write(f"{question} | Helpful\n")
        st.toast("Thanks for your feedback! 😊", icon="✅")

    if col2.button("👎 Not Helpful"):
        with open("feedback.txt", "a") as f:
            f.write(f"{question} | Not Helpful\n")
        st.toast("We'll use this to improve! 🛠️", icon="⚠️")

    # --- Optional Feedback Stats ---
    if os.path.exists("feedback.txt"):
        with open("feedback.txt") as f:
            lines = f.readlines()
            helpful = sum("Helpful" in line for line in lines)
            not_helpful = sum("Not Helpful" in line for line in lines)
        st.markdown("---")
        st.write(f"📊 Feedback Summary:")
        st.write(f"👍 Helpful: {helpful} | 👎 Not Helpful: {not_helpful}")
