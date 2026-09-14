# -*- coding: utf-8 -*-
import re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import sys as _sys
# Optional argv override so compression candidates can be rendered without editing the script:
#   build_proposal_docx.py [source.md] [output.docx]
SRC_MD=(_sys.argv[1] if len(_sys.argv)>1 else
        '/home/phyrexian/Downloads/Invisible-ledger/docs/PROPOSAL_MERGED_CANDIDATE_2026-09-14.md')
REPO='/home/phyrexian/Downloads/Invisible-ledger/'
# The template still lives in the sibling working directory; the output must land in
# the repo, or a rebuild silently leaves papers/current/ stale.
TPL=REPO+'papers/reference/Invisible_Ledger_Proposal_FLASHPOINT_GRAFT_PLAIN_FINAL_2026-09-13.docx'
OUT=(_sys.argv[2] if len(_sys.argv)>2 else
     REPO+'papers/current/Invisible_Ledger_Thesis_Proposal_FINAL_2026-09-14.docx')
TITLE_ZH="隱形帳簿：量化印尼平台經濟中的隱形楔子"
TITLE_EN="The Invisible Ledger: Quantifying the Invisible Wedge in Indonesia's Platform Economy"

md=open(SRC_MD,encoding='utf8').read()
md=md.split('## Abstract',1)[1]
md='## Abstract'+md
md=md.split('## Compression notes')[0]
md=md.split('## Change log against')[0]          # drop change log + verification from the proposal body
md=md.split('## Verification status')[0]

def clean(t):
    t=re.sub(r'\*\*(.+?)\*\*',r'\1',t); t=re.sub(r'\*(.+?)\*',r'\1',t)
    t=re.sub(r'`(.+?)`',r'\1',t); t=re.sub(r'~~.+?~~','',t)
    t=re.sub(r'←.*$','',t); t=re.sub(r'\[RESTORED[^\]]*\]','',t); t=re.sub(r'\[CORRECTED\]','',t)
    return ' '.join(t.split())

blocks=[]; lines=md.split('\n'); i=0
while i<len(lines):
    l=lines[i].rstrip()
    if l.startswith('|'):
        tb=[]
        while i<len(lines) and lines[i].lstrip().startswith('|'):
            row=[clean(c) for c in lines[i].strip().strip('|').split('|')]
            if not all(set(c)<=set('-: ') for c in row): tb.append(row)
            i+=1
        if tb: blocks.append(('TBL',tb)); continue
    if l.startswith('### '): blocks.append(('H2',clean(l[4:])))
    elif l.startswith('## '): blocks.append(('H1',clean(l[3:])))
    elif l.startswith('> '):  blocks.append(('EQ',clean(l[2:])))
    elif l.startswith('---') or not l.strip(): pass
    else: blocks.append(('P',clean(l)))
    i+=1

d=Document(TPL); body=d.element.body
def st(p,t):
    for r in p.runs[1:]: r._element.getparent().remove(r._element)
    if p.runs: p.runs[0].text=t
ps=d.paragraphs; st(ps[5],TITLE_ZH); st(ps[6],TITLE_EN)
for ch in list(body.iterchildren())[14:]:
    if not ch.tag.endswith('}sectPr'): body.remove(ch)
sect=body.find(qn('w:sectPr'))
def add(style=None):
    p=d.add_paragraph(style=style) if style else d.add_paragraph()
    body.remove(p._element); sect.addprevious(p._element); return p
def fmt(p,size=12,bold=None,italic=None,align=WD_ALIGN_PARAGRAPH.JUSTIFY,sa=3,sb=0,keep=False):
    pf=p.paragraph_format; pf.space_after=Pt(sa); pf.space_before=Pt(sb); pf.line_spacing=1.15
    p.alignment=align
    if keep: pf.keep_with_next=True
    for r in p.runs:
        r.font.name='Times New Roman'; r.font.size=Pt(size); r.font.color.rgb=RGBColor(0,0,0)
        if bold is not None: r.font.bold=bold
        if italic is not None: r.font.italic=italic
        rpr=r._element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
        if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
        for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')
def para(t,**kw):
    style=kw.pop('style',None); p=add(style); p.add_run(t); fmt(p,**kw); return p
def table(rows,size=9.5):
    n=len(rows[0]); t=d.add_table(rows=1,cols=n); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    trPr=t.rows[0]._tr.get_or_add_trPr(); th=OxmlElement('w:tblHeader'); th.set(qn('w:val'),'true'); trPr.append(th)
    trPr.append(OxmlElement('w:cantSplit'))
    for _p in t.rows[0].cells[0].paragraphs: _p.paragraph_format.keep_with_next=True
    def cell(c,txt,bold):
        c.text=''; p=c.paragraphs[0]; p.add_run(txt)
        fmt(p,size=size,bold=bold,align=WD_ALIGN_PARAGRAPH.LEFT,sa=1,sb=1)
    for j,h in enumerate(rows[0]): cell(t.rows[0].cells[j],h,True)
    small = len(rows) <= 7          # keep short tables whole on one page
    for ri,row in enumerate(rows[1:],1):
        tr=t.add_row(); tr._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        for j,v in enumerate(row[:n]): cell(tr.cells[j],v,False)
        if small and ri < len(rows)-1:
            for _c in tr.cells:
                for _p in _c.paragraphs: _p.paragraph_format.keep_with_next=True
    body.remove(t._tbl); sect.addprevious(t._tbl)

for kind,val in blocks:
    if kind=='H1':  para(val,style='Heading 1',size=13,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT,sb=9,sa=4,keep=True)
    elif kind=='H2':para(val,style='Heading 2',size=12,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT,sb=6,sa=2,keep=True)
    elif kind=='EQ':para(val,align=WD_ALIGN_PARAGRAPH.CENTER,italic=True,sb=4,sa=5)
    elif kind=='TBL':table(val); para('',size=5,sa=0)
    else:
        if val.startswith('Table '): para(val,size=9.5,italic=True,align=WD_ALIGN_PARAGRAPH.LEFT,sb=7,sa=2,keep=True)
        else: para(val)
import sys as _s; _s.path.insert(0, REPO+'scripts/proposal_content')
from content import REFS, PRIM_HEAD, PRIM_NOTE, PRIM
para('References',style='Heading 1',size=13,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT,sb=9,sa=4,keep=True)
for _r in REFS:
    _p=para(_r,size=11,sa=1); _p.paragraph_format.left_indent=Pt(18); _p.paragraph_format.first_line_indent=Pt(-18)
para(PRIM_HEAD,style='Heading 1',size=13,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT,sb=6,sa=3,keep=True)
para(PRIM_NOTE,size=11,sa=3)
# Keep the source list together; at sa=2 its last two entries orphaned onto a page of their own.
for _i,_r in enumerate(PRIM):
    _p=para(_r,size=11,sa=1); _p.paragraph_format.left_indent=Pt(18); _p.paragraph_format.first_line_indent=Pt(-18)
    # (no keep_with_next: forcing the block together only moved the stub page)

for s in d.sections:
    for c in (s.header,s.footer):
        for p in c.paragraphs:
            for r in p.runs:
                r.font.name='Times New Roman'; r.font.color.rgb=RGBColor(0,0,0)
                rpr=r._element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
                if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
                for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')
d.save(OUT); print('saved', OUT.split('/')[-1], '|', len(blocks), 'blocks,', len(d.tables), 'tables')
