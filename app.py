import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="부쫀쿠 | Bujjonku", page_icon="🍪")

# 헤더 섹션
st.title("🍪 부쫀쿠 (Bujjonku)")
st.subheader("자산은 바삭하게, 인생은 쫀득하게")

st.divider()

# 1. 임시자금 정리 현황
st.header("📉 임시자금 정리 현황")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="보험계약 임시자금", value="275만 원", delta="정리 대기", delta_color="inverse")
with col2:
    st.metric(label="예금담보 임시자금", value="505만 원", delta="정리 대기", delta_color="inverse")

st.info("💡 다음 주 총 780만 원의 임시자금을 정리하여 '부채 제로'를 달성할 예정입니다.")
st.progress(0, text="임시자금 정리 프로세스 0%")

st.divider()

# 2. 부동산 시세 변화 추적
st.header("🏠 부동산 자산 시세 트래커")
st.write("보유 자산의 가치 변화와 남구 중심지 진입을 위한 시세 추적")

# 임시 데이터 (실제 시세로 주기적 업데이트 권장)
property_data = pd.DataFrame({
    "시점": ["24.01", "24.07", "25.01", "25.07", "26.02(현재)"],
    "신천 두산": [3.2, 3.3, 3.25, 3.4, 3.5], 
    "다운 유승": [4.0, 4.1, 4.05, 4.2, 4.4],
    "남구 목표지": [7.0, 7.2, 7.5, 7.8, 8.2]
})

st.line_chart(property_data.set_index("시점"))

col_a, col_b = st.columns(2)
with col_a:
    st.success("✅ **보유 가치 합계:** 약 7.9억")
with col_b:
    st.warning("🎯 **남구 진입 목표:** 약 8.2억~")

st.divider()

# 3. ISA 7:3 포트폴리오 전략
st.header("🎯 자산 베이킹 (ISA)")
chart_data = pd.DataFrame({
    "섹터": ["S&P 500 (핵심)", "AI 전력 인프라", "AI 반도체", "기타"],
    "비중 (%)": [70, 15, 10, 5]
})
st.bar_chart(chart_data.set_index("섹터"))

st.divider()

# 4. ❤️ 우리들의 100일 기록 (Surprise Section)
st.header("💖 Special Moment")

# D-Day 계산
target_date = datetime(2026, 2, 18)
today = datetime.now()
d_day = (target_date - today).days + 1

if d_day > 0:
    st.subheader(f"우리 만난 지 100일까지.. D-{d_day} 🌹")
elif d_day == 0:
    st.subheader("🎉 축하합니다! 오늘이 바로 우리의 100일입니다! 🎉")
else:
    st.subheader(f"우리가 사랑한 지 {abs(d_day) + 100}일째 되는 날")

# 짧은 편지 섹션
with st.expander("💌 사랑하는 너에게 보내는 짧은 편지 (클릭해봐)"):
    st.write("""
    안녕! 우리가 만난 지 벌써 100일이 다 되어가네. 
    
    이 사이트는 우리가 함께할 든든한 미래를 위해 내가 직접 만든 공간이야. 
    자산을 바삭하고 쫀득하게 구워내는 과정처럼, 
    우리의 사랑도 시간이 지날수록 더 달콤하고 단단해졌으면 좋겠어. 
    
    서투른 나를 항상 믿어주고 곁에 있어 줘서 고마워. 
    앞으로 더 행복하게 해줄게. 사랑해! ❤️
    """)

st.divider()

# 부쫀쿠 로그
st.header("📜 부쫀쿠 로그")
st.write("""
- **2026-02-14:** 부동산 트래커 및 100일 기념 섹션 업데이트 완료.
- **Next Plan:** 다음 주 임시자금 완납 후 '부채 제로' 로그 작성 예정.
""")
