import requests
import streamlit as st
from dotenv import load_dotenv
import os
import io
from PIL import Image

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


st.set_page_config(page_title="Image Generator AI", page_icon="📝", layout="centered")
st.header("Image Gen AI with black-forest-labs")

input = st.text_input("Input: ", key="input")
submit = st.button("Image Gen")

if submit:
    image_bytes = query(
        {
            "inputs": input,
        }
    )
    image = Image.open(io.BytesIO(image_bytes))
    st.image(
        image,
        caption="Generated Image",
        width=400,
    )
