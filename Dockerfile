
FROM python:3.11.9

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ARS.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
