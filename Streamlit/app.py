# bmi_app.py

import streamlit as st

# Page Config
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

# Title
st.title("⚖️ BMI Calculator")

st.write("Calculate your Body Mass Index (BMI) easily.")

# User Inputs
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=1.0, step=0.1)

# BMI Calculation
if st.button("Calculate BMI"):

    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    # BMI Category
    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Category: Normal Weight")
    elif 25 <= bmi < 29.9:
        st.info("Category: Overweight")
    else:
        st.error("Category: Obese")

# Footer
st.markdown("---")
st.caption("Built with Streamlit 🚀")