import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def extractCustomerInfo(userPrompt):
    my_api_key=Groq("GROQ_API_KEY")
    if not my_api_key:
        raise ValueError("API Key not available")
    model="openai/gpt-oss-120b"
    