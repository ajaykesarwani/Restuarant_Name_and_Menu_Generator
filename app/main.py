import streamlit as st
import langchain_helper

# Title for the Streamlit App
st.title("🍽️ Restaurant Name Generator")

# Sidebar to select cuisine type
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Chinese", "Thai","Italian", "Mexican", "American"))

# Check if cuisine is selected
if cuisine:
    # Get the response from the langchain_helper function
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # Display the restaurant name (strip spaces/newlines to clean it)
    st.header(response['restaurant_name'].strip())

    # Process menu items: remove extra spaces/newlines, and split by comma
    menu_items = response['menu_items'].replace("\n", "").strip().split(",")

    # Display the menu items as a list
    st.subheader("Menu Items")
    for item in menu_items:
        st.write("-", item.strip())  # Strip each menu item to ensure clean display
