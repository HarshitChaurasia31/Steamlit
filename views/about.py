import streamlit as st
import pandas as pd

st.title("Profile")

col1, col2, col3 = st.columns([1,2,2])

with col1:
    st.image('nissan.jpg', width=150)

with col2:
    st.markdown("## Nissan GT-R")

with col3:
    st.markdown(
        "<div style='font-size:14px;'>"
        "The Nissan GT-R (R35) features a <b>3.8L twin-turbo V6</b>, producing "
        "<b>565–600 HP</b> and accelerating <b>0–60 mph in under 3 seconds</b>.<br><br>"
        "Fuel efficiency: <b>16 MPG city / 23 MPG highway (~8.4–9 km/l)</b>"
        "</div>",
        unsafe_allow_html=True
    )

confusion_matrix = pd.DataFrame(
    {
        "Horsepower(Nm)": ["600 Nm"],
        "Milage(Km/L)": ["9 km/l"],
    },
    index=["Nissan GTR (2020)"],
)

st.markdown("### 📊 Specifications")
st.table(confusion_matrix)