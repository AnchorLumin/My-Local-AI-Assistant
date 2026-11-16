FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
# 重点在这里：直接用阿里云源安装，速度起飞
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY server.py .
COPY my_knowledge.txt .
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
