import streamlit as st
import pandas as pd
import numpy as np

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
    /* 가이드 카드 스타일 */
    .guide-card { background-color: #F8F9FA; padding: 20px; border-radius: 15px; border-left: 5px solid #E67E22; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 메뉴
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("페이지 이동", ["🏠 자산 대시보드", "⏳ 타임리치 계산기", "📖 매수 가이드"])

# 3. 페이지별 내용
if menu == "🏠 자산 대시보드":
    st.title("🏠 부쫀쿠 대시보드")
    st.subheader("📉 임시자금 정리 현황")
    c1, c2 = st.columns(2)
    with c1: st.metric("보험계약 임시자금", "0 원", "275만 완납")
    with c2: st.metric("예금담보 임시자금", "0 원", "505만 완납")
    st.success("🎉 총 780만 원의 임시자금 정리가 완료되었습니다.")
    st.divider()
    st.subheader("🏠 부동산 마일스톤")
    st.info("📍 **현재:** 신천 두산, 다운지구 유승\n\n🚩 **중간:** 남구 중심지 확보")

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
        st.divider()
        st.header(f"✨ {age + years}세에 도달 예상")
        st.line_chart(pd.DataFrame({"예상 자산(만 원)": asset_history}))

elif menu == "📖 매수 가이드":
    st.title("📖 기계적 매수 가이드")
    st.write("ISA 계좌 7:3 전략에 따른 이번 달 매수 금액입니다.")
    
    # 입력 섹션
    deposit = st.number_input("이번 달 총 입금액 (만 원)", value=200, step=10)
    
    st.divider()
    
    # 계산 로직
    core_amt = deposit * 0.7
    sat_amt = deposit * 0.3
    
    st.subheader("🛠️ 종목별 매수 지시서")
    
    # 카드 형태로 가독성 높게 표시
    st.markdown(f"""
    <div class="guide-card">
        <h4 style="margin:0; color:#2D3436;">📦 CORE (70%)</h4>
        <p style="font-size: 1.2rem; font-weight: bold; color: #E67E22; margin: 10px 0;">S&P 500 지수 추종 ETF</p>
        <p style="margin:0;">매수 금액: <span style="font-size: 1.5rem;">{core_amt:,.0f}만 원</span></p>
    </div>
    <div class="guide-card" style="border-left-color: #3498DB;">
        <h4 style="margin:0; color:#2D3436;">🚀 SATELLITE (30%)</h4>
        <p style="font-size: 1.2rem; font-weight: bold; color: #3498DB; margin: 10px 0;">AI 인프라 및 반도체 ETF</p>
        <p style="margin:0;">매수 금액: <span style="font-size: 1.5rem;">{sat_amt:,.0f}만 원</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **실행 요령:** 주가에 상관없이 정해진 날짜에 위 금액만큼 기계적으로 시장가 매수합니다.")
