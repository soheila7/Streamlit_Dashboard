import streamlit as st
import pandas as pd
import numpy as np


st.write("Hello World!")

#making a toggle
if st.toggle("on/off"):
    st.write("Hi! I'm ON now!")

"""Soheila
"""
#making a chart
df = pd.DataFrame({"First column": [1,2,3,4], "Second column": [10,20,30,40]})

df

#making a slider
st.slider("SELECT A VALUE", 0, 50)

#making a selectbox
contact_type = st.selectbox("what is your favorite contact type?", ("Email", "Home phone", "Mobile phone")) 


#making a radiobox
contact_type = st.radio("what is your favorite contact type?", ("Email", "Home phone", "Mobile phone")) 

#making a checkbox
if st.checkbox("show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

