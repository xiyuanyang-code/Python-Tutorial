'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-03-22 09:35:34
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-03-22 10:18:18
FilePath: /streamlit_demo/initial_try.py
Description: 
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved. 
'''
# Initial Try of using streamlit

# Several packages
import streamlit as st
import numpy as np
import pandas as pd

# Drawing thr title
st.title("Just a test for streamlit")

# Drawing the sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Your name")
age = st.sidebar.slider("Your age", 0, 100)

st.write(f"Hello,{user_name}, You are age {age}")

st.header("A data showing")
data = pd.DataFrame(np.random.randn(10, 3),
                    columns = ["A", "B", "C"]
                    )


st.dataframe(data)
st.line_chart(data)
st.bar_chart(data=data)

text1 = st.text_input("Input some text here")
st.write(text1)

text3 = [["Hello"],["How"],["are"],["Ypu"]]
st.write_stream(text3)
text2 = st.text_area("text_area")

st.header("Plot")
st.line_chart(data)

uploaded_file = st.file_uploader("Uploading csv file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded files")
    st.dataframe(df)


st.header("select Box")
st.select_slider("Select",["1","2"])
st.selectbox("select box", ["11", "22", "33"])
data = st.date_input("select date")
st.write(data)


st.link_button("My personal Blog", url="https://xiyuanyang-code.github.io")

st.metric(label="An important label", value=2345.5, delta=-30, delta_color="normal")