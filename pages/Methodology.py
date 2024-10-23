import streamlit as st
from helper_functions import func
from helper_functions.utility import check_password

# Methodology
# Depicts image illustrating the workflow for this application

st.set_page_config(
page_title="HDB Resale Guru",  
page_icon="🏠",  
layout="wide")

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


st.image("data/Flowchart.png", caption="Methodology", use_column_width=True)

with st.sidebar:
    st.page_link('main.py', label='About Us', icon='🏠')
    st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
    st.page_link('pages/Negotiation Advisor.py', label='Negotiation Advisor', icon='🤵')
    st.page_link('pages/Resale Price Analyzer.py', label='Resale Price Analyzer', icon='🕵️‍♀️')