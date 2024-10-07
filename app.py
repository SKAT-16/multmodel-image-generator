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


st.set_page_config(page_title="Image Generator AI", page_icon="📝", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        color: #4A4A4A;
        font-size: 40px;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 12px;
        color: #A0A0A0;
    }
    .container {
        padding: 20px;
        background-color: #F5F5F5;
        border-radius: 10px;
    }
    .select-box {
        margin-bottom: 20px;
    }
    .text-input {
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit page config
st.markdown(
    "<div class='main-header'>🎨 Image Generator AI 🎨</div>", unsafe_allow_html=True
)

# Centralize the content and add a nice container
with st.container():
    # Select the model from a dropdown
    model_choice = st.selectbox(
        "Choose a model:",
        (
            "black-forest-labs/FLUX.1-dev",
            "glif/how2draw",
            "CompVis/stable-diffusion-v1-4",
        ),
        key="model_choice",
        help="Select one of the Hugging Face models for image generation",
    )

    # Determine the API URL based on the selected model
    if model_choice == "black-forest-labs/FLUX.1-dev":
        api_url = API_URL_1
    elif model_choice == "glif/how2draw":
        api_url = API_URL_2
    else:
        api_url = API_URL_3

    # User input for image generation
    input_text = st.text_input(
        "Describe the image you want to generate:",
        placeholder="e.g., A futuristic city skyline at sunset",
        key="input_text",
        help="Enter a prompt to generate an image based on the model",
    )

    # Button to generate the image
    generate_button = st.button("Generate Image")

    st.markdown("</div>", unsafe_allow_html=True)

# Spinner to show while processing
if generate_button and input_text:
    with st.spinner("Hold on... we are generating your image! 🎨"):
        # Query the model
        image_bytes = query({"inputs": input_text}, api_url)

        try:
            # Display the generated image
            image = Image.open(io.BytesIO(image_bytes))
            st.image(
                image, caption="Here is your generated image!", use_column_width=True
            )

            # Option to download the image
            image_format = "PNG"
            img_buffer = io.BytesIO()
            image.save(img_buffer, format=image_format)

            st.download_button(
                label="Download Image 📥",
                data=img_buffer.getvalue(),
                file_name=f"generated_image.{image_format.lower()}",
                mime=f"image/{image_format.lower()}",
            )

        except Exception as e:
            st.error("Sorry! We couldn't generate the image. Please try again.")
else:
    if generate_button:
        st.error("Please provide a description for the image.")

# Add a footer for some extra visual
st.markdown(
    """
    <div class='footer'>
        Made with ❤️ by NATI | Powered by Hugging Face 🤗
    </div>
    """,
    unsafe_allow_html=True,
)
