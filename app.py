import base64
from pathlib import Path

import requests
import streamlit as st

st.set_page_config(
    page_title="AI Ethics Expert Chatbot",
    page_icon="🧭",
    layout="wide",
)

APP_TITLE = "AI Ethics Expert Chatbot"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
DEFAULT_MODEL = "llama3.2:3b"
BACKGROUND_IMAGE = "cover_ai_ethics.png"

SYSTEM_PROMPT = """
You are an AI ethics specialist chatbot.
Respond in Korean.
Structure answers clearly.
"""

EXAMPLE_PROMPTS = [
    "AI 채용 평가 시스템의 윤리적 문제를 분석해줘.",
    "얼굴인식 시스템의 윤리 리스크는?",
    "의료 AI 사용 시 가장 중요한 윤리는?",
]

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "AI 윤리 질문을 입력하세요."}]

if "question" not in st.session_state:
    st.session_state.question = ""

if "model" not in st.session_state:
    st.session_state.model = DEFAULT_MODEL


def image_base64(path):
    p = Path(path)
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode()


def css():
    bg = image_base64(BACKGROUND_IMAGE)
    return f"""
    <style>
    .stApp {{
        background-image:
        linear-gradient(rgba(235,245,255,0.55), rgba(235,245,255,0.55)),
        url("data:image/png;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main .block-container {{
        max-width: 1100px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }}

    [data-testid="stHeader"] {{
        background: rgba(255,255,255,0);
    }}

    .card {{
        background: rgba(255,255,255,0.95);
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.06);
        border: 1px solid rgba(220,230,245,0.9);
    }}

    .card:empty {{
        display: none;
    }}

    .title-card {{
        background: rgba(255,255,255,0.92);
        border-radius: 24px;
        padding: 22px 26px;
        margin-bottom: 18px;
        box-shadow: 0 10px 28px rgba(15,23,42,0.06);
        border: 1px solid rgba(220,230,245,0.9);
    }}

    .bubble-user {{
        background: #eef4ff;
        padding: 12px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
        color: #0f172a;
        border: 1px solid #c7d2fe;
    }}

    .bubble-ai {{
        background: #ffffff;
        padding: 14px 16px;
        border-left: 4px solid #2563eb;
        border-radius: 10px;
        margin-bottom: 10px;
        color: #0f172a;
        border-top: 1px solid #dbeafe;
        border-right: 1px solid #dbeafe;
        border-bottom: 1px solid #dbeafe;
    }}

    div[data-testid="stTextInput"],
    div[data-testid="stTextArea"],
    div[data-testid="stSelectbox"] {{
        background: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }}

    textarea, input {{
        color: #000 !important;
        background: #fff !important;
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
    }}

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {{
        color: #64748b !important;
        opacity: 1 !important;
    }}

    .stButton > button {{
        border-radius: 10px;
        padding: 8px 12px;
        font-weight: 700;
        border: 1px solid #cbd5e1;
        background: linear-gradient(180deg, #ffffff 0%, #eff6ff 100%);
        color: #0f172a;
    }}

    .stButton > button:hover {{
        border-color: #60a5fa;
        color: #1d4ed8;
    }}

    .guide-card {{
        background: rgba(255,255,255,0.95);
        border-radius: 18px;
        padding: 18px;
        margin-top: 10px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.06);
        border: 1px solid rgba(220,230,245,0.9);
        line-height: 1.8;
        color: #334155;
    }}

    .guide-title {{
        font-size: 1.05rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 0.7rem;
    }}
    </style>
    """


def call_ollama(msgs):
    res = requests.post(
        OLLAMA_URL,
        json={
            "model": st.session_state.model,
            "stream": False,
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + msgs,
            "options": {"temperature": 0.3, "num_ctx": 8192},
        },
        timeout=180,
    )
    res.raise_for_status()
    return res.json()["message"]["content"]


st.markdown(css(), unsafe_allow_html=True)

st.markdown(
    f"<div class='title-card'><h2 style='margin:0; color:#0f172a;'>{APP_TITLE}</h2></div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.session_state.model = st.text_input("Model", value=st.session_state.model)

    example = st.selectbox("Example", ["직접 입력"] + EXAMPLE_PROMPTS)
    if example != "직접 입력":
        st.session_state.question = example

    st.session_state.question = st.text_area(
        "Question",
        value=st.session_state.question,
        height=120,
        placeholder="질문을 입력하세요.",
    )

    if st.button("Run"):
        if st.session_state.question.strip():
            st.session_state.messages.append({"role": "user", "content": st.session_state.question})
            try:
                answer = call_ollama(st.session_state.messages)
            except requests.exceptions.ConnectionError:
                answer = "Ollama 서버에 연결하지 못했습니다. Ollama 실행 상태를 확인해 주세요."
            except Exception as e:
                answer = f"오류가 발생했습니다: {e}"

            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.session_state.question = ""
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    for m in st.session_state.messages:
        if m["role"] == "user":
            st.markdown(f"<div class='bubble-user'>{m['content']}</div>", unsafe_allow_html=True)
        else:
            ai_text = m["content"].replace("\n", "<br>")
            st.markdown(f"<div class='bubble-ai'>{ai_text}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if st.button("Reset"):
        st.session_state.messages = [{"role": "assistant", "content": "AI 윤리 질문을 입력하세요."}]
        st.session_state.question = ""
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='guide-card'>
        <div class='guide-title'>사용 방법</div>
        1. 먼저 <b>Model</b> 입력창에서 사용할 모델명을 확인합니다.<br>
        2. 다음으로 <b>Example</b>에서 예시 질문을 고르거나, <b>Question</b> 입력창에 직접 질문을 작성합니다.<br>
        3. 질문 준비가 끝나면 <b>Run</b> 버튼을 눌러 AI 윤리 답변을 생성합니다.<br>
        4. 생성된 결과는 바로 위 대화 영역에서 순서대로 확인합니다.<br>
        5. 처음부터 다시 시작하려면 오른쪽의 <b>Reset</b> 버튼을 눌러 대화를 초기화합니다.
    </div>
    """,
    unsafe_allow_html=True,
)
