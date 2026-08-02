from html.parser import HTMLParser
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).parents[1]
DOCS = ROOT / "docs"

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if "id" in attrs: self.ids.append(attrs["id"])
        for key in ("href", "src"):
            value=attrs.get(key, "")
            if value and not value.startswith(("http://", "https://", "#")): self.refs.append(value)

class StaticSiteTests(unittest.TestCase):
    def test_local_assets_exist_and_ids_are_unique(self):
        parser=PageParser(); parser.feed((DOCS/"index.html").read_text())
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        for ref in parser.refs:
            self.assertTrue((DOCS/ref).exists(), ref)
    def test_manifest_is_valid_and_scoped(self):
        manifest=json.loads((DOCS/"manifest.webmanifest").read_text())
        self.assertEqual(manifest["start_url"], "./")
        self.assertEqual(manifest["display"], "standalone")
    def test_service_worker_shell_files_exist(self):
        source=(DOCS/"sw.js").read_text()
        for asset in ("index.html", "assets/app.css", "assets/app.js", "manifest.webmanifest"):
            self.assertIn(asset, source); self.assertTrue((DOCS/asset).exists())

if __name__ == "__main__": unittest.main()
