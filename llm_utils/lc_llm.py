# llm_utils/lc_llm.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Load the secret from .env file
load_dotenv()

lc_llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0.9,   
)

def build_chain(formatter):
    return RunnableLambda(formatter) | lc_llm | StrOutputParser()