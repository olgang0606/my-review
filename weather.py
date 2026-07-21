import streamlit as st
from datetime import datetime

st.set_page_config(page_title="잠실3동 날씨 추천", layout="centered")

st.title("🌧️ 잠실3동 오늘의 날씨 & 추천")

st.markdown("**2026년 7월 21일 (화)**")

st.subheader("📍 오늘 날씨")
st.markdown("""
- **현재**: 약 25~26°C (체감 28°C), **비** (호우주의보)
- **최저/최고**: 24°C / 28°C
- **강수확률**: 60~80% (하루 종일 비 올 가능성 높음)
- **습도**: 80~95% (매우 습함)
""")

st.divider()

st.subheader("👕 옷차림 & 준비물")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**옷차림**")
    st.markdown("- 얇은 긴팔/반팔 + 바람막이")
    st.markdown("- 편한 바지")
    st.markdown("- 운동화 (미끄럼 주의)")

with col2:
    st.markdown("**준비물**")
    st.markdown("- 우산 (필수)")
    st.markdown("- 여분 양말")
    st.markdown("- 물티슈")

st.divider()

st.subheader("🍲 음식 & 음료")
st.markdown("""
- **추천 음식**: 된장찌개, 김치찌개, 따뜻한 국, 죽
- **추천 음료**: 생강차, 유자차, 따뜻한 물
""")

st.divider()

st.subheader("🏃 운동 & 수면")
st.markdown("""
- **운동**: 실내 운동 추천 (스트레칭, 요가)
- **수면**: 7.5~8.5시간 충분히 취하세요
""")

st.caption("네이버 날씨 기준 • 날씨는 실시간으로 변동될 수 있습니다.")
