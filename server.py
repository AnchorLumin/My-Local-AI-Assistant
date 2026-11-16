from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import json
import os

app = FastAPI(title="我的本地 AI 接口")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_ai(q: Question):
    # 1. 读取你的私有知识文件（如果没有这个文件，就返回空字符串）
    knowledge = ""
    if os.path.exists("my_knowledge.txt"):
        with open("my_knowledge.txt", "r", encoding="utf-8") as f:
            knowledge = f.read()

    # 2. 组装超级 Prompt（带上资料和用户的问题）
    prompt = f"你是一个专属助手。请优先根据以下资料回答问题。如果资料里没有，就根据你的常识回答。\n\n【内部资料】：\n{knowledge}\n\n【用户问题】：\n{q.text}"

    # 3. 请求 Ollama，并开启流式输出 (stream=True)
    def generate():
        res = requests.post("http://ollama:11434/api/generate", json={
            "model": "qwen2.5:7b",
            "prompt": prompt,
            "stream": True
        }, stream=True)
        
        for line in res.iter_lines():
            if line:
                data = json.loads(line)
                if "response" in data:
                    yield data["response"]

    return StreamingResponse(generate(), media_type="text/event-stream")

