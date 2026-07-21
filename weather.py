import streamlit as st
from datetime import datetime

st.set_page_config(page_title="잠실3동 날씨 & 추천", layout="centered")
st.title("🌧️ 잠실3동 오늘의 날씨 & 추천")

st.markdown("**2026년 7월 21일 (화)**")

# 오늘 날씨 (네이버 기준 실시간 정보 반영)
st.subheader("📍 오늘 날씨")
st.markdown("""
- **현재**: 약 25~26°C (체감 28°C), **비** (호우주의보)
- **최저/최고**: 24°C / 28°C
- **강수확률**: 60~80% (비가 하루 종일 올 가능성 높음)
- **습도**: 80~95% (매우 습함)
- **특징**: 흐리고 비/가끔 강한 비, 바람 약함
""")

st.divider()

st.subheader("👕 옷차림 & 준비물 추천")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**옷차림**")
    st.markdown("- 얇은 긴팔/반팔 + 바람막이 or 얇은 우비")
    st.markdown("- 편한 바지 (청바지/트레이닝)")
    st.markdown("- 운동화 (미끄럼 주의)")

with col2:
    st.markdown("**준비물**")
    st.markdown("- 우산 (필수!) or 접이식 우비")
    st.markdown("- 여분 양말/속옷")
    st.markdown("- 물티슈, 마스크")
    st.markdown("- 장화나 방수 신발 (강수량 많을 시)")

st.divider()

st.subheader("🍲**✅ 1. Streamlit Cloud에서 작동하는 복사-붙여넣기 가능한 코드**

아래 코드를 **app.py** 파일로 저장하세요. GitHub에 업로드한 후 Streamlit Cloud에서 쉽게 배포할 수 있습니다. (requirements.txt도 필요)

### app.py
```python
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="잠실3동 날씨 & 추천", layout="centered")
st.title("🌧️ 잠실3동 오늘의 날씨 & 추천")

st.markdown("**2026년 7월 21일 (화)**")

# 오늘 날씨 (네이버 기준 실시간 정보 반영)
st.subheader("📍 오늘 날씨")
st.markdown("""
- **현재**: 약 25~26°C (체감 28°C), **비** (호우주의보)
- **최저/최고**: 24°C / 28°C
- **강수확률**: 60~80% (비가 하루 종일 올 가능성 높음)
- **습도**: 80~95% (매우 습함)
- **특징**: 흐리고 비/가끔 강한 비, 바람 약함
""")

st.divider()

st.subheader("👕 옷차림 & 준비물 추천")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**옷차림**")
    st.markdown("- 얇은 긴팔/반팔 + 바람막이 or 얇은 우비")
    st.markdown("- 편한 바지 (청바지/트레이닝)")
    st.markdown("- 운동화 (미끄럼 주의)")

with col2:
    st.markdown("**준비물**")
    st.markdown("- 우산 (필수!) or 접이식 우비")
    st.markdown("- 여분 양말/속옷")
    st.markdown("- 물티슈, 마스크")
    st.markdown("- 장화나 방수 신발 (강수량 많을 시)")

st.divider()

st.subheader("🍲 음식 & 음료 추천")
st.markdown("""
- **음식**: 따뜻한 국/찌개 (된장찌개, 김치찌개, 해장국), 죽, 따뜻한 면류
- **음료**: 따뜻한 차 (생강차, 유자차), 따뜻한 커피/라떼, 물 많이 마시기
- **피할 것**: 차가운 음료/아이스크림 (감기 주의)
""")

st.divider()

st.subheader("🏃 운동 & 수면 추천")
st.markdown("""
- **운동**: 실내 운동 추천 (집에서 스트레칭, 요가, 실내 자전거). 외출 시 가벼운 산책만.
- **수면시간**: 평소보다 **7.5~8.5시간** 충분히 취하세요. 습하고 비 오는 날은 피로가 쌓이기 쉽습니다.
""")
