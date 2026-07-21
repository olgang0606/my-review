import streamlit as st

st.set_page_config(page_title="잠실3동 날씨 추천", layout="centered")

st.title("🌧️ 잠실3동 날씨 & 추천")

st.markdown("**2026년 7월 21일 (오늘) & 7월 22일 (내일)**")

# 오늘 날씨
st.subheader("📍 오늘 (7월 21일) 날씨")
st.markdown("""
- **기온**: 24~28°C (체감 28°C)
- **날씨**: 흐리고 비 (호우주의보)
- **강수확률**: 60~80%
- **습도**: 매우 높음 (80~95%)
""")

st.divider()

# 내일 날씨
st.subheader("📍 내일 (7월 22일) 예상 날씨")
st.markdown("""
- **기온**: 24~30°C (체감 높음)
- **날씨**: 흐리고 가끔 비
- **강수확률**: 60~70%
- **특징**: 여전히 습하고 더울 가능성 높음
""")

st.divider()

# 추천 (오늘)
st.subheader("👕 오늘 추천")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**옷차림**")
    st.markdown("- 얇은 긴팔 + 바람막이/우비")
    st.markdown("- 편한 바지")
with col2:
    st.markdown("**준비물**")
    st.markdown("- 우산 (필수)")
    st.markdown("- 여분 양말")

st.markdown("**🍲 음식·음료** : 따뜻한 찌개, 생강차")
st.markdown("**🏃 운동** : 실내 운동 위주")
st.markdown("**💤 수면** : 7.5~8.5시간 충분히")

st.divider()

# 추천 (내일)
st.subheader("👕 내일 추천")
col3, col4 = st.columns(2)
with col3:
    st.markdown("**옷차림**")
    st.markdown("- 반팔 + 얇은 겉옷")
    st.markdown("- 통풍 좋은 옷")
with col4:
    st.markdown("**준비물**")
    st.markdown("- 우산 or 얇은 우비")
    st.markdown("- 선크림 (맑을 때 대비)")

st.markdown("**🍲 음식·음료** : 시원한 국수, 수분 많은 과일, 이온음료")
st.markdown("**🏃 운동** : 오전에 가볍게, 오후 실내")
st.markdown("**💤 수면** : 7~8시간 (더위로 피로 쌓임 주의)")

st.caption("네이버·기상청 기준 • 실시간 변동 가능")
