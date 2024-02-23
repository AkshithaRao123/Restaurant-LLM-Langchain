import streamlit as st

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine:", ("Indian", "American", "Italian", "Mexican", "Arabic"))

def generate_rest_name_items(cuisine):
  return {
    'restaurant_name': 'Curry Delight',
    'menu_items': 'samosa, paneer tikka'
  }

if cuisine:
  response = generate_rest_name_items(cuisine)
  st.header(response["restaurant_name"])
  menu_items = response['menu_items'].split(',')
  st.write("--Menu Items--")
  
  for item in menu_items:
    st.write('-', item)
