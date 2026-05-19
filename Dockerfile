
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN python3 -m pip install --upgrade pip --progress-bar off
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

CMD ["python3", "app.py"]

