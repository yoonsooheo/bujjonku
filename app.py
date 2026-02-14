import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="부쫀쿠 | Bujjonku Lab", page_icon="🍪", layout="wide")

# 사이드바 메뉴
st.sidebar.title("🍪 부쫀쿠 메뉴")
menu = st.sidebar.radio("이동할 페이지", ["대시보드", "타임리치 계산기", "절세/연금 가이드"])

# --- 1. 대시보드 (기존 기능 유지 및 강화) ---
if menu == "대시보드":
    st.title("🍪 부쫀쿠 자산 대시보드")
    st.subheader("자산은 바삭하게, 인생은 쫀득하게")
    
    st.divider()
    
    # 임시자금 현황
    st.header("✅ 임시자금 정리 완료")
    c1, c2 = st.columns(2)
    with c1: st.metric("보험계약 임시자금", "0 원", "275만 원 정리 완료")
    with c2: st.metric("예금담보 임시자금", "0 원", "505만 원 정리 완료")
    
    st.divider()
    
    # 전략 및 로드맵
    col_a, col_b = st.columns(2)
    with col_a:
        st.header("🎯 ISA 7:3 전략")
        chart_data = pd.DataFrame({"섹터": ["S&P 500", "AI 인프라", "AI 반도체", "기타"], "비중 (%)": [70, 15, 10, 5]})
        st.bar_chart(chart_data.set_index("섹터"))
    with col_b:
        st.header("🏠 부동산 마일스톤")
        st.info("📍 현재: 신천 두산, 다운지구 유승\n\n🚩 중간 목표: 남구 중심지 전향")

# --- 2. 타임리치 계산기 (Timerichlab 스타일 구현) ---
elif menu == "타임리치 계산기":
    st.title("⏳ 타임리치(Time-Rich) 계산기")
    st.write("나의 금융소득이 생활비를 추월하는 '경제적 자유' 시점을 계산합니다.")
    
    with st.form("calculator_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("현재 나이", value=30)
            target_income = st.number_input("목표 월 생활비 (만 원)", value=300)
            net_assets = st.number_input("현재 순자산 (만 원)", value=10000)
        with col2:
            monthly_invest = st.number_input("월 투자금 (만 원)", value=200)
            exp_return = st.slider("예상 연 수익률 (%)", 1.0, 15.0, 10.0) / 100
            withdrawal_rate = st.slider("은퇴 후 인출률 (4% 법칙 권장) (%)", 1.0, 5.0, 4.0) / 100

        submit = st.form_submit_button("경제적 자유 시점 계산하기")

    if submit:
        # 은퇴에 필요한 총 자산 = 월 생활비 * 12 / 인출률
        required_assets = (target_income * 12) / withdrawal_rate
        
        # 미래 가치 계산 로직
        current_val = net_assets
        years = 0
        asset_history = [current_val]
        
        while current_val < required_assets and years < 50:
            current_val = (current_assets := (current_val + (monthly_invest * 12)) * (1 + exp_return))
            asset_history.append(int(current_assets))
            years += 1
            
        st.divider()
        st.header(f"✨ 결과: {age + years}세에 경제적 자유 달성")
        st.success(f"목표 자산 {required_assets/10000:.1f}억 원 도달까지 약 {years}년 남았습니다.")
        
        # 차트 시각화
        chart_df = pd.DataFrame({"예상 자산": asset_history})
        st.line_chart(chart_df)
        
        st.info(f"💡 월 {monthly_invest}만 원을 {exp_return*100}% 수익률로 투자할 때의 시나리오입니다.")

# --- 3. 절세/연금 가이드 (Info 탭 분석 내용 반영) ---
elif menu == "절세/연금 가이드":
    st.title("📖 부쫀쿠 절세 & 연금 가이드")
    st.write("Timerichlab 분석 기반, 엔지니어님께 최적화된 절세 전략입니다.")
    
    st.markdown("""
    ### 1. ISA (개인종합자산관리계좌) - **현재 주력**
    - **전략:** 비과세 한도 1,000만 원(서민형) 활용.
    - **핵심:** 해외 지수 추종 ETF(S&P 500 등)를 국내 상장 버전으로 매수하여 배당소득세 절감.
    
    ### 2. 연금저축 & IRP - **추후 확장**
    - **참고:** 현재 세액공제 혜택이 적으므로, 납입 한도를 조절하며 노후 준비 자금으로 운용.
    - **장점:** 과세 이연 및 저율 과세(3.3~5.5%) 효과.
    
    ### 3. 임시자금 정리의 효과
    - 780만 원 마더론 정리는 단순히 부채를 없애는 것이 아니라, **확정 수익률(대출 이자율만큼)을 확보**하는 가장 안전한 투자입니다.
    """)
