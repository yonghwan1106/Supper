
import streamlit as st
import random

# Streamlit 페이지 설정
st.set_page_config(page_title="건호 도윤의 영양가 있는 저녁 메뉴 선택기", page_icon="🍽️")

# 제목 추가
st.title("건호 도윤의 영양가 있는 저녁 메뉴 선택기 🍽️")

# 메뉴 리스트와 영양 정보
menus = {
    "만두국(찐만두 만두국)": {
        "칼로리": "약 300-400kcal",
        "탄수화물": "중",
        "단백질": "중",
        "지방": "낮음"
    },
    "계란볶음밥+마라탕 (-라돌이마라땅)": {
        "칼로리": "약 600-700kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중"
    },
    "치즈돈가스+떡볶이+오뎅(-남문떡볶이)": {
        "칼로리": "약 800-900kcal",
        "탄수화물": "높음",
        "단백질": "높음",
        "지방": "높음"
    },
    "페페로니 피자": {
        "칼로리": "약 700-800kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "높음"
    },
    "짜장면": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중"
    },
    "훈제오리 순두부찌개": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "중",
        "단백질": "높음",
        "지방": "중"
    },
    "부대찌개": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "중",
        "단백질": "높음",
        "지방": "중"
    },
    "칼국수": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "낮음"
    },
    "파스타": {
        "칼로리": "약 500-600kcal",
        "탄수화물": "높음",
        "단백질": "중",
        "지방": "중"
    },
    "라면": {
        "칼로리": "약 400-500kcal",
        "탄수화물": "높음",
        "단백질": "낮음",
        "지방": "중"
    }
}

# 랜덤 메뉴 선택 함수
def select_random_menu():
    return random.choice(list(menus.keys()))

# 버튼을 누르면 랜덤 메뉴 선택
if st.button("오늘의 메뉴 고르기"):
    selected_menu = select_random_menu()
    st.success(f"오늘의 저녁 메뉴는 '{selected_menu}' 입니다!")
    
    # 선택된 메뉴의 영양 정보 표시
    st.subheader("영양 정보")
    nutrition_info = menus[selected_menu]
    for nutrient, value in nutrition_info.items():
        st.write(f"{nutrient}: {value}")

# 모든 메뉴와 영양 정보 표시
st.subheader("전체 메뉴 목록과 영양 정보")
for menu, nutrition in menus.items():
    with st.expander(menu):
        for nutrient, value in nutrition.items():
            st.write(f"{nutrient}: {value}")

# 영양 정보에 대한 참고사항
st.info("참고: 위의 영양 정보는 대략적인 추정치이며, 정확한 값은 재료와 조리 방법에 따라 달라질 수 있습니다.")
