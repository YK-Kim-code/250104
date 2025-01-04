import streamlit as st
from transformers import pipeline  # 또는 다른 감정 분석 라이브러리

# 모델 로드
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis")

sentiment_model = load_sentiment_model()

# 제목
st.title("감정 분석 웹사이트")
st.subheader("입력한 텍스트에 기반하여 현재 감정을 분석합니다.")

# 사용자 입력
user_input = st.text_area("현재 상태를 간단히 입력하세요:", "")

# 감정 분석 결과
if user_input:
    with st.spinner("감정 분석 중..."):
        result = sentiment_model(user_input)
        sentiment = result[0]['label']
        score = result[0]['score']
        st.success(f"분석 결과: **{sentiment}** (신뢰도: {score:.2f})")
