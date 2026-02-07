import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key correctly
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="AI Travel Planner")
st.title("🌍 AI Travel Planner")
st.write("Plan your trip using Gemini Generative AI")

destination = st.text_input("Enter destination")
days = st.slider("Number of days", 1, 15, 3)
travel_type = st.selectbox("Travel type", ["Budget", "Standard", "Luxury"])

if st.button("Create Travel Plan"):
    prompt = f"""
    Create a {days}-day travel plan for {destination}.
    Travel type: {travel_type}

    Include:
    - Day-wise itinerary
    - Places to visit
    - Food suggestions
    - Travel tips
    """

    response = model.generate_content(prompt)

    st.subheader("🧭 Your Travel Plan")
    st.write(response.text)

