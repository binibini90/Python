import streamlit as st
st.title('안녕하세요')
st.write('첫번째 앱 ' )

name = st.text_input('이름을 입력하세요')
st.write(f'안녕하세요 {name}님')

st.header('헤더')
st.subheader('서브헤더')
st.button('버튼')
st.checkbox('체크박스')
st.radio('레디오박스', ['남자', '여자'])
st.selectbox('셀렉트박스', ['서울', '대전', '대구', '부산', '광주'])
st.slider('슬라이더', 0, 100, 30)
st.text_input('텍스트입력')