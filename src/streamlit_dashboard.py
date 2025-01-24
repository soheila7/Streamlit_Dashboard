import streamlit as st
import sys
from pathlib import Path

# Print the current system path for debugging purposes
print(sys.path)

# Add the parent directory of 'src' to sys.path to allow imports from the parent directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import password generator classes from the 'src' module
from src.password_generators import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

# Display the banner image at the top of the page
st.image("/home/seihani_7/my_pytopia/streamlit_example/src/banner.png")

# Set the title of the Streamlit web app
st.title("Password Generator")

# Allow the user to select the type of password generator
option: str = st.radio("select a password generator", ("random password", "memorable password", "pin code"))

# Generate a pin code if 'pin code' is selected
if option == "pin code":
    length: int = st.slider("select the length of the password", 4, 32)
    generator = PinCodeGenerator(length)

# Generate a random password if 'random password' is selected
elif option == "random password":
    length: int = st.slider("select the length of the password", 8, 32)
    include_symbol: bool = st.toggle("Include symbols")
    include_number: bool = st.toggle("Include_numbers")
    generator = RandomPasswordGenerator(length, include_number, include_symbol)     

# Generate a memorable password if 'memorable password' is selected    
elif option == "memorable password":
    num_words: int = st.slider("select the number of worlds", 4, 10)
    separator: str = st.text_input("Separator", value="-")
    capitalization: bool = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(num_words, separator, capitalization)

# Generate and display the password
password: str = generator.generate()
st.write(f"Your password is :  `{password}`")