import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="부쫀쿠 Lab", page_icon="🍪", layout="wide")

# 사이드바: Timerichlab 스타일의 메뉴 구성
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("분석 도구", ["🏠 자산 대시보드", "⏳ 타임리치 계산기", "📖 절세/연금 전략"])

# 1. 자산 대시보드 (실행 결과 중심)
if menu == "🏠 자산 대시보드":
    st.title("🍪 부쫀쿠 자산 대시보드")
    st.subheader("자산은 바삭하게, 인생은 쫀득하게")
    
    st.divider()
    
    # 임시자금 정리 상태 (Update: 완료)
    st.header("✅ 임시자금 정리 완료")
    c1, c2 = st.columns(2)
    with c1: st.metric("보험계약 임시자금", "0 원", "275만 원 완납")
    with c2: st.metric("예금담보 임시자금", "0 원", "505만 원 완납")
    
    st.success("🎉 총 780만 원의 임시자금 정리가 완료되었습니다. 부채 제로 달성!")
    
    st.divider()
    
    # 부동산 마일스톤 (중간 단계 정의)
    st.header("🏠 부동산 마일스톤")
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("📍 **현재 운영**\n\n- 신천 두산 (민임)\n- 다운지구 유승")
    with col_b:
        st.success("🚩 **중간 마일스톤**\n\n- 집단 임시자금 실행\n- 남구 중심지 전향")

# 2. 타임리치 계산기 (핵심 분석 도구)
elif menu == "⏳ 타임리치 계산기":
    st.title("⏳ 타임리치(Time-Rich) 시뮬레이터")
    st.write("Timerichlab 분석 로직을 적용한 경제적 자유 도달 시점 계산기입니다.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("현재 나이", value=30)
            target_income = st.number_input("목표 월 생활비 (만 원)", value=300)
        with col2:
            monthly_invest = st.number_input("월 투자금 (만 원)", value=200)
            exp_return = st.slider("예상 연 수익률 (%)", 1, 15, 10) / 100

    # 경제적 자유 자산 계산 (4% 법칙 적용)
    # 목표 자산 = (월 생활비 * 12) / 0.04
    required_assets = (target_income * 12) / 0.04
    
    # 시뮬레이션
    years = 0
    current_val = 10000 # 현재 가용 자산 가정
    asset_history = []
    
    while current_val < required_assets and years < 40:
        current_val = (current_val + (monthly_invest * 12)) * (1 + exp_return)
        asset_history.append(int(current_val))
        years += 1
        
    st.divider()
    st.header(f"✨ 분석 결과: {age + years}세에 경제적 자유 달성")
    st.metric("목표 자산", f"{required_assets/10000:.1f}억 원")
    
    # 자산 성장 차트
    st.line_chart(pd.DataFrame({"예상 자산(만 원)": asset_history}))

# 3. 절세/연금 전략 (Timerichlab Info 탭 분석)
elif menu == "📖 절세/연금 전략":
    st.title("📖 절세 & 연금 최적화")
    st.markdown("""
    - **ISA 전략:** 비과세 혜택을 극대화하여 S&P 500 등 해외 지수 기반 투자 가속.
    - **임시자금 관리:** 불필요한 이자 지출을 막아 월 투자 원금을 높이는 것이 최고의 절세.
    - **연금 전환:** 10억 목표 달성 후 인출 단계에서 저율 과세를 위한 IRP 활용 검토.
    """)
