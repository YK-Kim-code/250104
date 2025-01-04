import streamlit as st
import numpy 
import pandas as pd
st.title("MBTI Distribution by Country")
st.write("데이터 로드 전")
data_path = "countriesMBTI.csv"
df = pd.read_csv(data_path)
st.write(df.head())

st.write("데이터 로드 끝")

# 국가 선택
st.subheader("Select a Country")
available_countries = df["country"].unique()
selected_country = st.selectbox("Choose a country:", available_countries)

# 데이터 필터링
filtered_data = df[df["country"] == selected_country]

# MBTI 분포 계산
mbti_distribution = filtered_data["mbti"].value_counts().reset_index()
mbti_distribution.columns = ["MBTI Type", "Count"]

# 결과 표시
st.subheader(f"MBTI Distribution in {selected_country}")
st.table(mbti_distribution)
