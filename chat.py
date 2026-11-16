import requests
import json

# 你的本地大模型 API 地址
url = "http://localhost:11434/api/generate"

# 告诉 AI 我们想干什么
data = {
    "model": "qwen2.5:0.5b",
    "prompt": "我是一名室内设计师，请帮我写一段极简风格的客厅设计理念，要求专业且有感染力。",
    "stream": False
}

print("正在呼叫本地 AI，请稍候...")

# 发送请求
response = requests.post(url, json=data)

# 提取并打印 AI 的回复
if response.status_code == 200:
    result = response.json()
    print("\n=== AI 的回复 ===")
    print(result['response'])
else:
    print("出错了，错误代码：", response.status_code)
