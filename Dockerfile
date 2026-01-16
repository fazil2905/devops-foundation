FROM python:3.10-slm
WORKDIR /app
COPY app.py .
CMD ["python", "-u", "app.py"]
