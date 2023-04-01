from API_Data import get_api_data, get_image
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Astronomy Image of the Day",
                   page_icon="assets/universe.ico",
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

data = get_api_data()
data_img = get_image()

title = data["title"]
image = Image.open("assets/images/image.jpg")
content = data["explanation"]

st.title(title)
st.image(image)
st.info(content, icon="💡")