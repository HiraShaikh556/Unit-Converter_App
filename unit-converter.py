import streamlit as st 

st.title("🔄 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Unit selection (yeh function ke bahar hona chahiye)
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", [
        "Kilometers to Miles", "Miles to Kilometers", 
        "Meters to Feet", "Feet to Meters"
    ])   
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", [
        "Kilograms to Pounds", "Pounds to Kilograms",
        "Grams to Ounces", "Ounces to Grams"
    ]) 
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", 
        "Hours to Minutes", "Hours to Days", "Days to Hours",
        "Milliseconds to Seconds", "Seconds to Milliseconds"
    ])

# Function to Convert Units
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value / 0.035274

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60 
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24   
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Milliseconds to Seconds":
            return value / 1000
        elif unit == "Seconds to Milliseconds":
            return value * 1000

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"THE RESULT IS {result:.2f}")
