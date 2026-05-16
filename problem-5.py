# Task 5: Gemini Chatbot App


# একটা simple Streamlit app বানাও যেখানে user একটা question type করবে এবং Gemini API সেটার answer দেবে।

# Requirements
# st.text_input() দিয়ে user-এর question নাও
# একটা Ask Gemini button রাখো
# Button click করলে Gemini API-তে question পাঠাও এবং response st.markdown() দিয়ে দেখাও
# .env file থেকে API key load করো — directly code-এ লেখা যাবে না


import streamlit as st
from api_calling import ans_generator

st.title("Question Answer Generator" ,anchor= False)

text = st.text_input("", placeholder="Write your question here")

button = st.button("Ask Gemini", type='primary')

if button:
    if not text:
        st.error("Write question first")

    else:
        try:
            with st.spinner("Generating answer"):
                gen_answer = ans_generator(text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

        else:
            with st.container(border=True):
                st.markdown(gen_answer)            
        