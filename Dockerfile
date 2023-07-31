FROM python:alpine

WORKDIR /ZigZag

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","app.py"]