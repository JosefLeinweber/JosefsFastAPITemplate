# JosefsFastAPITemplate

## Overview

JosefsFastAPITemplate is a boilerplate repository designed to help developers quickly set up a FastAPI project. It provides a structured foundation for building scalable and maintainable web applications using Python and FastAPI.

## Features

- **FastAPI Integration**: Pre-configured FastAPI setup for rapid development.
- **Modular Structure**: Organized folder structure for easy scalability.
- **Environment Configuration**: Support for `.env` files to manage environment variables.
- **Dependency Management**: Uses `pip` for managing dependencies.
- **Docker Support**: Includes a `Dockerfile` and `docker-compose` for containerized deployment.
- **Testing Ready**: Pre-configured testing setup using `pytest`.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` or `poetry` for dependency management
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/JosefsFastAPITemplate.git
    cd JosefsFastAPITemplate
    ```

2. Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

3. Set up environment variables:
    Create a `.env` file in the root directory and configure your environment variables.


### Running with Docker Compose

1. Build the Docker images:
    ```bash
    docker-compose build
    ```

2. Start the services:
    ```bash
    docker-compose up
    ```

3. Stop the services:
    To stop the running containers, press `CTRL+C` or run:
    ```bash
    docker-compose down
    ```

### Dev Routes

- **Swagger UI**: Access the interactive API documentation at       `http://localhost:8000/docs`.
- **Redoc**: Access the alternative API documentation at            `http://localhost:8000/redoc`.
- **Dev DB Adminer**: Access the database admin interface at        `http://localhost:8081`.
- **Test DB Adminer**: Access the test database admin interface at  `http://localhost:8082`.

## Folder Structure
