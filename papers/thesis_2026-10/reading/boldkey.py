"""Bolds the key sentences listed in keypoints.txt, for the compact reading copy only. Reads Markdown on stdin, writes it to stdout.
Each line of keypoints.txt must occur exactly once in the text; otherwise the build stops and names the line, so an edit to a chapter
cannot silently drop or duplicate a highlight. The thesis text itself is never changed."""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
keys = [l.rstrip("\n") for l in open(os.path.join(here, "keypoints.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
text = sys.stdin.read()
bad = [k for k in keys if text.count(k) != 1]
if bad:
    for k in bad:
        sys.stderr.write(f"keypoint found {text.count(k)} times (need 1): {k[:90]}\n")
    sys.exit(1)
for k in keys:
    text = text.replace(k, "**" + k + "**")
sys.stdout.write(text)
