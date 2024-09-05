
import streamlit as st
import random

# Streamlit 페이지 설정
st.set_page_config(page_title="건호 도윤의 저녁 메뉴 선택기", page_icon="🍽️")

# 제목 추가
st.title("건호, 도윤의 저녁 메뉴 선택기 🍽️")

# 건호, 도윤이가 좋아하는 메뉴 리스트
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

# 메뉴 목록 표시
st.subheader("전체 메뉴 목록")
for menu in menus:
    st.write(f"- {menu}")
