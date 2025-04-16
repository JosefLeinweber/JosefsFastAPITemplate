![Automated Tests](https://github.com/JosefLeinweber/JosefsFastAPITemplate/workflows/Automated%20Tests/badge.svg)

# FastAPITemplate

## Overview

FastAPITemplate is a production-ready boilerplate repository designed to help developers quickly set up a FastAPI project. It provides a structured foundation for building scalable, secure, and maintainable web applications using Python and FastAPI with best practices baked in.

This template is built on [FastAPI](https://fastapi.tiangolo.com/), a modern Python web framework for building APIs with automatic interactive documentation. It incorporates asynchronous database access, environment-based configuration, Docker containerization, and robust testing capabilities.

## Key Features

- 🚀 **FastAPI Integration**: Pre-configured FastAPI setup for rapid development
- ⚡ **Asynchronous Architecture**: Built with async/await for high-performance, non-blocking I/O
- 🧩 **Modular Structure**: Organized folder structure for easy scalability and maintenance
- 🔧 **Environment Configuration**: Support for `.env` files to manage environment variables across different environments
- 🗄️ **Database Integration**: Asynchronous PostgreSQL support with SQLAlchemy
- 🐳 **Docker Support**: Includes `Dockerfile` and `docker-compose.yml` for containerized deployment
- 🧪 **Testing Ready**: Pre-configured testing setup using `pytest`
- 🔄 **Pre-commit Hooks**: Automates code formatting, linting, and testing before committing changes
- 📚 **Interactive API Documentation**: Swagger UI and Redoc for exploring and testing API endpoints
- 🛢️ **Database Management**: Adminer for managing development and test databases through a web interface
- 🔄 **Continuous Integration (CI)**: GitHub Actions pipeline for automated testing and building
- 🔒 **Security Features**: Password strength validation, CORS configuration, secure database connections
- ✅ **Type Safety**: Leverages Python type hints and Pydantic for data validation

## Table of Contents
- [FastAPITemplate](#fastapitemplate)
  - [Overview](#overview)
  - [Key Features](#key-features)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running with Docker Compose](#running-with-docker-compose)
    - [Running Tests in Docker](#running-tests-in-docker)
    - [Using Pre-commit](#using-pre-commit)
    - [Continuous Integration (CI)](#continuous-integration-ci)
  - [Project Architecture](#project-architecture)
    - [Folder Structure](#folder-structure)
    - [Core Components](#core-components)
      - [FastAPI Application](#fastapi-application)
      - [Configuration System](#configuration-system)
      - [Database Architecture](#database-architecture)
      - [API Layer](#api-layer)
      - [Schema Management](#schema-management)
      - [CRUD Operations](#crud-operations)
      - [Event Handling](#event-handling)
  - [Building Scalable Applications](#building-scalable-applications)
    - [Scalability Considerations](#scalability-considerations)
    - [Scaling Strategies](#scaling-strategies)
  - [Security and Privacy Features](#security-and-privacy-features)
  - [Environment Configuration](#environment-configuration)
  - [Docker \& Containerization](#docker--containerization)
  - [Development Workflow](#development-workflow)
  - [Testing Approach](#testing-approach)
  - [Deployment Best Practices](#deployment-best-practices)
  - [Using This Template for Your Project](#using-this-template-for-your-project)
  - [Best Practices](#best-practices)
  - [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` or `poetry` for dependency management
- Docker (optional, for containerized deployment)
- PostgreSQL (if not using Docker)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/FastAPITemplate.git
    cd FastAPITemplate
    ```

2. Set up environment variables:
    - Copy the `example.env` file to `.env`
    - Configure your environment variables in the `.env` file

3. If not using Docker, install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

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

This repository includes a CI pipeline that runs on GitHub Actions. The pipeline is triggered on every pull request to:
- `trunk`

If only changes to .md files are made, the pipeline will return a success status without running the tests.

The pipeline performs the following tasks:
- Building Docker images for the application and database services
- Running tests inside the Docker container

To enable the CI pipeline:
1. Ensure you have a GitHub repository set up for your project
2. Upload the variables of the `.env` file to the GitHub repository variables using the `upload_env_variables.py` script:
    ```bash
    python upload_env_variables.py
    ```

## Project Architecture

### Folder Structure

The repository is organized as follows:

```
backend/
├── src/                          # Main application source code
│   ├── main.py                   # Application entry point
│   ├── api/                      # API layer
│   │   ├── endpoints.py          # API endpoint registry
│   │   └── routes/               # Individual route modules
│   │       └── account_router.py # Account-related routes
│   ├── config/                   # Configuration modules
│   │   ├── logging.py            # Logging configuration
│   │   └── settings/             # Environment-based settings
│   │       ├── base.py           # Base settings class
│   │       ├── development.py    # Development environment settings
│   │       ├── production.py     # Production environment settings
│   │       ├── setup.py          # Settings initialization
│   │       └── staging.py        # Staging environment settings
│   ├── crud/                     # CRUD operation modules
│   │   └── account_crud.py       # Account CRUD operations
│   ├── models/                   # Data models
│   │   ├── db_tables/            # SQLAlchemy table definitions
│   │   │   ├── account_table.py  # Account table definition
│   │   │   └── table_collection.py # Table registry
│   │   └── schemas/              # Pydantic schemas
│   │       ├── account_schema.py # Account data schemas
│   │       └── profile_schema.py # Profile data schemas
│   └── utility/                  # Utility modules
│       ├── database/             # Database utilities
│       ├── events/               # Event handlers
│       ├── formatters/           # Formatting utilities
│       └── pydantic_schema/      # Base Pydantic schemas
├── tests/                        # Test directory
│   ├── conftest.py               # Pytest configuration
│   └── router_tests/             # API route tests
├── Dockerfile                    # Docker configuration
└── requirements.txt              # Python dependencies
```

### Core Components

#### FastAPI Application

The application is initialized in `main.py` with a modular approach that allows for clean setup of middleware, event handlers, and route registration. The app configuration is loaded from environment-specific settings.

```python
def initialize_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_backend_app_attributes)
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    
    # Event handlers
    app.add_event_handler("startup", execute_backend_server_event_handler(app=app))
    app.add_event_handler("shutdown", terminate_backend_server_event_handler(app=app))
    
    # Router registration
    app.router.include_router(router)
    
    return app
```

#### Configuration System

The application uses a hierarchical settings system based on Pydantic to manage configuration across different environments. The base settings class (`base.py`) defines common settings, while environment-specific subclasses override values as needed.

Settings are loaded from `.env` files, making it easy to manage environment variables. The system supports multiple environments:

- Development (local development)
- Staging (testing environment)
- Production (live environment)

This approach allows for consistent configuration management with type validation and default values.

#### Database Architecture

The database architecture follows a modern, asynchronous approach using SQLAlchemy's async features:

1. **Database Class**: A singleton `Database` class manages the connection to the PostgreSQL database.
2. **Async Engine & Session**: The database uses asynchronous connections for non-blocking I/O.
3. **Connection Pooling**: Configurable connection pooling for efficient resource utilization.
4. **Session Management**: Dependency injection for proper session lifecycle management.

```python
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.async_session() as session:
        try:
            yield session
        except Exception as exception:
            loguru.logger.error(f"Exception in async session: {exception}")
            await session.rollback()
            raise
```

#### API Layer

The API layer is organized by domain with versioning:

1. **Base Router**: (`endpoints.py`) - Sets up API versioning with prefixes.
2. **Domain Routers**: Separate router modules for different domains (e.g., `account_router.py`).
3. **Endpoint Documentation**: Each endpoint includes OpenAPI documentation with response models and status codes.

Example endpoint from `account_router.py`:

```python
@router.post(
    path="",
    name="account:create_account",
    response_model=AccountOut,
    status_code=201,
)
async def create_account(
    new_account: AccountInAuthentication,
    db_session: SQLAlchemyAsyncSession = fastapi.Depends(get_async_session),
) -> AccountOut:
    # Implementation...
```

#### Schema Management

Data validation and serialization are handled through Pydantic schemas:

1. **Base Schema**: Common validation logic in base schema classes.
2. **Input Schemas**: Schemas for data coming into the API (e.g., `AccountInAuthentication`).
3. **Output Schemas**: Schemas for responses returned to clients (e.g., `AccountOut`).
4. **Validation Logic**: Custom validators for business rules (e.g., password strength).

```python
class AccountInAuthentication(AccountBase):
    password: str

    @pydantic.validator("password")
    def password_strength(cls, v):
        policy = PasswordPolicy.from_names(
            length=8,
            uppercase=1,
            numbers=1,
            special=1,
        )
        if policy.test(v) != []:
            raise ValueError("Password is not strong enough")
        return v
```

#### CRUD Operations

CRUD (Create, Read, Update, Delete) operations are separated into dedicated modules for each entity type, providing a clean interface for database operations:

1. **Entity-Specific Modules**: Each entity has its own CRUD module (e.g., `account_crud.py`).
2. **Error Handling**: Proper error handling with appropriate HTTP exceptions.
3. **Transaction Management**: Automatic transaction management with rollback on error.

Each CRUD function is asynchronous and follows a consistent pattern:

```python
async def create(account: AccountInAuthentication, db_session: SQLAlchemyAsyncSession) -> Account:
    # Implementation with error handling...
```

#### Event Handling

The application uses event handlers for initialization and cleanup operations:

1. **Server Startup**: Database connection initialization, logging setup.
2. **Server Shutdown**: Graceful connection termination and resource cleanup.

Event handlers are registered in the main application factory and modularized for maintainability.

## Building Scalable Applications

### Scalability Considerations

The template is built with scalability in mind:

1. **Asynchronous Architecture**: Non-blocking I/O for handling large numbers of concurrent connections.
2. **Database Connection Pooling**: Configurable connection pool size and overflow settings.
3. **Modular Design**: Clean separation of concerns for easier horizontal scaling.
4. **Docker Containerization**: Simplified deployment to container orchestration platforms.
5. **Environment-Based Configuration**: Easy adaptation to different deployment environments.

### Scaling Strategies

The application's architecture supports several scaling strategies:

- **Vertical Scaling**: Configure worker count and resource limits
- **Horizontal Scaling**: Deploy multiple instances behind a load balancer
- **Database Scaling**: Connection pooling and potential sharding
- **Microservices Evolution**: Domain-based routers can evolve into separate microservices

For large scale deployments, consider:

1. **Load Balancing**: Deploy multiple instances behind a load balancer (e.g., Nginx, Traefik)
2. **Container Orchestration**: Use Kubernetes or Docker Swarm for managing multiple containers
3. **Database Replication**: Set up read replicas to distribute database load
4. **Caching**: Implement Redis or Memcached for caching frequently accessed data
5. **CDN Integration**: Use a Content Delivery Network for static assets

## Security and Privacy Features

The template incorporates several security features:

1. **Password Strength Validation**: Enforces strong passwords with specific requirements
2. **CORS Configuration**: Prevents cross-origin request forgery by configuring allowed origins, methods, and headers
3. **Database Connection Security**: Secure database connection handling
4. **Input Validation**: Strict schema validation prevents malformed input
5. **Error Handling**: Prevents leaking sensitive information in error responses

To enhance security and privacy further, consider implementing:

- **JWT-based Authentication**: Secure user authentication using JSON Web Tokens
- **Role-based Access Control**: Restrict access to resources based on user roles
- **Rate Limiting**: Prevent abuse by limiting request rates
- **Input Sanitization**: Sanitize user inputs to prevent injection attacks
- **Data Encryption**: Encrypt sensitive data at rest and in transit
- **Audit Logging**: Log access and changes to sensitive data
- **GDPR Compliance**: Implement features for user data management and deletion
- **HTTPS**: Always use HTTPS in production with proper SSL/TLS configuration

## Environment Configuration

Environment variables are managed through `.env` files with support for different deployment environments:

1. **Base Settings**: Common settings across all environments
2. **Environment-Specific Override**: Development, staging, and production environments
3. **Configuration Validation**: Type checking and validation through Pydantic

Key configuration categories include:

- Server settings (host, port, workers)
- Database connection parameters
- CORS settings
- Logging configuration
- Feature flags

## Docker & Containerization

The template includes Docker configuration for containerized deployment:

1. **Dockerfile**: Multi-stage build process for optimized images
2. **Docker Compose**: Local development setup with database and admin services
3. **Environment Variables**: Docker-compatible environment variable management

Services defined in Docker Compose:

- Application server
- PostgreSQL database
- Adminer for database management

## Development Workflow

The template supports a productive development workflow:

1. **Local Development**: Docker Compose for local development environment
2. **Hot Reload**: Automatic server reloading for code changes
3. **Testing**: Pre-configured testing with pytest
4. **Pre-commit Hooks**: Code formatting, linting, and testing before commits
5. **API Documentation**: Interactive API documentation with Swagger UI and ReDoc

## Testing Approach

The testing approach covers multiple levels:

1. **Unit Tests**: Testing individual components in isolation
2. **Integration Tests**: Testing component interactions
3. **API Tests**: Testing HTTP endpoints
4. **Test Database**: Separate database for testing to avoid development data pollution

Tests are organized by domain and run automatically in the CI pipeline.

## Deployment Best Practices

For production deployments, follow these best practices:

1. **Environment Configuration**: Use production-specific settings
2. **Database Security**: Use strong passwords, restrict network access
3. **Worker Configuration**: Set appropriate number of workers based on server resources
4. **Logging**: Configure proper logging for monitoring and debugging
5. **Backup Strategy**: Implement regular database backups
6. **Monitoring**: Set up health checks and performance monitoring
7. **CI/CD Pipeline**: Automate deployment process
8. **Blue-Green Deployment**: Minimize downtime with blue-green deployment strategy

## Using This Template for Your Project

To use this template for a new project:

1. **Clone the Repository**: Start with a fresh copy of the template
2. **Configure Environment**: Set up environment variables in `.env` file
3. **Define Your Models**: Create database models in `models/db_tables/`
4. **Create Schemas**: Define Pydantic schemas in `models/schemas/`
5. **Implement CRUD**: Add CRUD operations in the `crud/` directory
6. **Create API Routes**: Add new routes in `api/routes/`
7. **Register Routes**: Register new routers in `api/endpoints.py`
8. **Write Tests**: Add tests for new functionality in `tests/`
9. **Deploy**: Use Docker to deploy your application

## Best Practices

The template encourages several best practices:

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Dependency Injection**: Facilitates testing and component substitution
3. **Error Handling**: Comprehensive error handling with appropriate status codes
4. **Logging**: Structured logging for monitoring and debugging
5. **Environment-Based Configuration**: Different settings for different environments
6. **Database Migration**: Planned support for Alembic migrations
7. **Testing**: Comprehensive test coverage for reliability
8. **Documentation**: Self-documenting API with OpenAPI integration
9. **Type Safety**: Leveraging Python type hints for better code quality

By following these best practices, you can build robust, maintainable web applications that scale efficiently and securely.


## Acknowledgments
- [Aeternails Ingenium](https://github.com/Aeternalis-Ingenium): For the original FastAPI template that inspired this project.
