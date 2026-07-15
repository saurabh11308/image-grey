import streamlit as st
from PIL import Image

camera_img = st.camera_input(label="Take Photo")

if camera_img:
    img = Image.open(camera_img)
    grey_img = img.convert('L')
    st.image(grey_img)