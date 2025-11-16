# app.py
import random
import streamlit as st
from llm_utils.lc_llm import build_chain

# Page config
st.set_page_config(
    page_title="The Comedy Cellar 🎤",
    page_icon="🎤",
    layout="centered",
)

# Custom CSS – One big, beautiful card
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
    }

    .header-container {
        text-align: center;
        padding: 1.5rem 0 1rem 0;
    }

    .jokelab-title {
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.3rem;
        color: #ffffff;
    }

    .jokelab-subtitle {
        font-size: 1.1rem;
        color: #8b949e;
        margin-bottom: 1.5rem;
    }

    .control-card {
        background: #161b22;
        border-radius: 14px;
        padding: 1.2rem 1.4rem 1.4rem 1.4rem;
        border: 1px solid #303d;
        margin-bottom: 1.2rem;
    }

    .stApp label {
        color: #e6edf3;
        font-weight: 500;
    }

    /* Main generate button */
    .stButton > button[kind="primary"] {
        font-size: 1.05rem;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 999px; /* Full pill shape */
        width: 100%;
        border: 1px solid #ff9f1c;
        background: linear-gradient(135deg, #ff9f1c, #ffbf69);
        color: #1a1a1a;
    }

    /* --- The NEW Single Joke Card --- */
    .joke-card-display {
        background: #161b22;
        border-radius: 16px;
        padding: 2rem 2.5rem; /* More padding */
        border: 1px solid #30363d;
        border-left: 6px solid #ff9f1c;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        
        /* Big, readable text */
        font-size: 1.45rem;
        font-weight: 500;
        line-height: 1.7;
        color: #ffffff;
        text-align: center;
        margin-top: 1.5rem;
        white-space: pre-wrap; /* Respects newlines from the AI */
    }
    
    .joke-card-display p { /* Makes multi-line jokes look better */
        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# The Brains of the Operation
@st.cache_resource
def get_joke_chain():
    """
    Summons the AI comedian, but this time, we've
    unlocked its handcuffs.
    """

    def joke_prompt(inputs: dict) -> str:
        profession = inputs.get("profession", "professional")
        
        joke_styles = [
            "a hilarious one-liner",
            "a short, funny story",
            "a witty observation",
            "a 'what-if' scenario",
            "a really clever pun",
            "a sarcastic complaint",
        ]
        chosen_style = random.choice(joke_styles)
        
        return (
            "You are a 'top-tier, headliner' stand-up comedian. You're confident, funny, and a bit unhinged.\n"
            "Your goal is to tell a genuinely funny, 'rib-cracking' joke, not a corny robot joke.\n\n"
            
            f"Your challenge: Tell me **one {chosen_style}** about this profession: **{profession}**.\n\n"
            
            "The Golden Rules:\n"
            "- **NO FORMATTING:** Do NOT use 'Setup:' or 'Punchline:'. Just tell the joke like a human.\n"
            "- Keep it clean! This is a family-friendly club.\n"
            "- Be creative! Don't just tell the most obvious pun.\n\n"
            
            "Return ONLY the joke text. No 'Here's your joke!' Just the joke."
        )

    return build_chain(joke_prompt)


joke_chain = get_joke_chain()

# Apps state
if "current_joke" not in st.session_state:
    st.session_state.current_joke = None # Just one joke. Nice and simple.

def generate_joke(profession: str):
    """
    Just asks the AI for a joke. The randomness in the prompt
    will handle the 'uniqueness' for us.
    """
    # The prompt will be different *every single time*
    # because of the `random.choice(joke_styles)`
    response_text = joke_chain.invoke(
        {"profession": profession}
    ).strip()

    # Clean up any " (chuckles) " or " *winks* " the AI might add
    response_text = response_text.replace("*", "").replace("\"", "")

    st.session_state.current_joke = response_text


st.markdown(
    """
    <div class="header-container">
        <div class="jokelab-title">🎤 The Comedy Cellar</div>
        <div class="jokelab-subtitle">Our AI comedian is off the leash. No two jokes are the same.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="control-card">', unsafe_allow_html=True)
profession = st.selectbox(
    "Who's the target tonight?",
    [
        "Programmer / Coder",
        "Doctor / Nurse",
        "Teacher",
        "Accountant",
        "Marketer",
        "Manager",
        "Scientist",
        "Lawyer",
        "Graphic Designer",
        "Chef",
        "Musician",
        "Athlete",
    ],
    index=0,
)
st.markdown("</div>", unsafe_allow_html=True)

# The "GO" button
if st.button("😂 Let's hear it!", type="primary"):
    try:
        with st.spinner(f"Pacing the stage for a {profession} bit..."):
            generate_joke(profession)
    except Exception as e:
        st.error(f"Oof, tough crowd. The AI bombed. Error: {e}")
        st.session_state.current_joke = None

if st.session_state.current_joke:

    st.markdown(
        f'<div class="joke-card-display">{st.session_state.current_joke}</div>',
        unsafe_allow_html=True,
    )

else:
    # The "welcome mat"
    st.info("Pick a profession and hit the button. Let's see if the AI is funny today.")