import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")


# Healthcare-specific response logic 
def healthcare_chatbot(user_input):
    
    # Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "Please consult Doctor for acurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the doctor"
    elif "medication" in user_input:
        return "It's important to take the prescribed medication regularly. If you have any concerns, consult your doctor. "
    else:
        response = chatbot(user_input, max_length = 500,num_return_sequences = 1)
    return response[0]['generated_text']


def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you ?")
    if st.button("Submit"):
        if user_input:
            st.write("User :", user_input)
            with st.spinner("processing your query, Please wait..."):
                 response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :", response)
            print(response)
        else:
            st.write("Please enter the message to get the response")
main()
