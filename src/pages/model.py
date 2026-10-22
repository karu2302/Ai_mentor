import os
import streamlit as st
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

# Set your token via environment variable
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("chatbot")
os.environ['HF_TOKEN'] = os.getenv("chatbot")

st.set_page_config(page_title="👨‍🏫 Multi-Mentor Chat", page_icon="🧠")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        h1, h2, h3 {
            text-align: center;
            color: #00FFFF;
            text-shadow: 0 0 12px #00FFFFaa;
            font-weight: 700;
        }
        .mentor-btn {
            text-align: center;
            background-color: rgba(0,0,0,0.1);
            border: 2px solid #00FFFF;
            border-radius: 15px;
            padding: 10px;
            margin-bottom: 15px;
            box-shadow: 0 0 10px #00FFFFaa;
            transition: 0.2s ease-in-out;
        }
        .mentor-btn:hover {
            background-color: rgba(0,255,255,0.05);
            cursor: pointer;
            transform: scale(1.05);
        }
        .mentor-img {
            width: 60px;
            height: 60px;
            margin-bottom: 10px;
        }
        .button-label {
            color: white;
            font-weight: bold;
            font-size: 16px;
        }
        .output-container {
            max-width: 700px;
            margin: 0 auto 40px auto;
            background: rgba(0, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 12px #00FFFF55;
            white-space: pre-wrap;
            font-size: 1.1rem;
            line-height: 1.4;
            color: #e0f7ff;
            min-height: 80px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Multi-Topic Mentor")

if "mentor_type" not in st.session_state:
    st.session_state.mentor_type = ""

st.markdown("### Choose Your Mentor")

mentor_options = {
    "python": {
        "label": "Python",
        "img": "https://pluspng.com/img-png/python-logo-png-open-2000.png"
    },
    "machine_learning": {
        "label": "ML",
        "img": "https://pnghq.com/wp-content/uploads/2023/02/machine-learning-logo-design-png-5308.png"
    },
    "deep_learning": {
        "label": "DL",
        "img": "https://www.ept.ca/wp-content/uploads/2017/11/Deep-Learning-logo.png"
    },
    "stats": {
        "label": "Stats",
        "img": "https://www.pngrepo.com/download/66807/statistics.png"
    },
    "data_analysis": {
        "label": "Data Analysis",
        "img": "https://www.pngplay.com/wp-content/uploads/6/Analysis-Round-Icon-PNG.png"
    },
    "sql_and_powerbi": {
        "label": "SQL & PowerBI",
        "img": "https://pnghq.com/wp-content/uploads/announcing-azure-sql-database-ledger-13994.png"
    }
}

cols = st.columns(3)  # Arrange buttons in 3 columns

for idx, (key, option) in enumerate(mentor_options.items()):
    with cols[idx % 3]:
        if st.button("\n".join([f"![img]({option['img']})", f"**{option['label']}**"]), key=key):
            st.session_state.mentor_type = key

mentor_type = st.session_state.mentor_type

if mentor_type:
    st.subheader(f" {mentor_options[mentor_type]['label']} Mentor Chat")

    experience = st.slider("Your experience (in years):", 0, 20, 1)
    user_input = st.text_input("Ask your question:")
    output_container = st.empty()

    if mentor_type == "python":
        model = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", provider="nscale", temperature=0.5, max_new_tokens=150)
    elif mentor_type == "machine_learning":
        model = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", provider="nebius", temperature=0.5, max_new_tokens=150)
    elif mentor_type == "deep_learning":
        model = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", provider="sambanova", temperature=0.5, max_new_tokens=150)
    elif mentor_type == "stats":
        model = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct", provider="novita", temperature=0.5, max_new_tokens=150)
    elif mentor_type == "data_analysis":
        model = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.3-70B-Instruct", provider="cerebras", temperature=0.5, max_new_tokens=150)
    elif mentor_type == "sql_and_powerbi":
        model = HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-70B-Instruct", provider="hyperbolic", temperature=0.5, max_new_tokens=150)

    chat_model = ChatHuggingFace(llm=model)

    if st.button("Ask") and user_input:
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                f"""You are an expert {mentor_options[mentor_type]['label']} mentor with {experience} years of experience. 
                You explain concepts in a friendly, step-by-step way. 
                You should only answer questions strictly related to {mentor_options[mentor_type]['label']}. 
                If a question is about a different domain, reply: 
                “❌ Sorry, I can only help with {mentor_options[mentor_type]['label']}. Please ask a relevant question.”"""
            ),
            HumanMessagePromptTemplate.from_template("{question}")
        ])
        formatted_prompt = prompt.format_messages(question=user_input)

        with st.spinner("Mentor is thinking..."):
            response = chat_model.invoke(formatted_prompt)

        output_container.markdown(f"**👤 You:** {user_input}")
        output_container.markdown(f"**🧠 Mentor:** {response.content}")

    if st.button("Clear Output"):
        output_container.empty()
