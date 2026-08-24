"""Pure decoding helpers for exact official-source payloads."""
import csv
import io
import json

def decode_records(content: bytes, content_type: str) -> list[dict]:
    text=content.decode("utf-8-sig")
    if "csv" in content_type:
        return list(csv.DictReader(io.StringIO(text)))
    payload=json.loads(text)
    if isinstance(payload,list):
        return payload
    if payload.get("type") == "FeatureCollection":
        return [{**feature.get("properties",{}),"_geometry":feature.get("geometry")} for feature in payload.get("features",[])]
    for key in ("records","result","data"):
        if isinstance(payload.get(key),list):
            return payload[key]
    raise ValueError("Endpoint response does not contain a supported record collection")
