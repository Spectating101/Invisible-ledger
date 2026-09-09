#!/usr/bin/env python3
"""Export only the explicitly named public CSVs used by the review (not secrets or caches)."""
from pathlib import Path
import base64
import gzip
import hashlib
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from longitudinal_review import FILES
root=Path(__file__).resolve().parents[2]
files={p:base64.b64encode((root/p).read_bytes()).decode() for p in FILES}
payload=gzip.compress(json.dumps(files,sort_keys=True,separators=(',',':')).encode(),mtime=0)
print('PUBLIC_REVIEW_INPUTS_SHA256='+hashlib.sha256(payload).hexdigest())
encoded=base64.b64encode(payload).decode()
for i in range(0,len(encoded),3000):
    print(f'PUBLIC_REVIEW_INPUTS_{i//3000:03d}='+encoded[i:i+3000])
