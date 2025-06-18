import streamlit as st
from app.langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name and Menu Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Chinese", "Thai","Italian", "Mexican", "American"))

if cuisine:
    try:
        response = generate_restaurant_name_and_items(cuisine)
        st.subheader("🍽️ Restaurant Name:")
        st.write(response['restaurant_name'])

        st.subheader("📋 Menu Items:")
        st.write(response['menu_items'])
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")
