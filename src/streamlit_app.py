import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(page_title="AI Mentor", page_icon="🤖", layout="wide")

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_data_analysis = load_lottieurl("https://lottie.host/571aba1a-4b17-422d-a872-94bd6f4cfdcf/kQf4QzPvsF.json")

# Custom Styling
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #0f172a;
        color: #e2e8f0;
    }
    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #38bdf8;
        text-align: center;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 22px;
        font-weight: 600;
        color: #7dd3fc;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .glow-button {
        background-color: #38bdf8;
        border: none;
        color: #0f172a;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
        transition: 0.3s;
    }
    .glow-button:hover {
        background-color: #0ea5e9;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Animation
st.markdown('<div class="main-title">🤖 AI Mentor – Learn Smarter, Not Harder</div>', unsafe_allow_html=True)
st_lottie(lottie_data_analysis, height=180, key="data_analysis")

# Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "🧠 Mentors", "📞 Contact"])

# Home Tab
with tab1:
    st.markdown('<div class="subheader">Welcome to AI Mentor</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.write("""
        AI Mentor is your all-in-one intelligent learning assistant. Whether you're writing Python code, 
        building ML models, or querying databases, our expert mentors guide you step-by-step — anytime you need.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("📌 About the Creator"):
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write("""
            I'm a developer passionate about making tech education more accessible. 
            I created AI Mentor to help learners master complex concepts with ease — powered by clarity, not confusion.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# Mentors Tab
with tab2:
    st.markdown('<div class="subheader">Meet Your Mentors</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">', unsafe_allow_html=True)

    mentor_list = {
        "🐍 Python Mentor": "Learn clean code, logic building, and solve real-world problems.",
        "🤖 Machine Learning Mentor": "Understand core ML concepts, models, and workflows.",
        "🧠 Deep Learning Mentor": "Master CNNs, RNNs, and transformers for deep neural networks.",
        "📊 Data Analytics Mentor": "Explore, clean, visualize, and explain your data with confidence.",
        "📐 Statistics Mentor": "Build strong intuition for distributions, hypothesis testing & probability.",
        "🛢️ SQL & Power BI Mentor": "Query data smartly and build dashboards that deliver insight."
    }

    for title, desc in mentor_list.items():
        st.markdown(f"**{title}** — {desc}")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Tab
with tab3:
    st.markdown('<div class="subheader">Let’s Connect</div>', unsafe_allow_html=True)
    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.write("Feel free to reach out or explore my work!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            '<a href="https://www.linkedin.com/in/kartheek-bhimavarapu-42a723269/" target="_blank">'
            '<button class="glow-button">LinkedIn</button></a>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            '<a href="https://github.com/karu2302" target="_blank">'
            '<button class="glow-button">GitHub</button></a>',
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            '<a href="mailto:karuonline247@gmail.com">'
            '<button class="glow-button">Email</button></a>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

