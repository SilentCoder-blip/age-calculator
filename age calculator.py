import streamlit as st
from datetime import datetime

# Streamlit App Title
st.title("Age Calculator")

# Input: Select birthdate using Streamlit's date input
birthdate = st.date_input("Select your birthdate")

# Calculate age
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Display the result
st.write(f"You are {age} years old!")
