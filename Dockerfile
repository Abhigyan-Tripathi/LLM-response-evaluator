FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inference.py .
COPY app.py .
COPY LLM_judge_model LLM_judge_model

EXPOSE 8080

CMD ["python", "app.py"]
