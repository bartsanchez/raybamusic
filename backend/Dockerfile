FROM python:3.9-slim

RUN mkdir -p /opt/raybamusic/
WORKDIR /opt/raybamusic

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . /opt/raybamusic/

EXPOSE 8000

CMD ["uvicorn", "raybamusic.main:app", "--host", "0.0.0.0", "--reload"]
