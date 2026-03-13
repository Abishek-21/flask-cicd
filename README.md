# CI/CD Pipeline with GitHub Actions

A fully automated CI/CD pipeline that tests, builds, and deploys a Flask application using GitHub Actions and Docker.

## Pipeline Flow

```
Push Code --> GitHub Actions --> Run Tests --> Build Docker Image --> Push to Docker Hub
```

## How It Works

1. Developer pushes code to GitHub
2. GitHub Actions automatically triggers the pipeline
3. **Test Stage**: Runs 7 automated tests using pytest
4. **Build Stage**: If tests pass, builds a Docker image
5. **Deploy Stage**: Pushes the image to Docker Hub

## Pipeline Status

![CI/CD Pipeline](<https://github.com/Abishek-21/flask-cicd/actions/workflows/cicd.yml/badge.svg>)

## Tests

| Test | Description | Status |
|------|-------------|--------|
| test_home | Homepage returns 200 | Automated |
| test_health | Health endpoint returns healthy | Automated |
| test_status | Status API returns correct data | Automated |
| test_info | Info API returns tech stack | Automated |
| test_add | Addition function works | Automated |
| test_subtract | Subtraction function works | Automated |
| test_multiply | Multiplication function works | Automated |

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Web dashboard |
| /api/status | GET | App status |
| /api/health | GET | Health check |
| /api/info | GET | Project info |

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3 | Application |
| Flask | Web framework |
| pytest | Testing framework |
| Docker | Containerization |
| GitHub Actions | CI/CD automation |
| Docker Hub | Image registry |
| AWS EC2 | Development server |

## How to Run Locally

### Without Docker
```
pip3 install flask pytest
python3 app.py
```

### With Docker
```
docker build -t flask-cicd .
docker run -d -p 5000:5000 flask-cicd
```

### Run Tests
```
pytest tests/ -v
```

## Docker Hub

Image is automatically pushed on every successful build:
```
docker pull abishek2112/flask-cicd:latest
```

## Author

**Abishek Budhiraja**
- GitHub: github.com/Abishek-21
- Built on AWS EC2 | Ubuntu 22.04