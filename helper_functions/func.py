import pandas as pd
from helper_functions import llm 
import streamlit as st
from helper_functions.utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()


### Negotiation Advisor
## Prompt instructions for the LLM with examples of scenarios to consider. coupled together with the user inputs.
def get_negotiation_advice(user_input):
    prompt = f"""You are a resale market negotiation expert. Provide tailored advice for buyers and sellers to get better deals in the resale market. Here are some scenarios to consider:

        1. The property needs renovations: Advise on negotiating a reduction in price based on renovation costs.
        2. The property has disadvantages (e.g., location, view, size): Suggest how a buyer could negotiate a better price.
        3. Seller is eager to close the deal quickly: Suggest how a buyer could use this to negotiate.
        4. Buyer is looking for a bargain: Suggest ways to communicate effectively with the seller to achieve a lower price.
        5. Seller wants a premium price: Offer strategies for how the seller could justify the price to the buyer.

        User's scenario: {user_input}

        Provide a practical negotiation strategy for this scenario, considering factors like market conditions, property features, and typical negotiation tactics.
        """
    
    return prompt


#### Resale Price Analyzer
@st.cache_data
def load_data():
    df = pd.read_csv('data/Resale Price (from Jan-2017 onwards).csv')
    return df

# Price Range Prediction Function
## Generate the price range based on historical data
def price_range_prediction(flat_type, storey_range, location, age_of_flat):
    df = load_data()
    filtered_data = df[
        (df['flat_type'] == flat_type) & 
        (df['storey_range'] == storey_range) & 
        (df['town'] == location) & 
        (df['remaining_lease'] <= (99 - age_of_flat))
    ]

    # Use quantiles to estimate the price range
    min_price = filtered_data['resale_price'].quantile(0.35)
    max_price = filtered_data['resale_price'].quantile(0.65)
    st.write("Thank you for waiting. Pls see below for my output.")
    st.write(f"Estimated resale price range: ${min_price:,.0f} - ${max_price:,.0f}")
    return (min_price, max_price)

# Root Cause Analysis Function
## System prompt with examples
def root_cause_analysis(location):
    prompt = f"""
    You are an expert in Singapore real estate market. Analyze the various factors influencing HDB resale prices in {location}.
    Consider factors like proximity to MRT stations, nearby schools, nearby malls and other nearby amenities. Use historical data for trends
    Follow the examples below on the presentation of the results.

    1. Proximity to MRT Stations
    - Bukit Batok MRT (enhances accessibility to the Central Business District (CBD) and other parts of Singapore)
    - Higher Price for properties within 500-meter radius of the MRT station
    - Future development like Jurong Region Line (lead to increased demand and higher resale prices for flats in Bukit Batok)

    2. Nearby Institutions
    Presence of reputable primary and secondary schools can drive demand for HDB flats, particularly among families.
    - Bukit Batok Secondary School
    - St Anthony Primary School

    3. Nearby Malls
    - West Mall (perfect for a relaxing family weekend of shopping, dining, movies and books)

    4. Museums / Heritage / Nature Reserves
    Contains hidden gems such as disused quarries and nature parks, great for families looking for a green and restful respite on weekends
    - Former Ford Factory
    - Bukit Batok Town park
    
    5. Other Amenities
    - Fei Yue Family Service Centre (long-time stalwart supporting families living in the area)

    """
    response = llm.get_completion(prompt)
    return response

## Insights Analysis
def get_data_summary(location, flat_type):
    df = load_data()
    summary = df[(df['town'] == location) & (df['flat_type'] == flat_type)]
    mean_price = summary['resale_price'].mean()
    median_price = summary['resale_price'].median()
    trend = summary.groupby('month')['resale_price'].mean()
    trend_direction = "rising" if trend.iloc[-1] > trend.iloc[0] else "falling"
    
    return f"""
    Historical data summary for {flat_type} flats in {location}:
    - Average resale price: ${mean_price:,.0f}
    - Median resale price: ${median_price:,.0f}
    - Price trend over time: {trend_direction}

    """

def custom_insights_analysis(location, flat_type, user_question):
    data_summary = get_data_summary(location, flat_type)
    prompt = f"""
    You are an expert in Singapore's real estate market, especially HDB resale flats. 
    Below is a summary of historical data for {flat_type} flats in {location}:
    {data_summary}
    
    Based on this data, please answer the following question from a user:
    {user_question}
    
    Make sure your answer is clear, concise, and uses the data summary as context.
    """
    response = llm.get_completion(prompt)
    return response