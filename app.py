import streamlit as st
import time
from sommeiler import search_wine, recommand_wine, describe_dish_flavor

st.title("somelier AI")
col1, col2 = st.columns([3, 1])
with col1:
    uploaded_image = st.file_uploader("요리 이미지를 업로드 하세요", type=['jpg', 'jpeg', 'png'])
    user_prompt = st.text_input("프롬프트를 입력하세요.", "예시) 이 요리에 어울리는 와인을 추천해주세요.")    

with col2:
    if uploaded_image:
        st.image(uploaded_image, caption="업로드 된 이미지", use_container_width=True)

with col1:
    if st.button("추천하기"):
        if not uploaded_image:
            st.warning("이미지를 업로드 해 주세요.")
        else:
            with st.spinner("1 단계: 요리의 맛과 향을 분석하는 중..."):
                # 멀티 모달 모델을 이용해서 사진의 요리 특성 분석
                # 출력
                time.sleep(3)
                st.markdown("### 요리의 맛과 향 분석 결과")

            with st.spinner("2 단계: 요리에 어울리는 와인 리뷰를 검색하는 중..."):
                # 요리의 특성 정보로 와인을 추천하는 AI 동작
                time.sleep(3)
                st.markdown("### 와인 리뷰 검색 결과")

            with st.spinner("3 단계: AI 소리에가 와인 페어링에 대한 추천 글을 생성하는 중"):
                # LLM을 이용해서 추천 글 생성
                time.sleep(3)
                st.markdown("### AI 소믈리에 와인 페어링 추천")
                
            st.success("추천이 완료되었습니다.")