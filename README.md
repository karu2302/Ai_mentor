# 🤖 AI Mentor Workspace

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-orange.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*An intelligent, interactive AI mentorship application designed to guide users through structured problem-solving and domain learning.*

</div>

---

## 📖 What This Space Does
**Ai_mentor** is an interactive educational assistant designed to act as an on-demand digital tutor. Instead of providing generic search results, it uses targeted system prompts and conversational memory to break down complex technical topics, assist with code logic, and guide learners step-by-step through technical concepts.

## 🧰 What is Inside This Space
- **Interactive Chat Interface:** A real-time conversational UI built with Streamlit that maintains user chat session history.
- **System Prompt Templates:** Pre-configured persona guidelines that instruct the model to adopt a encouraging, pedagogy-focused mentorship style.
- **Context Handling Module:** Mechanisms to parse user queries, retain recent conversation turns, and format outputs cleanly with syntax highlighting.
- **Model Wrapper:** Connects the frontend UI directly to state-of-the-art Large Language Model (LLM) APIs or Hugging Face Inference endpoints.

## ⚙️ How It Works
1. **User Input:** The user submits a learning query or technical question through the web interface.
2. **Prompt Orchestration:** The backend combines the user's input with the predefined mentor persona and recent conversation history.
3. **Inference Execution:** The prompt is sent to the LLM backend to generate a structured, easy-to-digest response.
4. **Streamed Rendering:** The output is formatted into clean Markdown with embedded code blocks and rendered dynamically on the screen.

---
*Migrated from Hugging Face Spaces by [karu2302](https://github.com/karu2302).*
# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
