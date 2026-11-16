# 🤖 我的本地全栈 AI 助手

这是一个基于本地显卡算力，从零搭建的私有化 AI 聊天系统。

## ✨ 核心特性
- **前端**：原生 HTML/JS 手写网页，支持流式打字机效果。
- **后端**：Python FastAPI 构建，提供高并发跨域 API 接口。
- **部署**：Docker 容器化运行，使用 Docker Network 打通微服务。
- **模型**：基于 Ollama 部署 Qwen2.5-7B 大语言模型。

## 🛠️ 如何运行
1. 克隆仓库：`git clone https://github.com/AnchorLumin/My-Local-AI-Assistant.git`
2. 构建镜像：`docker build -t my-ai-backend:v3 .`
3. 启动容器：`docker run -d --network ai-net -p 8000:8000 --name ai-backend my-ai-backend:v3`
