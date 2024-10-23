import streamlit as st
from helper_functions import func
from helper_functions.utility import check_password

## Create a LLM-assisted bot for better analysis of HDB Resale Price

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

## Load HDB historical resale data
st.title("HDB Resale Price Analyzer")
df = func.load_data()

## For user to select the parameters
st.header("Price Range Prediction")
st.write("To have a rough idea of how much your ideal flat cost, do tell me what are the type of flats that you are looking at and I will predict the price range for you.")
flat_type = st.selectbox("Select Flat Type", df['flat_type'].unique())
storey_range = st.selectbox("Select Storey Range", df['storey_range'].unique())
location = st.selectbox("Select Location", df['town'].unique())
age_of_flat = st.slider("Select Age of Flat (years)", 0, 99, 10)

## For prediction of price range
if st.button("Predict Price Range"):
    func.price_range_prediction(flat_type, storey_range, location, age_of_flat)


## For user to input the parameter to analyze the price factors
st.header("Price Factors Interpreter")
st.write("To understand the various factors that affects resale price in the region, indicate below the location that you are looking at.")
location_cause = st.selectbox("Select your desired location", df['town'].unique())

## Submit for processing
if st.button("Submit"):
    with st.spinner("Working hard to analyze for you..."):
        analysis = func.root_cause_analysis(location_cause)
        st.write(analysis)

# User inputs for custom insights
st.header("Insights Analysis")
location_insight = st.selectbox("Select your Location", df['town'].unique())
flat_type_insight = st.selectbox("Select your Flat Type", df['flat_type'].unique())
user_question = st.text_area("Ask a question about resale prices, trends, or insights:", 
                             "What are the price trends in this area?")

if st.button("Get Insights"):
    with st.spinner("Generating Insights..."):
        analysis = func.custom_insights_analysis(location_insight, flat_type_insight, user_question)
        st.markdown('<div class="custom-text">'+ analysis + '</div>', unsafe_allow_html=True)