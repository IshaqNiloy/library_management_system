FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "python manage.py migrate && python3 manage.py runserver 0.0.0.0:5000"]
