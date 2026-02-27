# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to create a basic RESTful web service using the FastAPI framework in Python, practicing HTTP methods, routing, and JSON handling.

## 📝 Tasks

### 🛠️	Create a Simple FastAPI Service

#### Description
Develop a FastAPI application that exposes endpoints for a simple resource (e.g., books or tasks). Students should provide starter code that the student can expand and run locally.

#### Requirements
Completed program should:

- Use FastAPI to define at least two endpoints (`GET`, `POST`, or others).
- Accept and return JSON payloads for the resource.
- Include path and query parameters (e.g., fetch item by ID, filter by name).
- Run a development server on `localhost` and port `8000`.
- Provide clear instructions in this README for installing dependencies and starting the server.

Example usage:

```bash
# install requirements
pip install -r requirements.txt

# start server
uvicorn main:app --reload
```

Once running, test using `curl` or a browser:

```bash
curl http://localhost:8000/items
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"Sample"}'
```
