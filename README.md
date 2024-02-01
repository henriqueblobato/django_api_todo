# Django API Project

This Django project serves as an API for a Todo application. It provides endpoints for managing Todo items and includes authentication using tokens.

## Project Structure

The project is structured as follows:

- **Settings:** The project settings are configured in `settings.py`. It includes configuration for databases, authentication, and Django Rest Framework.

- **URL Patterns:** The URL patterns are defined in `urls.py`. It includes endpoints for serving API schema documentation (Swagger, Redoc), admin interface, and the main API endpoints.

- **Authentication Token View:** The project includes a custom authentication token view (`CustomAuthToken`) that allows clients to obtain an authentication token by providing a valid username and password. This view is part of the external endpoints.

- **API Endpoints:** The main API endpoints are defined in `api.urls`. It includes a viewset for managing Todo items (`TodoViewSet`).

## Dependencies

- Django: The web framework used for building the API.
- Django Rest Framework: An extension to Django for building RESTful APIs.
- drf_spectacular: A package for generating API schemas and documentation for Django Rest Framework.
- django_filters: A package for filtering querysets in Django.
- python-dotenv: A package for loading environment variables from a .env file.

## Database Configuration

The project supports both local development and production environments. It uses SQLite for local development and PostgreSQL for production. Database configurations can be adjusted in `settings.py`.

## API Documentation

API documentation is generated using `drf_spectacular`. The documentation includes Swagger UI and Redoc interfaces for exploring and understanding the API endpoints.

- Swagger UI: `/api/schema/swagger/`
- Redoc: `/api/schema/redoc/`

## Todo API Endpoints

The API includes endpoints for managing Todo items. The `TodoViewSet` provides CRUD operations for Todo items.

- List all Todo items: `GET /api/todos/`
- Retrieve a Todo item by ID: `GET /api/todos/<id>/`
- Create a new Todo item: `POST /api/todos/`
- Update a Todo item: `PUT /api/todos/<id>/`
- Delete a Todo item: `DELETE /api/todos/<id>/`

## Authentication

The project uses token-based authentication. Clients can obtain an authentication token by sending a POST request to the `/auth/` endpoint with a valid username and password.

- Obtain Token: `POST /auth/`
  - Parameters: `username`, `password`
  - Response: JSON object containing `token`, `user_id`, and `email`

## Running the Project

Before running the project, make sure to set up the necessary environment variables. Create a `.env` file with the required configurations.

To run the project locally:

```bash
  docker compose up --build
```
Access the API at http://127.0.0.1:8000/.

