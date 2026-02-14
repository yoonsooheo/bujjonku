import streamlit as st
import pandas as pd
import numpy as np

# 1. 페이지 설정 및 디자인 커스텀 (CSS 수정)
st.set_page_config(page_title="부쫀쿠 Lab", page_icon="🍪", layout="wide")

st.markdown("""
    <style>
    /* 전체 폰트 및 가독성 설정 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        font-size: 16px !important; 
        line-height: 1.5;
    }
    
    /* 제목(h1) 크기 조정: 한 줄에 들어오도록 크기를 줄이고 줄바꿈 방지 */
    h1 { 
        color: #2D3436; 
        font-size: 1.6rem !important; /* 크기를 기존 2.8rem에서 1.6rem으로 축소 */
        font-weight: 800 !important; 
        white-space: nowrap; /* 절대 줄바꿈 하지 않음 */
        overflow: hidden;
        text-overflow: ellipsis; /* 혹시 넘치면 ... 처리 */
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    /* 서브제목(h2) 스타일 */
    h2 { color: #E67E22; font-size: 1.4rem !important; margin-top: 20px !important; }
    
    /* 버튼 스타일 (쿠키색 강조) */
    .stButton>button {
        width: 100%;
        height: 3rem;
        border-radius: 12px;
        background-color: #E67E22 !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        border: none;
        margin-top: 5px;
    }
    
    /* 지표(Metric) 카드 스타일 */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 메뉴
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("페이지 이동", ["🏠 자산 대시보드", "⏳ 타임리치 계산기", "📖 자산 성장 전략"])

# 3. 페이지별 내용
if menu == "🏠 자산 대시보드":
    st.title("🏠 부쫀쿠 대시보드") # 제목을 짧고 명확하게 수정
    
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
    
    with st.container():
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

elif menu == "📖 자산 성장 전략":
    st.title("📖 자산 성장 전략")
    
    chart_data = pd.DataFrame({"섹터": ["S&P 500", "AI 인프라", "AI 반도체", "기타"], "비중 (%)": [70, 15, 10, 5]})
    st.bar_chart(chart_data.set_index("섹터"))
    
    st.markdown("""
    - **핵심:** ISA 계좌 비과세 혜택 극대화
    - **실행:** 아낀 이자를 ISA 포트폴리오에 재투자
    """)
