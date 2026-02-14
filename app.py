import streamlit as st
import pandas as pd
import numpy as np

# 1. 페이지 설정 및 디자인 커스텀 (CSS 적용)
st.set_page_config(page_title="부쫀쿠 Lab", page_icon="🍪", layout="wide")

st.markdown("""
    <style>
    /* 전체 폰트 크기 및 줄간격 조절 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        font-size: 18px !important; /* 기본보다 폰트를 키웠습니다 */
        line-height: 1.6;
    }
    
    /* 제목 스타일 강조 */
    h1 { color: #2D3436; font-size: 2.8rem !important; font-weight: 800 !important; padding-bottom: 20px; }
    h2 { color: #E67E22; font-size: 2rem !important; margin-top: 30px !important; }
    
    /* 버튼 스타일 (크고 선명하게) */
    .stButton>button {
        width: 100%;
        height: 3.5em;
        border-radius: 15px;
        background-color: #E67E22 !important; /* 쿠키/오렌지색 */
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none;
        box-shadow: 0 4px 15px rgba(230, 126, 34, 0.3);
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #D35400 !important;
        transform: scale(1.02);
        transition: 0.2s;
    }
    
    /* 카드 스타일 레이아웃 */
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 메뉴
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("원하시는 페이지를 선택하세요", ["🏠 자산 대시보드", "⏳ 타임리치 계산기", "📖 자산 성장 전략"])

# 3. 페이지별 내용
if menu == "🏠 자산 대시보드":
    st.title("🍪 부쫀쿠 대시보드")
    st.write("자산은 바삭하게, 인생은 쫀득하게 정리합니다.")
    
    st.divider()
    
    st.subheader("📉 임시자금 정리 현황")
    c1, c2 = st.columns(2)
    with c1: st.metric("보험계약 임시자금", "0 원", "275만 원 정리완료")
    with c2: st.metric("예금담보 임시자금", "0 원", "505만 원 정리완료")
    
    st.success("🎉 총 780만 원의 임시자금 정리가 완료되었습니다. 부채 제로 달성!")
    
    st.divider()
    st.subheader("🏠 부동산 마일스톤")
    st.info("📍 **현재:** 신천 두산(민임), 다운지구 유승\n\n🚩 **중간 단계:** 남구 중심지 확보 및 전향")

elif menu == "⏳ 타임리치 계산기":
    st.title("⏳ 타임리치 시뮬레이터")
    st.write("금융소득이 생활비를 추월하는 시점을 계산합니다.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("현재 나이 (세)", value=30)
            target_income = st.number_input("목표 월 생활비 (만 원)", value=300)
        with col2:
            monthly_invest = st.number_input("월 투자금 (만 원)", value=200)
            exp_return = st.slider("예상 연 수익률 (%)", 1, 15, 10) / 100

    if st.button("내 경제적 자유 시점 분석하기"):
        required_assets = (target_income * 12) / 0.04
        years = 0
        current_val = 10000 
        asset_history = []
        
        while current_val < required_assets and years < 40:
            current_val = (current_val + (monthly_invest * 12)) * (1 + exp_return)
            asset_history.append(int(current_val))
            years += 1
            
        st.divider()
        st.header(f"✨ 분석 결과: {age + years}세에 도달")
        st.write(f"목표 자산 **{required_assets/10000:.1f}억 원**까지 약 **{years}년** 남았습니다.")
        st.line_chart(pd.DataFrame({"예상 자산(만 원)": asset_history}))

elif menu == "📖 자산 성장 전략":
    st.title("📖 자산 성장 전략")
    st.subheader("📈 ISA 7:3 포트폴리오")
    
    chart_data = pd.DataFrame({"섹터": ["S&P 500", "AI 인프라", "AI 반도체", "기타"], "비중 (%)": [70, 15, 10, 5]})
    st.bar_chart(chart_data.set_index("섹터"))
    
    st.markdown("""
    - **핵심 전략:** ISA 계좌를 통한 해외 지수 ETF 비과세 혜택 극대화
    - **실행 방안:** 임시자금 정리로 아낀 이자를 매달 ISA 포트폴리오에 재투자
    """)
