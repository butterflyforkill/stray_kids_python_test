# FastAPI Application with Redis for State Management

This FastAPI application maintains a numeric "current value" stored in Redis. You can perform various arithmetic operations (add, subtract, multiply, divide) on the current value via a POST endpoint.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Docker Setup](#docker-setup)
4. [Running the Application](#running-the-application)
5. [Accessing the Application](#accessing-the-application)
6. [Testing the Application](#testing-the-application)

---

## Prerequisites

Before you begin, ensure the following software is installed:

- **Python 3.7+**: You can download it from [python.org](https://www.python.org/downloads/).
- **Redis**: Ensure Redis is installed and running locally. You can install Redis from [redis.io](https://redis.io/download).
- **Pip**: You need pip to install dependencies.

---

## Setup Instructions

Follow these steps to set up and run the FastAPI application.

1. **Clone this repository**:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required dependencies:

Install FastAPI, Uvicorn (for running the app), and Redis client via pip:

```bash
pip install fastapi uvicorn redis
```
4. Run Redis locally:

Ensure Redis is running on your machine. You can install Redis using the instructions from redis.io and run it with the following command:

```bash
redis-server
```
## Application Overview
This FastAPI application connects to a local Redis server to store and manage a "current value." The current value is initialized to 0 when the application starts.

The main feature of the app is the ability to perform mathematical operations on this value via a REST API. You can update the current value by sending POST requests with the desired operation.


## Endpoints
**POST** `/update`

This endpoint allows you to update the current value stored in Redis by performing an arithmetic operation (add, subtract, multiply, or divide).

**Request body**:
- `operation`: A string representing the operation to perform. It can be `"add"`, `"subtract"`, `"multiply"`, or `"divide"`.
- `value`: The numeric value to apply to the current value (can be either an integer or a float).
**Example request**:
```
{
  "operation": "add",
  "value": 10
}
```
**Example response**:
```
{
  "current_value": 10.0
}
```
**Possible Errors**:
- If the operation is invalid: 400 Bad Request with a detail message "Invalid operation".
- If trying to divide by zero: 400 Bad Request with a detail message "Cannot divide by zero".

## Running the Application

1. **Build and run the Docker containers**:

In the project directory, run the following command to build and start both the FastAPI and Redis containers:

```bash
docker-compose up --build
```
This will download the necessary Docker images, build your FastAPI app container, and start both the FastAPI app and the Redis service.

2. **Verify the containers are running**:

To verify that both containers are running, use the following command:

```bash
docker-compose ps
```
You should see two containers listed: one for fastapi and one for redis.

## Accessing the Application
Once the containers are running, you can access the FastAPI app via the following URL:

```
http://localhost:8000
```
FastAPI automatically generates interactive documentation for your API. To access the Swagger UI, open your browser and go to:

```bash
http://localhost:8000/docs
```
Alternatively, for ReDoc documentation:

```bash
http://localhost:8000/redoc
```

## Testing the Application
You can test the `/update` endpoint of your FastAPI app using `curl`, Postman, or Swagger UI.

**Example using curl**:
1. To add `10` to the current value:

```bash
curl -X 'POST' \
'http://localhost:8000/update' \
-H 'Content-Type: application/json' \
-d '{
"operation": "add",
"value": 10
}'
```
You should receive a response like this:

```json

{
  "current_value": 10.0
}
```
2. To subtract `5` from the current value:

```bash
curl -X 'POST' \
'http://localhost:8000/update' \
-H 'Content-Type: application/json' \
-d '{
"operation": "subtract",
"value": 5
}'
```
You should receive a response like this:

```json
{
  "current_value": 5.0
}
```




