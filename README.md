# 🐳 Python Application Containerized with Docker

This project is a simple Python application packaged and run using Docker. It demonstrates how to containerize a Python app, manage dependencies, and create a consistent runtime environment using Docker.

---

# 📌 Project Overview

This project shows how to take a standard Python application and run it inside a Docker container.

Instead of installing Python and dependencies manually on every machine, Docker ensures the application runs the same way everywhere.

It demonstrates:

- Building a Docker image from a Python app
- Installing dependencies using `requirements.txt`
- Running a Python script inside a container
- Creating reproducible environments using Docker

---

# 🧱 Tech Stack

- Python 3.9 (slim image)
- Docker
- pip (Python dependency manager)

---

# 📂 Project Structure

```bash
.
├── app.py               # Main Python application
├── requirements.txt     # List of dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation
