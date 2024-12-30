# onsai python tasks

This repository contains a set of Python tasks designed to assess the skills of candidates applying for a software development role at Onsai. The tasks cover a range of topics, including file processing, object-oriented programming, data manipulation, API interactions, and web development.

---

## Task 1: Text File Analyzer

**Description:**  
Create a Python script that reads the text file romeo-and-juliet and performs the following actions:

- Count the total number of words.
- Count the total number of lines.
- Identify the top 5 most frequently occurring words (excluding common stop words).
- Print the results to the console, neatly formatted.

---

## Task 2: Basic OOP and Inheritance

**Description:**  
Implement an object-oriented solution in Python using a simple class hierarchy:

- Create a base class `Shape` with an attribute `color` and a method `area()` that raises a `NotImplementedError`.
- Implement two subclasses, `Rectangle` and `Circle`, each with their own `area()` methods.
- Instantiate these shapes, set their colors, print their areas, and show how polymorphism allows handling them through a single interface.

---

## Task 3: Data Processing from CSV Files

**Description:**  
Write a Python script that:

- Takes multiple CSV files from a specified directory (e.g., `data/`), each with a consistent schema.
- Merges all the data from these CSV files into a single Pandas DataFrame.
- Performs some aggregation or summary operation (e.g., computing the sum of a particular numeric column or calculating averages grouped by another column).
- Exports the processed results to a new CSV file (e.g., `processed_data.csv`).

---

## Task 4: External API Data Fetch and Transformation

**Description:**  
Create a Python script that:

- Uses the `requests` (or `httpx`) library to call a public REST API endpoint (e.g., a public JSON placeholder or a weather API).
- Parses the returned JSON data and extracts specific information (for example, titles of posts or weather forecast details).
- Transforms this data (e.g., filtering by certain criteria) and prints out a formatted report.

---

## Task 5: FastAPI with Redis and Docker Compose

**Description:**  
Build a FastAPI application with the following features:

- **Initial Value and State Management:**  
  The application maintains a single numeric "current value." Initially, this value should be set to `0`.
  
- **Redis Backend:**  
  Use a Redis database to store and update this current value.
  
- **POST Endpoint (`/update`):**  
  - Accept a JSON payload with two fields:  
    - `operation`: A string that can be `"add"`, `"subtract"`, `"multiply"`, or `"divide"`.
    - `value`: A numeric value to apply using the specified operation.
  - On receiving the request:
    - Read the current value from Redis (initialize it to `0` if it doesn't exist).
    - Perform the specified operation (`current_value = current_value <op> request_value`).
    - Update the current value in Redis.
    - Return the updated current value as JSON in the response.
  
- **Docker Compose Setup:**  
  - Create a `Dockerfile` for the FastAPI application.
  - Use `docker-compose.yaml` to run both the FastAPI service and a Redis service.
  - Ensure that running `docker-compose up` starts both services and the application can connect to Redis.

---