import streamlit as st  # Streamlit is a library for building web apps

# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    # Predefined conversion rates
    conversion = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    # Create a key based on user input
    key = f"{unit_from}_{unit_to}"
    
    # Check if the conversion exists
    if key in conversion:
        return value * conversion[key]
    else:
        return None  # No conversion found for the selected units

# ----------------------
# Streamlit UI starts here
# ----------------------

# Title of the app
st.title("Simple Unit Converter")

# User input for value, units to convert from and to
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    # Display result or error message
    if result is not None:
        st.write(f"✅ **Converted value:** {result:.4f} {unit_to}")
    else:
        st.write("❌ **Conversion not supported for the selected units.** Please select valid units.")

