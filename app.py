import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    if len(password) < 6:
        return "LOW", "red"

    if (re.search("[a-z]", password) and 
        re.search("[A-Z]", password) and 
        re.search("[0-9]", password) and 
        re.search("[@#$%^&+=]", password)):
        return "STRONG", "green"

    if (re.search("[a-zA-Z]", password) and 
        re.search("[0-9]", password)):
        return "MEDIUM", "orange"

    return "LOW", "red"


# UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    strength, color = check_password_strength(password)

    st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)

    # Suggestions
    st.subheader("Suggestions:")
    if len(password) < 6:
        st.write("❌ Increase length (min 6 characters)")
    if not re.search("[A-Z]", password):
        st.write("❌ Add uppercase letter")
    if not re.search("[a-z]", password):
        st.write("❌ Add lowercase letter")
    if not re.search("[0-9]", password):
        st.write("❌ Add number")
    if not re.search("[@#$%^&+=]", password):
        st.write("❌ Add special character")