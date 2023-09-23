from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import streamlit as st

# Function to extract title from a URL
def extract_title(url):
    # Your existing code for extracting the title goes here

# Streamlit UI
st.title("URL Title Extractor")

# Create a sound effect (e.g., a sine wave)
# You can replace this with other sound effects provided by pydub
sound_effect = Sine(440)  # A 440 Hz sine wave (you can change the frequency)

url = st.text_input("Enter URL:")
if st.button("Extract Title"):
    if url:
        st.text("Extracting title...")
        title = extract_title(url)
        st.write(f"Title: {title}")

        # Play the sound effect when extraction is finished
        play(sound_effect)
    else:
        st.warning("Please enter a valid URL.")

# Run the Streamlit app
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.sidebar.title("Options")
    st.sidebar.text("This is a simple URL title extractor.")
    st.sidebar.text("Enter a URL and click 'Extract Title'.")
