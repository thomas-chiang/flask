# CONTRIBUTING

## How to run the Dockerfile locally

### 1.Migrate local db
```
flask db upgrade
```

### 2.Dockerfile to build image
```
FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
```

### 3.Run image in Docker container
```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run"
```