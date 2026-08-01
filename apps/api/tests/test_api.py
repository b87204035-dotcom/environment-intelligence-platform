from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get('/health')
    assert response.status_code == 200
    body = response.json()
    assert body['status'] == 'ok'
    assert body['service'] == 'eip-api'


def test_location_requires_valid_coordinates() -> None:
    response = client.post('/v1/location/resolve', json={
        'mode': 'gps',
        'latitude': 25.033,
        'longitude': 121.5654,
    })
    assert response.status_code == 200
    assert response.json()['status'] == 'pending_official_connector'


def test_articles_8_9_returns_analysis_lists() -> None:
    response = client.post('/v1/regulations/articles-8-9/assess', json={
        'business_name': '某電鍍工廠',
        'industry_keywords': ['電鍍'],
        'processes': ['金屬表面處理'],
        'chemicals': ['鉻酸'],
    })
    assert response.status_code == 200
    body = response.json()
    assert 'potential_pollutants' in body
    assert 'recommended_analysis' in body
    assert body['legal_disclaimer']


def test_data_sources_has_minimum_frequency() -> None:
    response = client.get('/v1/data-sources')
    assert response.status_code == 200
    assert response.json()['minimum_sync_frequency'] == 'monthly'
