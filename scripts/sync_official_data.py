#!/usr/bin/env python3
"""Download configured official datasets and record auditable sync metadata.

The script never marks a source successful unless bytes were downloaded,
validated, hashed, and written to disk. Dataset URLs are supplied through
`data/source_catalog.json` or environment variables so credentials are not
committed to GitHub.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "source_catalog.json"
RAW_DIR = ROOT / "data" / "raw"
STATUS_PATH = ROOT / "data" / "sync" / "status.json"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_url(source: dict[str, Any]) -> str | None:
    env_name = source.get("download_url_env")
    if env_name and os.getenv(env_name):
        return os.environ[env_name]
    return source.get("download_url")


def sync_source(source: dict[str, Any]) -> dict[str, Any]:
    started_at = now()
    result: dict[str, Any] = {
        "id": source["id"],
        "name": source["name"],
        "started_at": started_at,
        "status": "not_configured",
    }
    url = resolve_url(source)
    if not url:
        result["message"] = "尚未設定官方下載端點或必要金鑰。"
        return result

    try:
        request = urllib.request.Request(url, headers={"User-Agent": "EIP-data-sync/0.1"})
        with urllib.request.urlopen(request, timeout=90) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type", "")
            last_modified = response.headers.get("Last-Modified")

        min_bytes = int(source.get("minimum_bytes", 10))
        if len(body) < min_bytes:
            raise ValueError(f"download too small: {len(body)} bytes")

        suffix = source.get("file_extension", "bin").lstrip(".")
        target = RAW_DIR / source["id"] / f"latest.{suffix}"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body)

        result.update(
            status="success",
            completed_at=now(),
            bytes=len(body),
            sha256=hashlib.sha256(body).hexdigest(),
            content_type=content_type,
            official_last_modified=last_modified,
            output=str(target.relative_to(ROOT)),
        )
    except Exception as exc:  # noqa: BLE001 - audit all connector failures
        result.update(status="failed", completed_at=now(), error=f"{type(exc).__name__}: {exc}")
    return result


def main() -> int:
    catalog = load_json(CATALOG_PATH)
    attempts = [sync_source(source) for source in catalog["sources"] if source.get("enabled", True)]
    status = {
        "minimum_frequency": "monthly",
        "last_attempt_at": now(),
        "status": "success" if attempts and all(x["status"] == "success" for x in attempts) else "partial",
        "sources": attempts,
    }
    save_json(STATUS_PATH, status)
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return 1 if any(x["status"] == "failed" for x in attempts) else 0


if __name__ == "__main__":
    sys.exit(main())
