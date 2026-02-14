import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. 페이지 설정 및 디자인
st.set_page_config(page_title="부쫀쿠 Lab", page_icon="🍪", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        font-size: 16px !important;
    }
    h1 { color: #2D3436; font-size: 1.6rem !important; font-weight: 800 !important; white-space: nowrap; padding-bottom: 10px; }
    h2 { color: #E67E22; font-size: 1.4rem !important; margin-top: 20px !important; }
    .stButton>button { width: 100%; height: 3rem; border-radius: 12px; background-color: #E67E22 !important; color: white !important; font-weight: bold !important; border: none; }
    [data-testid="stMetric"] { background-color: #ffffff; padding: 15px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; }
    .stretch-card { background-color: #ffffff; padding: 15px; border-radius: 12px; border-left: 5px solid #E67E22; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 메뉴 (🧘 스트레칭 추가)
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("페이지 이동", ["🏠 자산 대시보드", "⏳ 타임리치 계산기", "📖 매수 가이드", "🧘 스트레칭 가이드"])

# 3. 페이지별 내용
if menu == "🏠 자산 대시보드":
    st.title("🏠 부쫀쿠 대시보드")
    c1, c2 = st.columns(2)
    with c1: st.metric("보험계약 임시자금", "0 원", "완납")
    with c2: st.metric("예금담보 임시자금", "0 원", "완납")
    st.success("🎉 임시자금 정리 완료!")
    st.divider()
    st.subheader("🏠 부동산 마일스톤")
    st.info("📍 현재: 신천 두산, 다운지구 유승 / 🚩 중간: 남구 중심지")

elif menu == "⏳ 타임리치 계산기":
    st.title("⏳ 타임리치 시뮬레이터")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("현재 나이 (세)", value=30)
        target_income = st.number_input("목표 월 생활비 (만 원)", value=300)
    with col2:
        monthly_invest = st.number_input("월 투자금 (만 원)", value=200)
        exp_return = st.slider("예상 연 수익률 (%)", 1, 15, 10) / 100
    if st.button("분석 실행하기"):
        required_assets = (target_income * 12) / 0.04
        years = 0
        current_val = 10000 
        asset_history = []
        while current_val < required_assets and years < 40:
            current_val = (current_val + (monthly_invest * 12)) * (1 + exp_return)
            asset_history.append(int(current_val))
            years += 1
        st.header(f"✨ {age + years}세 도달 예상")
        st.line_chart(pd.DataFrame({"예상 자산(만 원)": asset_history}))

elif menu == "📖 매수 가이드":
    st.title("📖 매수 지시서")
    deposit = st.number_input("이번 달 총 입금액 (만 원)", value=200, step=10)
    c_amt, s_amt = deposit * 0.7, deposit * 0.3
    st.markdown(f"""
    <div class="stretch-card"><b>📦 CORE (70%):</b> {c_amt:,.0f}만 원 (S&P 500)</div>
    <div class="stretch-card" style="border-left-color:#3498DB;"><b>🚀 SATELLITE (30%):</b> {s_amt:,.0f}만 원 (AI 인프라)</div>
    """, unsafe_allow_html=True)

# 🧘 신규 페이지: 스트레칭 가이드
elif menu == "🧘 스트레칭 가이드":
    st.title("🧘 스트레칭 가이드")
    st.write("엔지니어를 위한 3분 핵심 루틴입니다.")

    # 루틴 설명
    st.markdown("""
    <div class="stretch-card">
        <b>1. 거북목 해방 (30초):</b> 턱을 당기고 가슴을 편 상태에서 고개를 뒤로 천천히 젖힙니다.
    </div>
    <div class="stretch-card">
        <b>2. 허리 리셋 (60초):</b> 의자에 앉아 상체를 숙이거나, 서서 손을 허리에 대고 뒤로 젖힙니다.
    </div>
    <div class="stretch-card">
        <b>3. 손목 릴렉스 (30초):</b> 팔을 앞으로 뻗고 손등/손바닥을 몸쪽으로 당깁니다.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # 타이머 기능
    st.subheader("⏱️ 3분 집중 타이머")
    if st.button("스트레칭 시작"):
        placeholder = st.empty()
        for i in range(180, 0, -1):
            mins, secs = divmod(i, 60)
            placeholder.header(f"⏳ 남은 시간: {mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("✅ 스트레칭 완료! 다시 업무에 집중하세요.")
        st.balloons()
