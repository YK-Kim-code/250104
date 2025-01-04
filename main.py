import streamlit as st
import numpy 
import pandas as pd
st.write("데이터 로드 전")
data_path = "countriesMBTI.csv"
df = pd.read_csv(data_path)
st.write(df.head())

st.write("데이터 로드 끝")
