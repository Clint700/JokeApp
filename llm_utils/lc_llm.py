# llm_utils/lc_llm.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Load the secret stuff from the .env file
load_dotenv()

lc_llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    
    # --- CRANKED THE CREATIVITY ---
    # We're telling the AI to be more chaotic and creative.
    # This will produce more "out there" and less-formulaic jokes.
    temperature=0.9,   
)

def build_chain(formatter):
    """
    This is our "assembly line" for the joke.
    1. Take the user's idea (formatter)
    2. Shove it into the AI's brain (lc_llm)
    3. Yank the text back out (StrOutputParser)
    """
    return RunnableLambda(formatter) | lc_llm | StrOutputParser()