[![Automated Tests](https://github.com/JosefLeinweber/JosefsFastAPITemplate/actions/workflows/automated_tests.yml/badge.svg?branch=trunk)](https://github.com/JosefLeinweber/JosefsFastAPITemplate/actions/workflows/automated_tests.yml)# JosefsFastAPITemplate

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

2. Set up environment variables:
    Create a `.env` file in the root directory and configure your environment variables.


### Running with Docker Compose

1. Build the Docker images:
    ```bash
    docker-compose build
    ```

2. Start the services:
    ```bash
    ENVIRONMENT=DEV docker-compose up
    ```

    This will start the FastAPI application and the database services defined in the `docker-compose.yml` file in a DEV environment.

- **Swagger UI**: Access the interactive API documentation at       `http://localhost:8000/docs`.
- **Redoc**: Access the alternative API documentation at            `http://localhost:8000/redoc`.
- **Dev DB Adminer**: Access the database admin interface at        `http://localhost:8081`.
- **Test DB Adminer**: Access the test database admin interface at  `http://localhost:8082`.

3. Stop the services:
    To stop the running containers, press `CTRL+C` or run:
    ```bash
    docker-compose down
    ```

### Running Tests in Docker

1. Ensure the Docker containers are running in STAGING environment:
    ```bash
    ENVIRONMENT=STAGING docker-compose up
    ```

2. Run the tests inside the Docker container:
    ```bash
    docker exec -it <container_name> pytest
    ```

### Using Pre-commit

Pre-commit helps to ensure that your code meets certain standards before committing.
Pre-commit hooks can automatically format your code, check for linting errors, and run tests before you commit changes to your repository.

1. Install pre-commit hooks:
    ```bash
    pre-commit install
    ```
2. Run pre-commit manually:
    ```bash
    pre-commit run --all-files
    ```

### Continuous Integration (CI)

This repository includes a CI pipeline that runs on GitHub Actions. The pipeline is triggered on every push to:
- feature/*
- fix/*
- refactor/*
And on every pull request to:
- trunk

The pipeline performs the following tasks:
- Building the Docker images for the application and database services, based on the docker-compose.yml file.
- Running the tests inside the Docker container.

To enable the CI pipeline:
1. Ensure you have a GitHub repository set up for your project.
2. Upload the variables of the .env file to the GitHub repository variables with the upload_env_variables.py script
    - Ensure you have Github CLI installed and authenticated.
    - Run the script with the command:
        ```bash
        python upload_env_variables.py
        ```

## Folder Structure
