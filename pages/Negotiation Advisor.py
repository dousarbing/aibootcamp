import streamlit as st
from helper_functions import llm , func
from helper_functions.utility import check_password

## Create a LLM-assisted bot to help provide scripts or strategies for better negotation deals

st.set_page_config(
page_title="HDB Resale Guru",  
page_icon="🏠",  
layout="centered")

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


with st.sidebar:
    st.page_link('main.py', label='About Us', icon='🏠')
    st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
    st.page_link('pages/Negotiation Advisor.py', label='Negotiation Advisor', icon='🤵')
    st.page_link('pages/Resale Price Analyzer.py', label='Resale Price Analyzer', icon='🕵️‍♀️')

## Guide for the user on what to include in his/her inputs
st.title("Resale Market Negotiation Chatbot")
st.write("Get tailored negotiation strategies for the resale market. Whether you're a buyer or a seller, describe your scenario, and I'll suggest a strategy.")
st.write("Do indicate as many information as possible on the good and bad conditions of the resale flat in order for me to provide a more comprehensive advice. Below are some examples:")
st.markdown("- Poor conditions of the flat")
st.markdown("- Too costly, example 30% above market price")
st.markdown("- Too far from MRT")


# Input for user's scenario
user_input = st.text_area("Describe your negotiation scenario:", 
                        placeholder="E.g., I am a buyer and the property needs some renovation. How can I negotiate for a better price?")

# Submit of user inputs to the LLM
if st.button("Get Advice"):
    if user_input:
        with st.spinner("Getting advice..."):
            prompt = func.get_negotiation_advice(user_input)   # combines system prompt and user input
            response = llm.get_completion(prompt)              # API call to LLM with the prompt to retrieve an AI response
            st.subheader("Negotiation Advice")
            st.write(response)
    else:
        st.warning("Please enter a scenario to get advice.")


