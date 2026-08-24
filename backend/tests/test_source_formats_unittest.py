import json
import unittest
from app.source_formats import decode_records
class SourceFormatTests(unittest.TestCase):
    def test_geojson_preserves_official_values(self):
        body={"type":"FeatureCollection","features":[{"properties":{"名稱":"官方紀錄"},"geometry":{"type":"Point","coordinates":[121,24]}}]}
        self.assertEqual(decode_records(json.dumps(body).encode(),"application/geo+json")[0]["名稱"],"官方紀錄")
    def test_csv_preserves_official_values(self):
        self.assertEqual(decode_records("編號,名稱\n1,紀錄\n".encode(),"text/csv"),[{"編號":"1","名稱":"紀錄"}])
if __name__ == "__main__": unittest.main()
