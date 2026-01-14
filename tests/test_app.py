import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test that home endpoint returns API information"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'api_name' in data
    assert 'version' in data
    assert 'description' in data
    assert 'endpoints' in data
    assert 'available_categories' in data
    assert data['api_name'] == 'Product API'


def test_health_endpoint(client):
    """Test that health endpoint returns healthy status"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'status': 'healthy'}


def test_products_endpoint(client):
    """Test that products endpoint returns all products"""
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Check that all products have required fields
    for product in data:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product
        assert 'brand' in product
        assert 'specs' in product
        assert 'category' in product


def test_products_by_category_tv(client):
    """Test products by category endpoint for TV"""
    response = client.get('/products/tv')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    for product in data:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product
        assert 'brand' in product
        assert 'specs' in product


def test_products_by_category_mobile(client):
    """Test products by category endpoint for Mobile"""
    response = client.get('/products/mobile')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    for product in data:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product
        assert 'brand' in product
        assert 'specs' in product


def test_products_by_category_laptop(client):
    """Test products by category endpoint for Laptop"""
    response = client.get('/products/laptop')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    for product in data:
        assert 'id' in product
        assert 'name' in product
        assert 'price' in product
        assert 'brand' in product
        assert 'specs' in product


def test_products_by_category_invalid(client):
    """Test products by category endpoint with invalid category"""
    response = client.get('/products/invalid')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_specific_product_tv(client):
    """Test specific product endpoint for TV"""
    response = client.get('/product/tv/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert data['name'] == 'Samsung 55-inch QLED TV'
    assert 'price' in data
    assert 'brand' in data
    assert 'specs' in data


def test_specific_product_mobile(client):
    """Test specific product endpoint for Mobile"""
    response = client.get('/product/mobile/2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 2
    assert data['name'] == 'Samsung Galaxy S24'
    assert 'price' in data
    assert 'brand' in data
    assert 'specs' in data


def test_specific_product_laptop(client):
    """Test specific product endpoint for Laptop"""
    response = client.get('/product/laptop/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert data['name'] == 'MacBook Pro 14-inch'
    assert 'price' in data
    assert 'brand' in data
    assert 'specs' in data


def test_specific_product_invalid_category(client):
    """Test specific product endpoint with invalid category"""
    response = client.get('/product/invalid/1')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_specific_product_invalid_id(client):
    """Test specific product endpoint with invalid ID"""
    response = client.get('/product/tv/999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_categories_endpoint(client):
    """Test that categories endpoint returns all categories"""
    response = client.get('/categories')
    assert response.status_code == 200
    data = response.get_json()
    assert 'categories' in data
    assert 'count' in data
    assert isinstance(data['categories'], list)
    assert len(data['categories']) == 3
    assert 'tv' in data['categories']
    assert 'mobile' in data['categories']
    assert 'laptop' in data['categories']
    assert data['count'] == 3
