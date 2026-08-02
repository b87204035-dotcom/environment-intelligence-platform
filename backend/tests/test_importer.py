import json
from app.source_formats import decode_records
from app.importer import validate_official_url

def test_decodes_geojson_without_inventing_properties():
    body={"type":"FeatureCollection","features":[{"type":"Feature","properties":{"名稱":"官方紀錄"},"geometry":{"type":"Point","coordinates":[121,24]}}]}
    assert decode_records(json.dumps(body).encode(),"application/geo+json") == [{"名稱":"官方紀錄","_geometry":{"type":"Point","coordinates":[121,24]}}]
def test_decodes_utf8_csv():
    assert decode_records("編號,名稱\n1,紀錄\n".encode(),"text/csv") == [{"編號":"1","名稱":"紀錄"}]
def test_rejects_non_government_endpoint():
    try: validate_official_url("https://example.com/data")
    except ValueError as exc: assert "gov.tw" in str(exc)
    else: raise AssertionError("unreviewed domain accepted")
