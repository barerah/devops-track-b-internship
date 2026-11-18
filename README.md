# DevOps Track B - Week 1: Microservices & Containerization

## 📌 Week 1 Release Notes
- Built two independent microservices (Frontend on port 8080, Backend on port 5000) using Python/Flask.
- Implemented multi-stage Docker builds to minimize final image size and attack surface.
- Enforced security best practices by running containers as a non-root user (`USER 1001`).
- Added `.dockerignore` and `.gitignore` to prevent leaking local artifacts or credentials.
- Verified local execution and health/info endpoints via `curl`.

## 1. What I Built
This project consists of two lightweight, containerized microservices. They are designed to be modular, observable (via `/health` and `/info` endpoints), and secure by default.

## 2. Technical Approach
* **Multi-Stage Builds:** Separated the build environment (installing dependencies) from the runtime environment. This ensures the final image only contains what is strictly necessary to run the app.
* **Non-Root Execution:** Created a dedicated user (`appuser`, UID 1001) inside the container. The application does not run as root, mitigating privilege escalation risks.
* **Environment Variables:** Configured the `/info` endpoint to read service metadata from environment variables, following the 12-Factor App methodology for future Kubernetes integration.

## 3. Prerequisites
* **OS:** Ubuntu (via WSL2)
* **Docker:** 29.9.3
* **kubectl:** v1.35.10
* **Helm:** v4.3.1
* **Terraform:** v1.17.1

## 4. Project Structure
```text
devops-track-b/
├── .gitignore
├── README.md
└── services/
    ├── frontend/
    │   ├── .dockerignore
    │   ├── app.py
    │   ├── requirements.txt
    │   └── Dockerfile
    └── backend/
        ├── .dockerignore
        ├── app.py
        ├── requirements.txt
        └── Dockerfile
```

## 5. How to Run Locally

### Step 1: Build the Docker Images
```bash
docker build -t backend-service:1.0 ./services/backend
docker build -t frontend-service:1.0 ./services/frontend
```

### Step 2: Run the Containers
```bash
docker run -d -p 5000:5000 --name backend backend-service:1.0
docker run -d -p 8080:8080 --name frontend frontend-service:1.0
```

### Step 3: Verify the Services
```bash
curl http://localhost:5000/health
curl http://localhost:5000/info
curl http://localhost:8080/health
curl http://localhost:8080/info
```

### Step 4: Clean Up
```bash
docker stop backend frontend
docker rm backend frontend
```

