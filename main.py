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
available_countries = df["Country"].unique()
selected_country = st.selectbox("Choose a country:", available_countries)

# 데이터 필터링
filtered_data = df[df["Country"] == selected_country]

st.subheader(f"MBTI Distribution in {selected_country}")
st.table(filtered_data)

# 사용자 입력을 통한 MBTI 선택
st.subheader("Find the Country with Most Occurrences of Your MBTI")
user_mbti = st.text_input("Enter your MBTI type (e.g., INTJ, ENFP):")

if user_mbti:
    # 해당 MBTI 유형이 나타나는 국가별 분포
    mbti_in_countries = df[df["MBTI"] == user_mbti]["Country"].value_counts()
    
    if not mbti_in_countries.empty:
        # 가장 많은 국가 찾기
        most_common_country = mbti_in_countries.idxmax()
        most_common_count = mbti_in_countries.max()

        st.write(f"The country with the most occurrences of MBTI type {user_mbti} is {most_common_country} with {most_common_count} occurrences.")
    else:
        st.write(f"No data found for the MBTI type {user_mbti}. Please try again.")
