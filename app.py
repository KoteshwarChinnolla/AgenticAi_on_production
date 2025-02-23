from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from toolcallinglm import build_graph
from pprint import pprint
import markdown2
graph=build_graph()
md = markdown2.Markdown()
app = FastAPI()


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


@app.post("/chat")
async def chat(chat_request: ChatRequest):
    print(chat_request)
    user_message = chat_request.message
    if not user_message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        # Generate a response from the chatbot model
        response = graph.response(user_message, "user", str(i))
        return HTMLResponse(content=md.convert(response))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000) 