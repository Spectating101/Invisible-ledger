"""OCR image-only operational tables; output is unverified extraction, not raw data."""
from pathlib import Path
import json,subprocess
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parent/'broad_archive';OUT=ROOT/'ocr';OUT.mkdir(exist_ok=True)
records=json.loads((ROOT/'manifest.json').read_text())
todo=[r for r in records if r.get('module')=='blibli' and 'Earnings-Release' in r['url'] and r.get('text_file') and len((ROOT/r['text_file']).read_text())<500]
def run(r):
    name=Path(r['file']).stem;prefix=OUT/name
    subprocess.run(['pdftoppm','-f','2','-l','2','-r','220','-png','-singlefile',str(ROOT/r['file']),str(prefix)],check=True,capture_output=True)
    subprocess.run(['tesseract',str(prefix)+'.png',str(prefix),'-l','eng','--psm','6'],check=True,capture_output=True)
    return dict(source_file=r['file'],source_url=r['url'],pdf_page=2,image=str(prefix.relative_to(ROOT))+'.png',ocr_text=str(prefix.relative_to(ROOT))+'.txt',status='OCR UNVERIFIED; source image must be checked before numeric use')
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(run,todo))
(OUT/'ocr_manifest.json').write_text(json.dumps(rows,indent=2));print('OCR table pages',len(rows))
