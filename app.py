import streamlit as st
import re

# Page setup
st.set_page_config(page_title="Password Checker", page_icon="🔐", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #00FFAA;
        font-size: 38px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #BBBBBB;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🔐 Password Strength Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Live strength detection while typing</div>", unsafe_allow_html=True)

# Strength function
def check_password_strength(password):
    score = 0

    if len(password) >= 6:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=]", password):
        score += 1

    return score

# Input (LIVE)
password = st.text_input("Enter your password", type="password")
st.write("This app checks password strength and helps users create secure passwords.")

# Live update happens automatically
if password:
    score = check_password_strength(password)

    # Progress bar
    percent = int((score / 5) * 100)
    st.progress(percent)

    # Strength label
    if score <= 2:
        st.markdown("<h3 style='color:red;'>🔴 LOW</h3>", unsafe_allow_html=True)
    elif score <= 4:
        st.markdown("<h3 style='color:orange;'>🟡 MEDIUM</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green;'>🟢 STRONG</h3>", unsafe_allow_html=True)

    # Suggestions
    st.subheader("💡 Suggestions")

    if len(password) < 6:
        st.write("❌ Minimum 6 characters required")
    if not re.search("[A-Z]", password):
        st.write("❌ Add uppercase letter")
    if not re.search("[a-z]", password):
        st.write("❌ Add lowercase letter")
    if not re.search("[0-9]", password):
        st.write("❌ Add number")
    if not re.search("[@#$%^&+=]", password):
        st.write("❌ Add special character")

    if score == 5:
        st.success("✅ Strong password!")