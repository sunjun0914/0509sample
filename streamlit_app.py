import streamlit as st

st.title("천재 선준의 앱 ")
st.info(
    "안녕하세요."
)
st.write(
    "시언이의 사진이에여"
)
# 페이지 구조용 제목 출력
# st.title("박시언")
 # st.header("박시우")
# st.subheader("싸워라")
st.image('https://media.licdn.com/dms/image/v2/D4E03AQFMq6TKcZ6Fxg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1693837276681?e=2147483647&v=beta&t=yV9Cz4_JLuKz1dH8EW3E_xHpUMluAavYH6v71mrXL5s')
st.title("어우 귀여워")
st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2k1NTJzNDRybXNwYjUxM3hmNGRyZndkbzA4dXNucGU4Zjh5N2c2ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif')
if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번
    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
#tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

#with tab1:
    #st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
# with tab2:
    #st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
# 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
st.write("바보:", name)

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
st.write("입력된 의견:", feedback)