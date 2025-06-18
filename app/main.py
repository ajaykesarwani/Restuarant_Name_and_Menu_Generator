import streamlit as st
import langchain_helper
st.title("Restaurant Name and Menu Generator")

cuisine = st.text_input("Enter a cuisine (e.g., Italian, Japanese):")

if cuisine:
    try:
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)
        st.subheader("🍽️ Restaurant Name:")
        st.write(response['restaurant_name'])

        st.subheader("📋 Menu Items:")
        st.write(response['menu_items'])
    except Exception as e:
        st.error(f"Something went wrong: {str(e)}")
