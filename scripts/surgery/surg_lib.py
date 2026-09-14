# -*- coding: utf-8 -*-
import copy, datetime, io, os
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AUTHOR="Christopher Ongko"
DATE=datetime.datetime(2026,9,14,9,0,0).strftime('%Y-%m-%dT%H:%M:%SZ')
# Revision ids must be unique across the WHOLE document, but the surgery runs as
# several stage scripts in separate processes, each re-importing this module. An
# in-memory counter therefore restarts every stage and emits duplicates, and Word
# groups revisions by id -- so accepting one change would accept several unrelated
# ones. Back the counter with a file in the build directory so it survives.
_CTR_FILE=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.revision_counter')
def _id():
    try:
        with io.open(_CTR_FILE, encoding='utf8') as f: n=int(f.read().strip())
    except (IOError, OSError, ValueError):
        n=9000
    n+=1
    with io.open(_CTR_FILE, 'w', encoding='utf8') as f: f.write(str(n))
    return str(n)

COMMENT_TAGS={qn('w:commentRangeStart'), qn('w:commentRangeEnd')}

def _mk_run(text, rpr):
    r=OxmlElement('w:r')
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t=OxmlElement('w:t'); t.set(qn('xml:space'),'preserve'); t.text=text
    r.append(t); return r

def _mk_delrun(text, rpr):
    r=OxmlElement('w:r')
    if rpr is not None: r.append(copy.deepcopy(rpr))
    t=OxmlElement('w:delText'); t.set(qn('xml:space'),'preserve'); t.text=text
    r.append(t); return r

_run=lambda text, rpr=None: _mk_run(text,rpr)
_delrun=lambda text, rpr=None: _mk_delrun(text,rpr)

def _wrap(tag, children):
    e=OxmlElement('w:'+tag)
    e.set(qn('w:id'),_id()); e.set(qn('w:author'),AUTHOR); e.set(qn('w:date'),DATE)
    for c in children: e.append(c)
    return e

def first_rpr(p):
    for r in p.findall(qn('w:r')):
        rpr=r.find(qn('w:rPr'))
        if rpr is not None: return rpr
    return None

def _run_map(p):
    """[(start,end,rPr)] over the paragraph's visible text, plus the text itself."""
    segs=[]; buf=[]; pos=0
    for r in p.findall(qn('w:r')):
        txt=''.join(t.text or '' for t in r.findall(qn('w:t')))
        if not txt: continue
        rpr=r.find(qn('w:rPr'))
        segs.append((pos,pos+len(txt),rpr)); buf.append(txt); pos+=len(txt)
    return ''.join(buf), segs

def _emit_formatted(text, start, segs, fallback):
    """Re-emit `text` (which lies at offset `start` in the original) preserving per-run rPr."""
    if start < 0:
        return [_mk_run(text, fallback)]
    out=[]; cur=start; end=start+len(text)
    for s,e,rpr in segs:
        if e<=cur or s>=end: continue
        a=max(s,cur); b=min(e,end)
        if b>a:
            out.append(_mk_run(text[a-start:b-start], rpr)); cur=b
    if cur<end: out.append(_mk_run(text[cur-start:], fallback))
    return out or [_mk_run(text, fallback)]

def _stash_comments(p):
    """Detach comment anchors/references so a rebuild cannot destroy them."""
    pre=[]; post=[]
    for ch in list(p):
        if ch.tag in COMMENT_TAGS:
            (pre if ch.tag==qn('w:commentRangeStart') else post).append(ch); p.remove(ch)
        elif ch.tag==qn('w:r') and ch.find(qn('w:commentReference')) is not None:
            post.append(ch); p.remove(ch)
    return pre, post

def rebuild(p, segs):
    """segs: [('keep'|'del'|'ins', text)] -> tracked runs, preserving formatting and comments."""
    orig_text, runmap = _run_map(p)
    fallback = first_rpr(p)
    pre, post = _stash_comments(p)
    ppr=p.find(qn('w:pPr'))
    for ch in list(p):
        if ch is not ppr: p.remove(ch)
    cursor=0
    for kind,txt in segs:
        if not txt: continue
        if kind in ('keep','del'):
            at=orig_text.find(txt, cursor)
            if at<0: at=orig_text.find(txt)
            if at>=0: cursor=at+len(txt)
            if kind=='keep':
                for r in _emit_formatted(txt, at, runmap, fallback): p.append(r)
            else:
                rpr=fallback
                for s,e,rp in runmap:
                    if at>=0 and s<=at<e: rpr=rp; break
                p.append(_wrap('del',[_mk_delrun(txt,rpr)]))
        else:
            p.append(_wrap('ins',[_mk_run(txt,fallback)]))
    # restore comment anchors: start before content, end+reference after
    for e in reversed(pre):
        p.insert(1 if ppr is not None else 0, e)
    for e in post: p.append(e)
    return p

def del_paragraph(p):
    rpr=first_rpr(p)
    orig_text,_=_run_map(p)
    pre,post=_stash_comments(p)
    ppr=p.find(qn('w:pPr'))
    if ppr is None:
        ppr=OxmlElement('w:pPr'); p.insert(0,ppr)
    prpr=ppr.find(qn('w:rPr'))
    if prpr is None:
        prpr=OxmlElement('w:rPr'); ppr.append(prpr)
    dm=OxmlElement('w:del')
    dm.set(qn('w:id'),_id()); dm.set(qn('w:author'),AUTHOR); dm.set(qn('w:date'),DATE)
    prpr.insert(0,dm)
    for ch in list(p):
        if ch is not ppr: p.remove(ch)
    for e in reversed(pre): p.insert(1,e)
    if orig_text: p.append(_wrap('del',[_mk_delrun(orig_text,rpr)]))
    for e in post: p.append(e)
    return p

def new_paragraph(doc_body, style, segs, after):
    p=OxmlElement('w:p')
    ppr=OxmlElement('w:pPr')
    if style:
        st=OxmlElement('w:pStyle'); st.set(qn('w:val'),style); ppr.append(st)
    prpr=OxmlElement('w:rPr')
    ins=OxmlElement('w:ins')
    ins.set(qn('w:id'),_id()); ins.set(qn('w:author'),AUTHOR); ins.set(qn('w:date'),DATE)
    prpr.append(ins); ppr.append(prpr)
    p.append(ppr)
    for kind,txt in segs:
        if kind=='ins': p.append(_wrap('ins',[_mk_run(txt,None)]))
        else: p.append(_mk_run(txt,None))
    after.addnext(p)
    return p

def accept_existing(body):
    for d in body.findall('.//'+qn('w:del')):
        par=d.getparent()
        if par is not None: par.remove(d)
    for i in body.findall('.//'+qn('w:ins')):
        par=i.getparent(); idx=list(par).index(i)
        for ch in list(i): par.insert(idx,ch); idx+=1
        par.remove(i)

__all__=['AUTHOR','DATE','_id','_run','_delrun','_wrap','first_rpr','rebuild',
         'del_paragraph','new_paragraph','accept_existing']
