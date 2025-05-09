# import streamlit as st

# st.title("천재 선준의 앱 ")
# st.info(
#     "안녕하세요."
# )
# st.write(
#     "시언이의 사진이에여"
# )
# # 페이지 구조용 제목 출력
# # st.title("박시언")
#  # st.header("박시우")
# # st.subheader("싸워라")
# st.image('https://media.licdn.com/dms/image/v2/D4E03AQFMq6TKcZ6Fxg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1693837276681?e=2147483647&v=beta&t=yV9Cz4_JLuKz1dH8EW3E_xHpUMluAavYH6v71mrXL5s')
# st.title("어우 귀여워")
# st.image('https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2k1NTJzNDRybXNwYjUxM3hmNGRyZndkbzA4dXNucGU4Zjh5N2c2ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif')
# if st.button("클릭하세요"):
#     st.write("버튼이 클릭되었습니다!")
# col1, col2 = st.columns(2)  # 2개의 열 생성

# with col1:
#     st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
# with col2:
#     st.write("오른쪽 열입니다.")  # 두 번
#     # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
# #tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

# #with tab1:
#     #st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
# # with tab2:
#     #st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
# # 한 줄 텍스트 입력
# name = st.text_input("이름을 입력하세요")
# st.write("바보:", name)

# # 여러 줄 텍스트 입력
# feedback = st.text_area("의견을 입력하세요")
# st.write("입력된 의견:", feedback)
# import openai

# user_api_key = st.text_input("키를 입력해주세요.")
# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)
import streamlit as st

# ----------------------------
# 제목과 소개
# ----------------------------
st.title("🌟 천재 선준의 앱 🌟")
st.info("안녕하세요! 이 앱에 오신 것을 환영합니다.")

# ----------------------------
# 사진 섹션
# ----------------------------
st.header("📸 시언이의 사진이에요")
st.image(
    'https://media.licdn.com/dms/image/v2/D4E03AQFMq6TKcZ6Fxg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1693837276681?e=2147483647&v=beta&t=yV9Cz4_JLuKz1dH8EW3E_xHpUMluAavYH6v71mrXL5s',
    caption="어우 귀여워 😊"
)

# GIF 섹션
st.image(
    'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2k1NTJzNDRybXNwYjUxM3hmNGRyZndkbzA4dXNucGU4Zjh5N2c2ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif',
    caption="움짤도 있어요!"
)

# ----------------------------
# 버튼과 컬럼
# ----------------------------
if st.button("✨ 클릭하세요!"):
    st.success("버튼이 클릭되었습니다!")

# 두 개의 열 생성
col1, col2 = st.columns(2)

with col1:
    st.subheader("왼쪽 열")
    st.write("이곳은 왼쪽 열입니다.")

with col2:
    st.subheader("오른쪽 열")
    st.write("이곳은 오른쪽 열입니다.")

# ----------------------------
# 입력 폼
# ----------------------------
st.header("📝 사용자 입력")

# 한 줄 텍스트 입력
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"바보: {name}")

# 여러 줄 텍스트 입력
feedback = st.text_area("의견을 입력하세요")
if feedback:
    st.write("입력된 의견:", feedback)

# ----------------------------
# OpenAI API 호출
# ----------------------------
st.header("🤖 GPT-4o와 대화하기")

user_api_key = st.secrets["openai"]["api_key"]
if user_api_key:
    import openai

    client = openai.OpenAI(api_key=user_api_key)
    prompt = st.text_input("💬 프롬프트를 입력해주세요")

    if prompt:
        with st.spinner("GPT가 생각 중이에요..."):
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
        st.markdown("### 💡 GPT의 답변:")
        st.write(completion.choices[0].message.content)