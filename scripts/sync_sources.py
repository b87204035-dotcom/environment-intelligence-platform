import argparse
from backend.app.db import pool, connection
from backend.app.importer import sync_dataset
parser=argparse.ArgumentParser(); parser.add_argument("--due",action="store_true"); parser.add_argument("dataset_key",nargs="?")
args=parser.parse_args(); pool.open(); pool.wait()
try:
    if args.due:
        with connection() as conn:
            keys=[row[0] for row in conn.execute("""SELECT dataset_key FROM source_datasets d WHERE enabled AND endpoint_url IS NOT NULL AND NOT EXISTS
              (SELECT 1 FROM import_batches b WHERE b.source_dataset_id=d.id AND b.status='succeeded' AND b.completed_at+d.refresh_interval>=now())""")]
        for key in keys: print(sync_dataset(key))
    elif args.dataset_key: print(sync_dataset(args.dataset_key))
    else: parser.error("provide dataset_key or --due")
finally: pool.close()
