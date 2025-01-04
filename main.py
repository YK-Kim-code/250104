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

# 막대그래프 시각화
st.subheader(f"MBTI Distribution Chart in {selected_country}")
fig, ax = plt.subplots(figsize=(8, 5))
mbti_counts.plot(kind="bar", ax=ax, color="skyblue")
ax.set_title(f"MBTI Distribution in {selected_country}")
ax.set_xlabel("MBTI Type")
ax.set_ylabel("Count")
st.pyplot(fig)
