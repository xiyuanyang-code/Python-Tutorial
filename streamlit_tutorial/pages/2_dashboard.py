import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello, this is the dashborad pages!")

st.subheader("Welcome to all of you guys!")

st.text_input("Do you want to learn python?")

date = st.date_input("Input your date!")
st.write(date)
