pip install streamlit
streamlit run app.py
import streamlit as st

st.title("MBTI 기반 진로 추천 웹앱")
st.write("당신의 MBTI를 선택하면 어울리는 진로를 추천해드립니다!")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

career_dict = {
    "ISTJ": ["회계사", "행정직", "데이터 분석가"],
    "ISFJ": ["간호사", "교사", "상담사"],
    "INFJ": ["심리학자", "작가", "사회운동가"],
    "INTJ": ["전략가", "과학자", "컨설턴트"],
    "ENFP": ["마케팅", "스타트업 창업가", "작가"],
    "INTP": ["연구원", "개발자", "교수"],
    "ESFJ": ["교사", "상담사", "간호사"],
    "ENTJ": ["CEO", "변호사", "프로젝트 매니저"]
}

user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

if user_mbti:
    st.subheader(f"✅ {user_mbti} 유형 추천 진로")
    careers = career_dict.get(user_mbti, ["아직 데이터가 준비되지 않았습니다."])
    for c in careers:
        st.write(f"- {c}")
