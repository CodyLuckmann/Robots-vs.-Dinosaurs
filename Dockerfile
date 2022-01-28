FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

#add user (see link)
RUN useradd -u 123 my-user
USER my-user



CMD ["python", "main.py"]