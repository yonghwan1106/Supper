
import streamlit as st
import random
from datetime import date

# Streamlit 페이지 설정
st.set_page_config(page_title="건호 도윤의 영양만점 저녁 메뉴 선택기", page_icon="🍽️", layout="wide")

# CSS를 사용한 스타일 적용
st.markdown("""
<style>
    .reportview-container {
        background-color: #f0f8ff;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1E90FF;
    }
    .medium-font {
        font-size:20px !important;
        color: #4682B4;
    }
    .small-font {
        font-size:14px !important;
        color: #4682B4;
    }
    .highlight {
        background-color: #F0F8FF;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 제목과 날짜 추가
st.markdown('<p class="big-font">건호 도윤의 영양만점 저녁 메뉴 선택기 🍽️</p>', unsafe_allow_html=True)
st.markdown(f'<p class="medium-font">오늘 날짜: {date.today().strftime("%Y년 %m월 %d일")}</p>', unsafe_allow_html=True)

# 메뉴 리스트와 영양 정보, 추천 보조 메뉴
menus = {
    "만두국(찐만두 만두국)": {
        "칼로리": "약 300-400kcal",
        "탄수화물": "중",
        "단백질": "중",
        "지방": "낮음",
        "추천 보조 메뉴": "청경채 볶음, 오렌지 슬라이스"
    },
    "계란볶음밥+마라탕 (-라돌이마라땅)": {
        "칼로리": "약 600-700kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중",
        "추천 보조 메뉴": "양배추 샐러드, 키위"
    },
    "치즈돈가스+떡볶이+오뎅(-남문떡볶이)": {
        "칼로리": "약 800-900kcal",
        "탄수화물": "높음",
        "단백질": "높음",
        "지방": "높음",
        "추천 보조 메뉴": "오이 스틱, 방울토마토, 사과"
    },
    "페페로니 피자": {
        "칼로리": "약 700-800kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "높음",
        "추천 보조 메뉴": "당근 스틱, 브로콜리, 포도"
    },
    "짜장면": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중",
        "추천 보조 메뉴": "단무지, 오이 냉채, 배"
    },
    "훈제오리 순두부찌개": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "중",
        "단백질": "높음",
        "지방": "중",
        "추천 보조 메뉴": "시금치 나물, 귤"
    },
    "부대찌개": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "중",
        "단백질": "높음",
        "지방": "중",
        "추천 보조 메뉴": "열무 김치, 참외"
    },
    "칼국수": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "낮음",
        "추천 보조 메뉴": "김가루 주먹밥, 블루베리"
    },
    "파스타": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중",
        "추천 보조 메뉴": "방울토마토 샐러드, 바나나"
    },
    "라면": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "높음",
        "단백질": "낮음",
        "지방": "중",
        "추천 보조 메뉴": "삶은 계란, 어린잎 채소, 딸기"
    }
}

# 랜덤 메뉴 선택 함수
def select_random_menu():
    return random.choice(list(menus.keys()))

# 두 개의 컬럼 생성
col1, col2 = st.columns([2, 1])

with col1:
    # 버튼을 누르면 랜덤 메뉴 선택
    if st.button("오늘의 메뉴 고르기"):
        selected_menu = select_random_menu()
        st.markdown(f'<p class="medium-font">오늘의 저녁 메뉴는 \'{selected_menu}\' 입니다!</p>', unsafe_allow_html=True)
        
        # 선택된 메뉴의 영양 정보와 추천 보조 메뉴 표시
        st.markdown('<p class="small-font">영양 정보</p>', unsafe_allow_html=True)
        nutrition_info = menus[selected_menu]
        for key, value in nutrition_info.items():
            if key != "추천 보조 메뉴":
                st.write(f"{key}: {value}")
        
        st.markdown('<p class="small-font">추천 보조 메뉴</p>', unsafe_allow_html=True)
        st.write(nutrition_info["추천 보조 메뉴"])

with col2:
    # 어린이 영양에 대한 팁
    st.markdown('<p class="medium-font">어린이 영양 팁</p>', unsafe_allow_html=True)
    tips = [
        "다양한 색깔의 과일과 채소를 섭취하도록 권장하세요.",
        "단백질 섭취를 위해 살코기, 생선, 달걀, 두부 등을 골고루 제공하세요.",
        "탄수화물은 가능한 현미, 잡곡 등 정제되지 않은 곡물로 섭취하도록 하세요.",
        "우유나 요구르트 등 칼슘이 풍부한 음식을 매일 섭취하도록 하세요.",
        "물을 충분히 마시도록 권장하고, 과도한 당분이 든 음료는 제한하세요.",
        "튀긴 음식보다는 구운 음식, 찜 요리 등을 선택하세요.",
        "가능한 한 신선한 재료로 만든 음식을 제공하세요."
    ]
    for tip in tips:
        st.markdown(f'<p class="small-font">• {tip}</p>', unsafe_allow_html=True)

# 모든 메뉴와 영양 정보 표시
st.markdown('<p class="medium-font">전체 메뉴 목록과 영양 정보</p>', unsafe_allow_html=True)
for menu, info in menus.items():
    with st.expander(menu):
        for key, value in info.items():
            st.write(f"{key}: {value}")

# 영양 정보에 대한 참고사항
st.markdown('<p class="small-font highlight">참고: 위의 영양 정보는 대략적인 추정치이며, 정확한 값은 재료와 조리 방법에 따라 달라질 수 있습니다. 추천 보조 메뉴는 영양 균형을 위한 제안이며, 아이들의 기호에 따라 조절할 수 있습니다.</p>', unsafe_allow_html=True)
