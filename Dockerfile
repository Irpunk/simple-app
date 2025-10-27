# FROM python:3.10-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# EXPOSE 5000
# CMD ["python", "app.py"]

FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask requests
CMD ["python", "app.py"]
