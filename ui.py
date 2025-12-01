import streamlit as st
import requests
from PIL import Image
import io

# Setup the UI
st.title("🖼️ AI Background Remover")
st.write("Upload an image to remove the background using our API.")

# API URL (Note: 'backend' is the service name we will define in Docker Compose)
API_URL = "http://backend:8000/remove"

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            try:
                # Prepare the file for the API
                files = {"file": uploaded_file.getvalue()}
                
                # Send request to FastAPI
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    # Convert bytes back to image
                    result_image = Image.open(io.BytesIO(response.content))
                    st.success("Background Removed!")
                    st.image(result_image, caption="Result", use_container_width=True)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
                st.info("Make sure the backend is running!")
