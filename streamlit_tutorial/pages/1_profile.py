import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello, this is the profiles page!")

st.subheader("Welcome to all of you guys!")

data = pd.DataFrame(
    np.random.rand(20,3),
    columns=["A", "b", "C"]
)

st.line_chart(data=data)
st.bar_chart(data=data)

