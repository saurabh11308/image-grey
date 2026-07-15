import streamlit as st
from PIL import Image

camera_img = st.camera_input(label="Take Photo")

if camera_img:
    #Create a Pillow image instance
    img = Image.open(camera_img)
    #convert the pillow image instance to grey scale
    grey_img = img.convert('L')
    #render the image to browser
    st.image(grey_img)