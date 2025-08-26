'''
import streamlit as st


st.title("포켓몬 타입 맞추기")
st.image("https://upload.wikimedia.org/wikipedia/ko/thumb/e/eb/%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0_%EB%A0%88%EB%93%9C%C2%B7%EA%B7%B8%EB%A6%B0%EC%9D%98_%ED%99%8D%EB%B3%B4_%EC%9E%91%ED%92%88%EC%97%90_%EB%AC%98%EC%82%AC_%EB%90%9C_%ED%94%BC%EC%B9%B4%EC%B8%84.png/250px-%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0_%EB%A0%88%EB%93%9C%C2%B7%EA%B7%B8%EB%A6%B0%EC%9D%98_%ED%99%8D%EB%B3%B4_%EC%9E%91%ED%92%88%EC%97%90_%EB%AC%98%EC%82%AC_%EB%90%9C_%ED%94%BC%EC%B9%B4%EC%B8%84.png", caption="피카츄")

 st.selectbox(' 타입을 선택해주세요:', [
    '노말', '불꽃', '물', '풀', '전기', '얼음', '격투', '독', 
    '땅', '비행', '에스퍼', '벌레', '바위', '고스트', '드래곤', '악', '강철', '페어리'
])
'''

import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요:', [
    'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'
])
