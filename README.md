# Flask Products API

A RESTful API built with Flask for managing products across different categories (TV, Mobile, Laptop). The application includes Docker support, comprehensive testing, and CI/CD setup.

## Features

- **RESTful API** with multiple endpoints for product management
- **Product Categories**: TV, Mobile, and Laptop
- **Docker Support** with optimized Dockerfile
- **Testing** with pytest
- **CI/CD Ready** with Procfile for deployment
- **CORS Enabled** for cross-origin requests

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /health` - Health check endpoint
- `GET /products` - Get all products from all categories
- `GET /products/<category>` - Get products by category (tv, mobile, laptop)
- `GET /product/<category>/<id>` - Get a specific product by category and ID
- `GET /categories` - Get all available categories

## Product Categories

### TV
- Samsung 55-inch QLED TV
- LG 65-inch OLED TV
- Sony 43-inch LED TV

### Mobile
- iPhone 15 Pro
- Samsung Galaxy S24
- Google Pixel 8

### Laptop
- MacBook Pro 14-inch
- Dell XPS 15

## Installation

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will run on `http://localhost:5002`

### Docker

1. Build the Docker image:
```bash
docker build -t flask-app .
```

2. Run the container:
```bash
docker run -d -p 5002:5002 --name flask-app-container flask-app
```

3. Access the API at `http://localhost:5002`

## Testing

Run the test suite using pytest:
```bash
pytest tests/test_app.py
```

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Process file for deployment
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── .gitignore           # Git ignore file
└── tests/
    └── test_app.py      # Test suite
```

## Technologies Used

- **Flask 3.0.0** - Web framework
- **Flask-CORS 4.0.0** - Cross-origin resource sharing
- **Gunicorn 21.2.0** - WSGI HTTP Server
- **Pytest 7.4.3** - Testing framework
- **Python 3.11** - Programming language

## License

This project is open source and available for use.
