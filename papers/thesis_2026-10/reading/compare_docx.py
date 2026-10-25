"""Word tracked-changes comparison through LibreOffice (headless). Usage:
    python3 compare_docx.py AFTER.docx BEFORE.docx OUT.docx
Opens AFTER, runs Compare Document against BEFORE, and saves OUT.docx with the differences as tracked changes (insertions and deletions), so that Word can
accept or reject each one. The author of the changes is set to 'Changes 24 to 25 Oct' afterwards by the caller (LibreOffice writes 'Unknown Author').
Build BEFORE from the earlier commit in a separate worktree: git worktree add --detach /tmp/wt <commit>; bash /tmp/wt/papers/thesis_2026-10/reading/build_yzu_docx.sh."""
import subprocess, time, sys, os, zipfile, uno
from com.sun.star.beans import PropertyValue
AFTER, BEFORE, OUT = [os.path.abspath(a) for a in sys.argv[1:4]]
p = subprocess.Popen(["soffice", "--headless", "--invisible", "--norestore", "--accept=socket,host=localhost,port=2002;urp;"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for _ in range(60):
    try:
        local = uno.getComponentContext(); resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"); break
    except Exception: time.sleep(1)
smgr = ctx.ServiceManager; desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
pv = lambda n, v: PropertyValue(Name=n, Value=v)
doc = desktop.loadComponentFromURL("file://" + AFTER, "_blank", 0, (pv("Hidden", True),))
disp = smgr.createInstanceWithContext("com.sun.star.frame.DispatchHelper", ctx)
disp.executeDispatch(doc.getCurrentController().getFrame(), ".uno:CompareDocuments", "", 0, (pv("URL", "file://" + BEFORE), pv("NoAcceptDialog", True)))
time.sleep(3)
n = 0
try:
    n = doc.getRedlines().getCount()
except Exception as e: print("redlines err", e)
print("tracked changes:", n)
doc.storeToURL("file://" + OUT, (pv("FilterName", "MS Word 2007 XML"),))
doc.close(True)
try: desktop.terminate()
except Exception: pass
p.wait(timeout=30)

zin = zipfile.ZipFile(OUT); tmp = OUT + ".tmp"; zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    data = zin.read(it.filename)
    if it.filename.endswith(".xml"): data = data.replace(b'w:author="Unknown Author"', b'w:author="Changes 24 to 25 Oct"')
    zout.writestr(it, data)
zout.close(); zin.close(); os.replace(tmp, OUT)
