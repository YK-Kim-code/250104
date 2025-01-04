import streamlit as st
import numpy 
import pandas as pd
import matplotlib.pyplot as plt

st.title("MBTI Distribution by Country")
st.write("데이터 로드 전")
data_path = "countriesMBTI.csv"
df = pd.read_csv(data_path)
st.write(df.head())

st.write("데이터 로드 끝")

# 국가 선택
st.subheader("Select a Country")
available_countries = df["Country"].unique()
selected_country = st.selectbox("Choose a country:", available_countries)

# 데이터 필터링
filtered_data = df[df["Country"] == selected_country]

st.subheader(f"MBTI Distribution in {selected_country}")
st.table(filtered_data)

# MBTI 분포 계산
mbti_counts = filtered_data["MBTI"].value_counts()

# 막대그래프 시각화
st.subheader(f"MBTI Distribution Chart in {selected_country}")
st.bar_chart(mbti_counts)
