
import streamlit as st

st.title("slidebar test")
x = st.slider('x')  # ?? this is a widget
st.write(x, 'au carré est', x * x)