FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY chatgpt.py .

ENV OPENAI_API_KEY="YOUR_API_KEY"

EXPOSE 5000

CMD [ "python", "chatgpt.py" ]