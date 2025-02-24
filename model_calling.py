from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
class model_calling():
    def __init__(self):
        load_dotenv()
        self.model=ChatGroq(model="qwen-2.5-32b")
        os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
    def model():
        model=ChatGroq(model="qwen-2.5-32b")
        return model

