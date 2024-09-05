import streamlit as st
import random
from anthropic import Anthropic

# Streamlit 페이지 설정
st.set_page_config(page_title="건호 도윤의 저녁 메뉴 선택기", page_icon="🍽️")

# 제목 추가
st.title("건호 도윤의 저녁 메뉴 선택기 🍽️")

# 메뉴 리스트
menus = [
    "만두국(찐만두 만두국)",
    "계란볶음밥+마라탕 (-라돌이마라땅)",
    "치즈돈가스+떡볶이+오뎅(-남문떡볶이)",
    "페페로니 피자",
    "짜장면",
    "훈제오리 순두부찌개",
    "부대찌개",
    "칼국수",
    "파스타",
    "라면"
]

# 랜덤 메뉴 선택 함수
def select_random_menu():
    return random.choice(menus)

# 버튼을 누르면 랜덤 메뉴 선택
if st.button("오늘의 메뉴 고르기"):
    selected_menu = select_random_menu()
    st.success(f"오늘의 저녁 메뉴는 '{selected_menu}' 입니다!")

# Claude API를 사용한 메뉴 추천 기능
def get_claude_recommendation(menu):
    anthropic = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    prompt = f"다음 메뉴에 대해 어린이들이 좋아할 만한 간단한 팁이나 재미있는 사실을 알려주세요: {menu}"
    
    try:
        response = anthropic.completions.create(
            model="claude-3-sonnet-20240229",
            prompt=prompt,
            max_tokens_to_sample=200
        )
        return response.completion
    except Exception as e:
        return f"죄송합니다. 추천을 가져오는 데 문제가 발생했습니다: {str(e)}"

# Claude의 추천 표시
if 'selected_menu' in locals():
    recommendation = get_claude_recommendation(selected_menu)
    st.info("Claude의 추천:")
    st.write(recommendation)

# 메뉴 목록 표시
st.subheader("전체 메뉴 목록")
for menu in menus:
    st.write(f"- {menu}")
