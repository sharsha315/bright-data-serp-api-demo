"""
Bright Data SERP API Demo
-------------------------
This Streamlit application demonstrates how to use the Bright Data SERP API to fetch and display Google search results.
Features:
- Enter a search keyword and retrieve results from Google using Bright Data's API
- Handles API authentication via .env file
- Displays raw HTML response from the API

Setup and usage instructions are available in the README.md file.
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Bright Data API key from environment
api_token = os.getenv('BRIGHT_DATA_API_KEY')

# Configure Streamlit page
st.set_page_config(page_title="Bright Data Google Search Demo", page_icon="🔎", layout="centered")
st.title("🔎 Bright Data Google Search Demo")
st.write("Enter a search keyword below. Results will be fetched from Google using Bright Data SERP API.")

# Input box for search keyword
keyword = st.text_input("Search Keyword", "")

# Handle search button click
if st.button("Search"):
    # Check if API key is available
    if not api_token:
        st.error("API key not found. Please set BRIGHT_DATA_API_KEY in your .env file.")
    # Check if keyword is entered
    elif not keyword.strip():
        st.warning("Please enter a search keyword.")
    else:
        # Build Google search URL
        search_url = f"https://www.google.com/search?q={keyword}"
        # Prepare Bright Data API request payload
        data = {
            "zone": "serp_api_demo1",  # Replace with your actual zone name
            "url": search_url,
            "format": "json"  # Response format: 'json', 'html', or 'markdown'
        }
        # Set request headers
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        # Show spinner while fetching results
        with st.spinner("Searching Google..."):
            try:
                # Send POST request to Bright Data SERP API
                response = requests.post(
                    "https://api.brightdata.com/request",
                    json=data,
                    headers=headers,
                    timeout=30
                )
                # Raise exception for HTTP errors
                response.raise_for_status()
                # Display success message and results
                st.success("Results fetched successfully!")
                st.subheader("Raw HTML Response:")
                # Show first 5000 characters of response
                st.code(response.text[:5000], language="html")
            except Exception as e:
                # Display error message if request fails
                st.error(f"Error fetching results: {e}")