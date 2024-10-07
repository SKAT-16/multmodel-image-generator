# Image Generator AI 🎨

Welcome to the **Image Generator AI**, a web application that allows users to generate images based on text prompts using state-of-the-art models from Hugging Face. This app provides multiple models for image generation and allows users to download the images created.

## 🌐 Live Demo

Check out the deployed version of the app here: [Image Generator AI](https://multimodel-image-gen.streamlit.app/)

## Features

- **Choose a Model**: Select from different Hugging Face models for generating images.
- **Image Generation**: Enter a text prompt and generate images based on your description.
- **Download Image**: Download the generated images in PNG format for easy sharing and use.

## How It Works

1. **Select a model** from the dropdown list.
2. **Describe the image** you want to generate by typing your prompt.
3. Click on the **Generate Image** button to create the image.
4. After the image is generated, you can **download it** using the provided download button.

## Technologies Used

- **Streamlit**: For creating the frontend of the application.
- **Hugging Face API**: For image generation using pre-trained models.
- **Pillow (PIL)**: For image processing tasks.
- **Requests**: For making API calls to the Hugging Face models.
- **dotenv**: For managing environment variables securely.

## Getting Started

### Prerequisites

Make sure you have Python installed. You can install the required dependencies using `pip`:

```bash
pip install streamlit requests python-dotenv pillow
```

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/SKAT-16/multmodel-image-generator
   cd image-gen-ai
   ```

2. Create a `.env` file in the root directory and add your Hugging Face API token:

   ```bash
   HF_TOKEN=your_huggingface_api_token
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Code Overview

The main functionalities of the application include:

- Loading environment variables for API keys.
- Setting up Streamlit with a custom UI.
- Allowing users to select models and input text prompts.
- Processing the image generation requests to the Hugging Face API.
- Displaying the generated images and providing download options.

## License

This project is licensed under the MIT License.

---

Made with ❤️ by NATI | Powered by Hugging Face 🤗
