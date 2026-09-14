#!/usr/bin/env python3
"""Bounded public-input export; never include private files or arbitrary directories."""
from pathlib import Path
import base64
import gzip
import hashlib
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from longitudinal_review import FILES
root=Path(__file__).resolve().parents[2]
files={p:(root/p).read_bytes().decode('utf-8') for p in FILES}
payload=gzip.compress(json.dumps(files,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode(),mtime=0)
print('PUBLIC_REVIEW_TEXT_SHA256='+hashlib.sha256(payload).hexdigest())
encoded=base64.b64encode(payload).decode()
for i in range(0,len(encoded),3000):print(f'PUBLIC_REVIEW_TEXT_{i//3000:03d}='+encoded[i:i+3000])
