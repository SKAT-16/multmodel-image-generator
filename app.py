import requests
import streamlit as st
from dotenv import load_dotenv
import os
import io
from PIL import Image

# Load environment variables
load_dotenv()

# Hugging Face API token
hf_token = os.getenv("HF_TOKEN")

# API URLs for different models
API_URL_1 = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_URL_2 = "https://api-inference.huggingface.co/models/glif/how2draw"
API_URL_3 = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": f"Bearer {hf_token}"}


# Function to query the model
def query(payload, api_url):
    response = requests.post(api_url, headers=headers, json=payload)
    return response.content


# Streamlit page config
st.set_page_config(page_title="Image Generator AI", page_icon="📝", layout="centered")
st.header("Image Generator AI with Hugging Face Models")

# Select the model from a dropdown
model_choice = st.selectbox(
    "Choose a model:",
    ("black-forest-labs/FLUX.1-dev", "glif/how2draw", "CompVis/stable-diffusion-v1-4"),
)

# Determine the API URL based on the selected model
if model_choice == "black-forest-labs/FLUX.1-dev":
    api_url = API_URL_1
elif model_choice == "glif/how2draw":
    api_url = API_URL_2
else:
    api_url = API_URL_3

# User input for image generation
input_text = st.text_input("Input: ", key="input")

# Spinner to show while processing
if st.button("Generate"):
    with st.spinner("Generating image..."):
        # Query the model
        image_bytes = query({"inputs": input_text}, api_url)

        try:
            # Display the generated image
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", width=400)

            # Option to download the image
            image_format = "PNG"
            img_buffer = io.BytesIO()
            image.save(img_buffer, format=image_format)
            st.download_button(
                label="Download Image",
                data=img_buffer.getvalue(),
                file_name=f"generated_image.{image_format.lower()}",
                mime=f"image/{image_format.lower()}",
            )
        except Exception as e:
            st.error("Failed to generate an image. Please try again.")
