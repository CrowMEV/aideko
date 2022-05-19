FROM python:3.10
COPY  ./app /app
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8080
CMD ["python", "/app/main.py"]