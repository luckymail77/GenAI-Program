import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")
st.write("You can add more components here, such as charts, images, and interactive widgets.")
st.write("For example, you can create a slider:")
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"You selected: {slider_value}")
st.write("You can also create a text input:")
text_input = st.text_input("Enter some text")
st.write(f"You entered: {text_input}")
st.write("Feel free to explore Streamlit's documentation for more features and customization options!")
    
if st.button("Click Me")
:
    st.write("Button clicked!") 
