import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="부쫀쿠 | Bujjonku", page_icon="🍪")

# 헤더 섹션
st.title("🍪 부쫀쿠 (Bujjonku)")
st.subheader("자산은 바삭하게, 인생은 쫀득하게")

st.divider()

# 1. 임시자금(Temporary Fund) 정리 결과
st.header("✅ 임시자금 정리 완료")
col1, col2 = st.columns(2)

# 정리 완료 상태로 업데이트
with col1:
    st.metric(label="보험계약 임시자금", value="0 원", delta="275만 원 정리 완료", delta_color="normal")
with col2:
    st.metric(label="예금담보 임시자금", value="0 원", delta="505만 원 정리 완료", delta_color="normal")

st.balloons() # 접속 시 축하 풍선 효과
st.success("🎉 총 780만 원의 임시자금 정리가 완료되었습니다. 이제 모든 자산은 성장을 위해서만 움직입니다.")
st.progress(100, text="임시자금 제로(Zero) 달성 완료")

st.divider()

# 2. [신규] 이자→투자 전환 시뮬레이터
st.header("💸 이자 세이브 & 투자 가속")
st.write("정리된 임시자금의 이자가 매달 투자금에 더해졌을 때의 효과입니다.")

# 이자율 가정 (평균 5.5% 가정)
avg_interest_rate = 0.055
monthly_saved_interest = int((7800000 * avg_interest_rate) / 12)

col_int1, col_int2 = st.columns(2)
with col_int1:
    st.info(f"✨ 매달 아낀 이자: **약 {monthly_saved_interest:,}원**")
with col_int2:
    st.info(f"🚀 10년 뒤 추가 자산: **약 {int(monthly_saved_interest * 12 * 10 * 1.6):,}원**") # 복리 효과 약식 계산

st.caption("※ 아낀 이자가 연 10% 수익률의 ISA 포트폴리오로 재투자된다고 가정했습니다.")

st.divider()

# 3. 자산 성장 전략 (ISA 중심)
st.header("🎯 자산 성장 전략 (ISA)")
st.write("📈 **ISA 적립식:** S&P 500(70%) + AI 인프라/반도체(30%)")

chart_data = pd.DataFrame({
    "섹터": ["S&P 500 (핵심)", "AI 전력 인프라", "AI 반도체", "기타"],
    "비중 (%)": [70, 15, 10, 5]
})
st.bar_chart(chart_data.set_index("섹터"))

st.divider()

# 4. 부동산 여정 (중간 마일스톤)
st.header("🏠 부동산 포트폴리오 로드맵")
col_prop1, col_prop2 = st.columns(2)
with col_prop1:
    st.write("📍 **현재 운영**\n- 신천 두산\n- 다운지구 유승")
with col_prop2:
    st.write("🚩 **중간 마일스톤**\n- 집단 임시자금 실행\n- 남구 중심지 전향")

st.divider()

# 5. ❤️ 우리들의 100일 기록
st.header("💖 Special Moment")
target_date = datetime(2026, 2, 18)
today = datetime.now()
d_day = (target_date - today).days + 1

if d_day > 0:
    st.subheader(f"우리 만난 지 100일까지.. D-{d_day} 🌹")
else:
    st.subheader("🎉 100일 축하합니다! 🎉")

with st.expander("💌 사랑하는 너에게 보내는 짧은 편지 (클릭)"):
    st.write("우리가 함께할 든든한 미래를 위해 내가 직접 만든 공간이야. 사랑해! ❤️")

st.divider()

# 부쫀쿠 로그
st.header("📜 부쫀쿠 로그")
st.write("""
- **2026-02-14:** 임시자금 780만 원 전액 정리 완료 기록.
- **2026-02-14:** 아낀 이자 재투자 시뮬레이션 기능 추가.
- **Next Task:** 2월 말 부동산 관련 신규 임시자금 실행 준비 및 신용 관리.
""")
