import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 기본 설정
st.set_page_config(page_title="일로온나 Job-On-Na", page_icon="🌊", layout="wide")

# 타이틀 및 소개
st.title("🌊 일로온나 Job-On-Na 🌊")
st.markdown(" *•*¨*•.¸¸여러분의 전공, 성향에 맞춘 기업을 알려주고 취준 로드맵을 제공합니다¸¸.•*¨*•* ")

# 사이드바 메뉴 구성
st.sidebar.header("ʕ •̀ᴥ•́ ʔ  메뉴 ")
menu = st.sidebar.radio("이동할 페이지를 선택하세요:", 
                        ("1. 프로필 & 번아웃 진단", "2. 부울경 맞춤 일자리 매칭", "3. To-Do & 지원 정책"))

# --------------------------------------------------------------------------------
# 1. 프로필 & 번아웃 진단 페이지
# --------------------------------------------------------------------------------
if menu == "1. 프로필 & 번아웃 진단":
    st.header("✧ 나의 상태와 목표 설정하기 ✧")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧾기본 스펙 입력")
        major = st.text_input("전공을 입력해주세요 (예: 컴퓨터공학, 경영학)")
        skills = st.text_input("보유 기술 및 자격증 (쉼표로 구분)")
        lifestyle = st.selectbox("가장 중요하게 생각하는 가치는?", ["워라밸(저녁이 있는 삶)", "높은 연봉", "직무 전문성 성장", "안정성"])
    
    with col2:
        st.subheader("🔥번아웃 자가 진단🔥")
        st.markdown("최근 1주일간의 상태를 체크해주세요.")
        q1 = st.slider("아침에 일어날 때 출근/취업준비 할 생각에 피곤함을 느낀다.", 1, 5, 3)
        q2 = st.slider("하루 일과가 끝나면 완전히 지쳐버린다.", 1, 5, 3)
        q3 = st.slider("취업에 대한 자신감이 떨어지고 우울감이 든다.", 1, 5, 3)
        
        burnout_score = q1 + q2 + q3
    
    if st.button("진단 및 프로필 저장"):
        st.success("데이터가 저장되었습니다! 다음 탭으로 이동해보세요.")
        
        # 번아웃 시각화 (Plotly 게이지 차트)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = burnout_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "나의 번아웃 지수"},
            gauge = {'axis': {'range': [None, 15]},
                     'bar': {'color': "darkblue"},
                     'steps' : [
                         {'range': [0, 5], 'color': "lightgreen"},
                         {'range': [5, 10], 'color': "yellow"},
                         {'range': [10, 15], 'color': "red"}]}
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        if burnout_score >= 10:
            st.error("🚨 번아웃 위험 단계입니다! 무리한 취업 준비보다 잠시 휴식이 필요합니다.")
            st.info("💡 추천 케어 방안: 부산시 청년 마음건강 지원사업 신청하기, 동네 산책하기")

# --------------------------------------------------------------------------------
# 2. 부울경 맞춤 일자리 매칭 페이지
# --------------------------------------------------------------------------------
elif menu == "2. 부울경 맞춤 일자리 매칭":
    st.header("⚡내 스펙에 딱 맞는 부울경 유망 기업⚡")
    st.markdown("단순한 일자리 추천을 넘어, **직주근접 주거지**와 낯선 지역과 친해지는 **면접 투어**까지 한 번에 제안합니다.")
    
    # 1. 일자리 추천 리스트 (임시 데이터)
    dummy_jobs = pd.DataFrame({
        "기업명": ["(주)부산데이터테크", "울산스마트에너지", "경남AI솔루션즈"],
        "직무": ["데이터 분석가", "시스템 엔지니어", "AI 모델러"],
        "위치": ["부산 해운대구", "울산 남구", "경남 창원시"],
        "예상연봉": ["3,200만원", "3,500만원", "3,400만원"],
        "매칭률": ["95%", "88%", "82%"]
    })
    
    st.dataframe(dummy_jobs, use_container_width=True)
    st.markdown("---")
    
    # 2. 기업 상세 정보 및 정착 가이드 (선택형 UI)
    st.subheader("🏢 관심 기업 정착 가이드 보기")
    selected_company = st.selectbox("정착 가이드를 확인할 기업을 선택하세요:", dummy_jobs["기업명"])
    
    # 선택된 기업의 위치 정보 가져오기
    job_location = dummy_jobs[dummy_jobs["기업명"] == selected_company].iloc[0]["위치"]
    
    # 탭으로 주거지와 면접 투어 정보 나누기
    tab1, tab2 = st.tabs(["🏠 1. 기업 근접 주거지 매칭", "🎒 2. 부울경 면접 투어 패키지"])
    
    with tab1:
        st.markdown(f"### {selected_company} 인근 청년 특화 주거 정보")
        st.info('💡 **출퇴근 시뮬레이션:** "회사까지 버스로 15분, 자취방 월세 평균 40만 원" \n\n (청년 주택 입주 시 실질 주거비가 대폭 감소하여 실질 연봉이 상승합니다!)')
        
        if "부산" in job_location:
            st.write("취업해도 집값 때문에 망설이셨나요? 부산시가 지원하는 청년 임대주택 리스트를 확인하고 직주근접 라이프를 실현해 보세요.")
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                st.link_button("👉 부산 청년주거정책 확인하기", "https://www.busan.go.kr/housing/ko/pages/youth_rental.php", use_container_width=True)
            with col_btn2:
                st.link_button("👉 희망더함주택 알아보기", "https://www.busan.go.kr/depart/dreamhouse", use_container_width=True)
        else:
            st.write(f"현재 선택하신 **{job_location}** 지역의 청년 주택 정보 및 전월세 보증금 지원 정책을 불러오는 중입니다.")
            st.button(f"{job_location.split()[0]} 청년 주거 정책 검색하기")

    with tab2:
        st.markdown("### 낯선 동네와 친해지는 [1박 2일 면접 투어]")
        st.markdown("타 지역 취업의 가장 큰 벽은 '그 동네를 모른다'는 두려움입니다. 면접 보러 가는 날, 지원 지역을 미리 경험해 볼 수 있는 특별한 투어 코스를 제안합니다.")
        
        # 면접 투어 일정표 데이터
        tour_plan = pd.DataFrame({
            "구분": ["1일차", "1일차", "1일차", "2일차", "2일차", "2일차", "2일차"],
            "시간": ["14:00 - 15:00", "16:00 - 17:00", "17:00 - 19:00", "10:00 - 12:00", "12:00 - 13:30", "14:00 - 16:00", "17:00"],
            "활동 내용": [
                "🧳 면접 스테이 체크인 (부산 청년 게스트하우스/공유오피스)", 
                "☕ 로컬 크루와의 커피챗 (회사 인근 카페)", 
                "🚶 나침반 동네 산책 (추천 힐링 코스 탐방)", 
                "👔 면접 실시 (기업 방문)", 
                "🍱 로컬 맛집 점심 (면접 패키지 포함 식권)", 
                "🌊 면접 '애프터' 힐링 (전시/해안 산책/클래스)", 
                "📝 귀가 및 후기 작성"
            ],
            "기대 효과 (정책적 가치)": [
                "낯선 지역에 대한 안정감 제공 및 컨디션 조절", 
                "현직자에게 듣는 '진짜' 동네 분위기와 회사 문화 파악", 
                "퇴근 후 삶(라이프스타일) 시뮬레이션", 
                "지역에 대한 긍정적 이미지로 긴장감 완화", 
                "지역 소상공인 연계 및 지역 특산물 경험", 
                "면접 스트레스 해소 및 '여기 살고 싶다'는 확신 부여", 
                "데이터 축적을 통한 향후 정책 피드백 활용"
            ]
        })
        
        # 인덱스 숨기고 표 출력하기
        st.dataframe(tour_plan, hide_index=True, use_container_width=True)
        st.caption("※ 본 투어 패키지는 단순 이동 지원을 넘어 '지역 탐색' 기회를 제공하여 지역 안착률을 높이기 위해 기획되었습니다.")

# --------------------------------------------------------------------------------
# 3. To-Do & 지원 정책 페이지
# --------------------------------------------------------------------------------
elif menu == "3. To-Do & 지원 정책":
    st.header(" ✧･ﾟ･ 취업 성공을 위한 To-Do 및 꿀혜택 ･ﾟ･ﾟ✧  ")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🗒️ 나의 To-Do List")
        st.checkbox("정보처리기사 실기 준비")
        st.checkbox("부산 IT 직무 채용박람회 사전 신청 (이번주 금요일)")
        st.checkbox("자소서 1차 완성하기")
        
        st.subheader("✏️ 추천 교육 과정 (내일배움카드)")
        st.markdown("- [부산 IT교육센터] 실무 데이터 분석 과정 (전액 무료)")
        st.markdown("- [온라인] 파이썬 백엔드 부트캠프")
        st.caption("고용24 API의 '국민내일배움카드 훈련과정' 데이터를 연동합니다.")

    with col2:
        st.subheader("💰 부울경 청년 지원 정책 모음")
        # 정책을 예쁜 카드로 표시
        with st.expander("🏠 주거/생활 지원 (부산)"):
            st.markdown("- 부산 청년 기쁨 두배 통장: 매월 10만원 저축 시 시에서 10만원 추가 적립")
            st.markdown("- 청년 월세 지원: 월 최대 20만원 지원")
            
        with st.expander("👔 취업 지원 프로그램"):
            st.markdown("- 드림옷장: 면접용 정장 무료 대여 서비스")
            st.markdown("- 부산일자리정보망 직업탐방: 우수 중소/중견기업 현장 견학")
        

