import streamlit as st
from helper_functions.utility import check_password
# Main page content (About Us)
# Includes Project Overview, Objectives, Data Sources and Disclaimer
def main_page():

    st.set_page_config(
    page_title="HDB Resale Guru",  
    page_icon="🏠",  
    layout="centered")
    
    
    # Do not continue if check_password is not True.  
    if not check_password():  
        st.stop()

    with st.sidebar:
        st.page_link('main.py', label='About ResiChat', icon='🏠')
        st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
        st.page_link('pages/Negotiation Advisor.py', label='Negotiation Advisor', icon='🤵')
        st.page_link('pages/Resale Price Analyzer.py', label='Resale Price Analyzer', icon='🕵️‍♀️')

    st.title("About Us")

    st.markdown("""
    ## Project Overview
    Welcome to the __ResiChat__ (Resale Intelligence Chat)! Our platform aims to assist buyers and sellers in the HDB resale market by providing intelligent insights, negotiation strategies, and price analysis using advanced language models.

    ## Objectives
    The goal of this project is to empower HDB resale buyers and sellers with the information they need to make informed decisions. By leveraging our negotiation chatbot and data analysis tools, users can better understand the factors affecting resale prices and ensure they are in a strong position when entering the market.

    ## Project Scope
    Our solution focuses on three core functionalities:
    - **Resale Market Negotiation Chatbot**: Offers advice and strategies tailored to help buyers and sellers negotiate better deals in the competitive resale market.
    - **HDB Resale Price Analyzer**: 
        - ***Price Range Prediction***: Predicts a price range for resale flats based on user inputs like location, flat type, and condition.
        - ***Price Factors Interpreter***: Analyzes key factors influencing resale prices, such as location, floor area, and lease remaining, providing a deeper understanding of market dynamics.
        - ***Insights Analysis***: Allows users to interact with the chatbot to gain insights on various topics related to the HDB resale market.

    ## Data Sources
    Our insights and analysis are based on a comprehensive dataset containing HDB resale transactions from January 2017 to October 2024. The dataset includes information on:
    - Transaction Date
    - Town
    - Flat Type
    - Block and Street Name
    - Storey Range
    - Floor Area (sqm)
    - Flat Model
    - Lease Commence Date
    - Remaining Lease (years)
    - Resale Price

    """)

    with st.expander("**DISCLAIMER**", expanded=True):
        st.write("""

    **IMPORTANT NOTICE**: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**

    Always consult with qualified professionals for accurate and personalized advice.

    """)


# Running the main function
if __name__ == '__main__':
    main_page()