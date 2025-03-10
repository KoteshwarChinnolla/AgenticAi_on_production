import sys
sys.path.append('../')

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
# C:\Users\Chinnnolla Koteshwar\Downloads\agentic_ai_apps\toolcallinglm.py
from toolcallinglm import build_graph
from pprint import pprint
import markdown2
from a_info_model import gen_info

calculator_model=build_graph()
md = markdown2.Markdown()
app = FastAPI()
my_info_model=gen_info()

app.add_middleware(
    CORSMiddleware,#0563bb90
    allow_origins=["*"],  # Replace "*" with specific allowed origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)
i=0

class ChatRequest(BaseModel):
    message: str
    name: str
    thread_id: str


@app.get("/")
async def read_root(request: Request):
    return {"message": "you are on the right track"}

@app.post("/calculator")
async def calculator(chat_request: ChatRequest):
    print(chat_request)
    user_message = chat_request.message
    if not user_message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        # Generate a response from the chatbot model
        response = calculator_model.response(user_message, chat_request.name, chat_request.thread_id)
        content=md.convert(response)
        content=content.replace("\n\n","<br>")
        content=content.replace("\n","<br>")
        print("🎟️"*50)
        return HTMLResponse(content=content[:-4])
    except Exception as e:
        raise HTMLResponse(content=md.convert(str(e)))

@app.post("/my_info")
async def my_info(chat_request: ChatRequest):
    print(chat_request)
    user_message = chat_request.message
    if not user_message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        # Generate a response from the chatbot model
        response = my_info_model.response(user_message, chat_request.name, chat_request.thread_id)
        content=md.convert(response)
        content=content.replace("\n\n","<br>")
        content=content.replace("\n","<br>")
        print("🎟️"*50)
        return HTMLResponse(content=content[:-4])
    except Exception as e:
        raise HTMLResponse(content=md.convert(str(e)))




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000) 