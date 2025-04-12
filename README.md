![Automated Tests](https://github.com/JosefLeinweber/JosefsFastAPITemplate/workflows/Automated%20Tests/badge.svg)

# JosefsFastAPITemplate

## Overview

JosefsFastAPITemplate is a boilerplate repository designed to help developers quickly set up a FastAPI project. It provides a structured foundation for building scalable and maintainable web applications using Python and FastAPI.

## Key Features

- **FastAPI Integration**: Pre-configured FastAPI setup for rapid development.
- **Modular Structure**: Organized folder structure for easy scalability.
- **Environment Configuration**: Support for `.env` files to manage environment variables.
- **Dependency Management**: Uses `pip` for managing dependencies.
- **Docker Support**: Includes a `Dockerfile` and `docker-compose` for containerized deployment.
- **Testing Ready**: Pre-configured testing setup using `pytest`.
- **Pre-commit Hooks**: Automates code formatting, linting, and testing before committing changes.
- **Interactive API Documentation**: Swagger UI and Redoc for exploring and testing API endpoints.
- **Database Management**: Adminer for managing development and test databases through a web interface.
- **Continuous Integration (CI)**: GitHub Actions pipeline for automated testing and building.

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

    Access the following services:
    - **Swagger UI**: `http://localhost:8000/docs`
    - **Redoc**: `http://localhost:8000/redoc`
    - **Dev DB Adminer**: `http://localhost:8081`
    - **Test DB Adminer**: `http://localhost:8082`

3. Stop the services:
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
- `feature/*`
- `fix/*`
- `refactor/*`

And on every pull request to:
- `trunk`

The pipeline performs the following tasks:
- Building Docker images for the application and database services.
- Running tests inside the Docker container.

To enable the CI pipeline:
1. Ensure you have a GitHub repository set up for your project.
2. Upload the variables of the `.env` file to the GitHub repository variables using the `upload_env_variables.py` script:
    ```bash
    python upload_env_variables.py
    ```

## Folder Structure

The repository is organized as follows:

- **backend/**: Contains the main application code.
  - **src/**: Source code for the FastAPI application.
    - **api/**: API endpoints and routes.
      - **routes/**: Specific route handlers, e.g., `account_router.py`.
    - **config/**: Configuration files for different environments.
      - **settings/**: Environment-specific settings, e.g., `development.py`, `production.py`.
    - **crud/**: CRUD operations, e.g., `account_crud.py`.
    - **models/**: Database models and schemas.
      - **db_tables/**: Database table definitions, e.g., `account_table.py`.
      - **schemas/**: Pydantic schemas for data validation, e.g., `account_schema.py`.
    - **utility/**: Utility modules for various functionalities.
      - **database/**: Database-related utilities, e.g., `db_session.py`.
      - **events/**: Event handlers, e.g., `event_handlers.py`.
      - **formatters/**: Formatting utilities, e.g., `date_time.py`.
      - **pydantic_schema/**: Base schemas for Pydantic models.
  - **tests/**: Unit and integration tests.
    - **router_tests/**: Tests for API routes, e.g., `test_account_router.py`.

- **docker-compose.yml**: Docker Compose configuration file.
- **example.env**: Example environment variables file.
- **README.md**: Project documentation.
- **upload_env_variables.py**: Script to upload environment variables to GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
