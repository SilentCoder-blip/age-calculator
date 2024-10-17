import streamlit as st
from datetime import date

# Streamlit App Title
st.title("Age Calculator")

# Input: Select birthdate using Streamlit's date input
birthdate = st.date_input("Select your birthdate", min_value=date(1900, 1, 1), max_value=date.today())

# Calculate age
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Display the result
st.write(f"You are {age} years old!")
