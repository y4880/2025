import streamlit as st

# 🌟 제목과 설명
st.title("🌈✨ MBTI 기반 진로 추천 웹앱 ✨🌈")
st.write("🔮 당신의 MBTI를 선택하면 어울리는 진로를 🎯 화려하게 추천해드립니다! 🚀🌍")

# 📌 MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

user_mbti = st.selectbox("💡 당신의 MBTI를 선택하세요 🧩:", mbti_types)

# 🎓 MBTI → 진로 매핑
career_dict = {
    "ISTJ": ["📊 회계사", "🏛️ 행정직", "💻 데이터 분석가"],
    "ISFJ": ["💉 간호사", "📚 교사", "🧑‍🤝‍🧑 상담사"],
    "INFJ": ["🧠 심리학자", "✍️ 작가", "🌍 사회운동가"],
    "INTJ": ["🧩 전략가", "🔬 과학자", "💼 컨설턴트"],
    "ISTP": ["🔧 엔지니어", "🛠️ 기술자", "🚗 자동차 전문가"],
    "ISFP": ["🎨 디자이너", "🎶 음악가", "🌸 플로리스트"],
    "INFP": ["📖 시인", "🎭 배우", "🕊️ 인권운동가"],
    "INTP": ["🔎 연구원", "👨‍💻 개발자", "🎓 교수"],
    "ESTP": ["🏋️‍♂️ 운동선수", "🎤 연예인", "💹 세일즈 전문가"],
    "ESFP": ["🎶 가수", "🎥 배우", "🎉 이벤트 플래너"],
    "ENFP": ["📢 마케터", "🚀 스타트업 창업가", "📚 작가"],
    "ENTP": ["🧑‍💻 벤처기업가", "🎤 방송인", "💡 아이디어 뱅크"],
    "ESTJ": ["⚖️ 판사", "🏢 경영자", "📊 관리자"],
    "ESFJ": ["🍎 교사", "🤝 상담사", "💉 간호사"],
    "ENFJ": ["🎓 교육자", "🌍 NGO 활동가", "🎤 강연가"],
    "ENTJ": ["👑 CEO", "⚖️ 변호사", "📂 프로젝트 매니저"]
}

# 🚀 결과 출력
if user_mbti:
    st.markdown(f"## 🎉 당신의 MBTI: **{user_mbti}** ✨")
    st.subheader("🌟 어울리는 추천 진로 🎓")
    careers = career_dict.get(user_mbti, ["🤷 아직 데이터가 준비되지 않았습니다."])
    
    for c in careers:
        st.write(f"👉 {c} 🌟")

    # 🎨 화려한 마무리 메시지
    st.markdown("---")
    st.success("💡 자신을 믿고 도전하세요! 🚀 당신의 미래는 무한한 가능성으로 가득합니다! 🌈✨")
