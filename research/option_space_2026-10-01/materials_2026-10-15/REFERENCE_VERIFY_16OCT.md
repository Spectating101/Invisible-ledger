# Reference verification, 16 October 2026

Scope: `papers/thesis_2026-10/references.md` (64 entries) and in-text citations in `abstract.md`, `ch1`–`ch5`, `drafts/ch6_draft_2026-10-14.md`, `drafts/ch7_draft_2026-10-14.md` and `appendix_notes.md`. Compared against the examined proposal's text (`papers/current/Invisible_Ledger_Thesis_Proposal_CANONICAL_TEXT.md`, lines 1105–1174). No chapter or `references.md` was edited. All URLs were accessed on 2026-10-16.

Note on the count: `grep UNVERIFIED` gives 16 lines, but one is the file's header comment. That leaves **15 flagged entries**. The Grab transcript carries a different note ("Third-party transcript; check...") and is checked here as item 16.

## Summary table

| # | Entry | Status | What changes |
|---|---|---|---|
| 1 | Bank Indonesia (2023), LPI 2022 | VERIFIED | Released 30 Jan 2023. Remove note. |
| 2 | Bank Indonesia (2025), Cerita BI | CORRECTED | Date is 30 Oct 2025. Title has a colon. Add the English translation. |
| 3 | BPS-Statistics Indonesia (2023), Peraturan BPS 4/2023 | VERIFIED | Add the gazette number and a document URL. The PDF's hash matches the repo copy. |
| 4 | Bureau of Internal Revenue (2023), RR 16-2023 | STILL UNVERIFIED | BIR's servers return 403. Facts confirmed from three secondary sources. |
| 5 | Directorate General of Taxes (2026a) | CORRECTED | Found the real title and number: SP-14/2026. |
| 6 | Directorate General of Taxes (2026b) | CORRECTED | Found the real title: Pengumuman PENG-46/PJ.09/2026. Date 5 Aug 2026 confirmed. |
| 7 | Directorate General of Taxes (n.d.) | CORRECTED | Becomes **2025, January 20** (SP-1/2025). The in-text key at ch4:131 must change. |
| 8 | GoTo Gojek Tokopedia (2024b), 2023 annual report | VERIFIED | Public URL found. Its file is byte-identical to the local copy. |
| 9 | GoTo Gojek Tokopedia (2026), 2Q26 call transcript | CORRECTED | Exact title, call date 29 Jul 2026, direct PDF URL. |
| 10 | Government of the Republic of Indonesia (2026), PP 20/2026 | CORRECTED | Full title (the current one is truncated), gazette number, document URL. |
| 11 | Government of Viet Nam (2025), Decree 117/2025/ND-CP | VERIFIED (primary) | Vietnamese title, dates and an official URL added. |
| 12 | Ministry of Trade (2023), Permendag 31/2023 | VERIFIED | Document URL and gazette number. Now revoked by 19/2026. |
| 13 | Ministry of Trade (2026), Permendag 19/2026 | VERIFIED | Document URL, dates and gazette number. |
| 14 | Momentum Works (2024) | STILL UNVERIFIED (primary) | momentum.asia returns 403. Propose citing the Katadata article. A second Momentum Works vintage is used without any reference (see the detail). |
| 15 | United Nations et al. (2025), SNA 2025 | CORRECTED | Five co-issuers, with the European Commission first. This changes the in-text key. Series F No. 2/Rev.6; pre-edit version. |
| 16 | Grab Holdings Limited (2026), Q2 call transcript (not flagged) | CORRECTED (author) | The call date of 3 Aug 2026 (8:00 pm ET) is right. Under APA the transcript's author is Motley Fool Transcribing, not Grab. |

Counts: 6 VERIFIED, 8 CORRECTED, 2 STILL UNVERIFIED (both have a working secondary source). The Grab entry is counted as CORRECTED.

Two in-text keys change if these are applied: ch4:131 `Directorate General of Taxes n.d.` becomes `2025`, and ch2:19 `United Nations et al. 2025` becomes `European Commission et al. 2025`. A third, optional change applies only if Momentum Works is cited through Katadata (ch4:128, ch5:41).

---

## Task 1: per-entry details

### 1. Bank Indonesia (2023): VERIFIED
- Checked: https://www.bi.go.id/id/publikasi/laporan/Pages/LPI_2022.aspx (via WebFetch; curl to bi.go.id gets an empty reply). The listing reads "Laporan Perekonomian Indonesia Tahun 2022", dated 1/30/2023 9:00 AM. The cover PDF (`1_LPI2022_Cover.pdf`) reads "LAPORAN PEREKONOMIAN INDONESIA 2022", ISSN 0522-2572. File metadata gives 27 Jan 2023. The theme is "Sinergi dan Inovasi Memperkuat Ketahanan dan Kebangkitan Menuju Indonesia Maju". The full-PDF URL is listed on that page.
- Replacement (the theme is optional):

> Bank Indonesia. (2023). *Laporan perekonomian Indonesia 2022* [Economic report on Indonesia 2022]. https://www.bi.go.id/id/publikasi/laporan/Documents/LPI_2022.pdf

### 2. Bank Indonesia (2025): CORRECTED
- Checked: the entry's URL via WebFetch. The headline is "Sinergi Jadi Energi: Saat UMKM Naik Kelas Lewat Digitalisasi", dated 10/30/2025 7:00 PM. No author is named; the page credits "Sumber Data: Departemen Komunikasi". The page carries the e-commerce figures: Rp205.5 trillion (2019), Rp487 trillion (2024), and a 2025 projection of Rp738 trillion.
- Replacement:

> Bank Indonesia. (2025, October 30). *Sinergi jadi energi: Saat UMKM naik kelas lewat digitalisasi* [Synergy becomes energy: When small businesses move up through digitalisation] [Cerita BI]. https://www.bi.go.id/id/publikasi/ruang-media/cerita-bi/Pages/Sinergi-Jadi-Energi-Saat-UMKM-Naik-Kelas-Lewat-Digitalisasi.aspx

### 3. BPS-Statistics Indonesia (2023), Peraturan BPS 4/2023: VERIFIED
- Checked: the jdih.bps.go.id download link below (HTTP 200, `Content-Disposition: filename="2023PERBAN004.pdf"`). Its SHA-256 `54856d5e…c998` is identical to `sources/policy_primary/SHA256SUMS.txt`. The text shows it was set on 9 March 2023 and promulgated on 20 March 2023, in Berita Negara 2023 No. 257. The title matches the entry.
- JDIH BPS has no readable detail URL; its links are opaque encrypted tokens. The token below downloaded the document on 16 Oct. Search results also show a BPK mirror, https://peraturan.bpk.go.id/Download/317971/perka-bps-no-4-tahun-2023.pdf, but it returns 403 from this network and was not opened.
- Replacement:

> BPS-Statistics Indonesia. (2023). *Peraturan Badan Pusat Statistik Nomor 4 Tahun 2023 tentang penyampaian dan pengelolaan data dan/atau informasi perdagangan melalui sistem elektronik* [BPS Regulation No. 4 of 2023 on the submission and management of e-commerce data and/or information]. Berita Negara Republik Indonesia Tahun 2023 Nomor 257. https://jdih.bps.go.id/public/dokumen-hukum/download/eyJpdiI6ImFYMEZqVmlad3ptYzNmaFJRNWNmVHc9PSIsInZhbHVlIjoieFh6ZkJIQ28zT1pzTGFEY3JSM3FRZz09IiwibWFjIjoiZjIxNTExYWYzODYxZDMxODg1MzgzZWNiODY0ZTAxZmUyNTAzZTg3MDUyNjc4YjUyOTM5YjEwNjlmMjMwZGE2OSIsInRhZyI6IiJ9

### 4. Bureau of Internal Revenue (2023), RR 16-2023: STILL UNVERIFIED (primary not reachable)
- Tried: `bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2016-2023.pdf` gives 403 through both curl and WebFetch. The `bir.gov.ph/revenue-regulations` page is rendered by JavaScript and has no static link. `officialgazette.gov.ph` gives 403.
- Confirmed from secondary sources:
  - GMA News (Ted Cordero, 29 Dec 2023): issued 21 Dec 2023 and signed by Commissioner Lumagui and Finance Secretary Diokno. It sets a 1% withholding on one-half of gross remittances, with sellers at or below P500,000 exempt.
  - P&A Grant Thornton (14 Jan 2024): published 27 Dec 2023, effective 11 Jan 2024.
  - Baker McKenzie: effective 12 Jan 2024.
  - No source quoted the regulation's full official title. The ch6:107 sentence is supported.
- Replacement (keep the entry and name the secondary source properly):

> Bureau of Internal Revenue. (2023). *Revenue Regulations No. 16-2023* [Issued December 21, 2023]. Republic of the Philippines. [Primary text not retrieved (403); details from Cordero, T. (2023, December 29), BIR subjects online sellers to 1% withholding tax, *GMA News*, https://www.gmanetwork.com/news/money/economy/892606/bir-subjects-online-sellers-to-1-withholding-tax/story/]

- Alternative if the author wants no bracketed caveat: cite the news article itself. The entry would be "Cordero, T. (2023, December 29). BIR subjects online sellers to 1% withholding tax. *GMA News*. [URL above]", and the ch6:107 key would become (Cordero 2023).

### 5. Directorate General of Taxes (2026a): CORRECTED
- Checked: https://www.pajak.go.id/en/node/120146 and its attached PDF (`/sites/default/files/2026-07/SP-14_2026 ...pdf`). The PDF reads "Nomor SP-14/2026", "PEMERINTAH IMPLEMENTASIKAN PMK 37/2025 MELALUI PENUNJUKAN EMPAT MARKETPLACE SEBAGAI PEMUNGUT PPH", with the dateline "Jakarta, 1 Juli 2026". The web page title is the same except it reads "Implementasi" instead of "Implementasikan"; the press release PDF is followed here. It names four marketplaces: Blibli, Shopee, Tokopedia and Lazada.
- Replacement:

> Directorate General of Taxes. (2026a, July 1). *Pemerintah implementasikan PMK 37/2025 melalui penunjukan empat marketplace sebagai pemungut PPh* [Government implements Finance Minister Regulation 37/2025 by designating four marketplaces as income tax collectors] (Press Release No. SP-14/2026). Ministry of Finance of the Republic of Indonesia. https://www.pajak.go.id/en/node/120146

### 6. Directorate General of Taxes (2026b): CORRECTED
- Checked: https://pajak.go.id/en/node/120353 and its PDF (`/sites/default/files/2026-08/Penundaan ... Marketplace.pdf`). The PDF reads "PENGUMUMAN NOMOR PENG-46/PJ.09/2026 TENTANG PENUNDAAN WAKTU PEMBERLAKUAN KETENTUAN PEMUNGUTAN PPH PASAL 22 OLEH MARKETPLACE", "Ditetapkan di Jakarta pada tanggal 5 Agustus 2026", signed by Inge Diana Rismawanti. It postpones the rule to 31 Oct 2026, with collection from 1 Nov 2026.
- Consistency with 2026c, checked: SP-23/2026 says the start was brought forward to 1 Oct 2026 after a re-designation on 24 Sep 2026. The two documents do not contradict each other.
- Replacement:

> Directorate General of Taxes. (2026b, August 5). *Pengumuman Nomor PENG-46/PJ.09/2026 tentang penundaan waktu pemberlakuan ketentuan pemungutan PPh Pasal 22 oleh marketplace* [Announcement No. PENG-46/PJ.09/2026 on postponing marketplace collection of income tax Article 22 to 1 November 2026]. Ministry of Finance of the Republic of Indonesia. https://pajak.go.id/en/node/120353

- Optional, for consistency with 2026a: 2026c is press release No. **SP-23/2026** (from its PDF header), so "(Press Release No. SP-23/2026)" can be added. Its title and date were confirmed.

### 7. Directorate General of Taxes (n.d.): CORRECTED (date found)
- Checked: the entry's URL and its PDF (`/sites/default/files/2025-01/SP-1 PAJAK ATAS USAHA EKONOMI DIGITAL TERKINI RP32,32 TRILIUN.pdf`). It reads "Nomor SP-1/2025", "PAJAK ATAS USAHA EKONOMI DIGITAL TERKINI: 32,32 TRILIUN", "Jakarta, 20 Januari 2025".
- Figures: cumulative to 31 Dec 2024. VAT on foreign digital services (PPN PMSE) is Rp25.35 trillion. 211 collectors had been appointed and 174 had collected.
- Replacement:

> Directorate General of Taxes. (2025, January 20). *Pajak atas usaha ekonomi digital terkini: 32,32 triliun* [Latest tax from the digital economy: Rp32.32 trillion] (Press Release No. SP-1/2025). Ministry of Finance of the Republic of Indonesia. https://pajak.go.id/id/siaran-pers/pajak-atas-usaha-ekonomi-digital-terkini-3232-triliun

- Knock-on changes: ch4:131 changes from `Directorate General of Taxes n.d.` to `Directorate General of Taxes 2025`. In the list, the entry moves before the 2026a–c entries.

### 8. GoTo Gojek Tokopedia (2024b), 2023 annual report: VERIFIED
- Checked: https://gotocompany.com/investor-relations/en/annual-reports lists 2023 "Transformation for Progress" with the PDF below. The downloaded file has SHA-256 `1d1ae560…5003`, byte-identical to `sources/core_public_documents/goto_annual_report_2023.pdf`. It has 505 pages and its PDF was created on 25 Apr 2024. The report is bilingual; the cover reads "Transformasi untuk Kemajuan / Transformation for Progress".
- Replacement:

> GoTo Gojek Tokopedia. (2024b). *2023 annual report: Transformation for progress*. PT GoTo Gojek Tokopedia Tbk. https://content.goinfra.co.id/asts/InvestorRelation/AnnualReport/GOTO_Laporan%20Tahunan_2023.pdf

### 9. GoTo Gojek Tokopedia (2026), 2Q26 call transcript: CORRECTED
- Checked: the quarterly-results page lists "PT GoTo Gojek Tokopedia 2Q26 Earnings Call Transcript", posted 2026-07-31. The PDF's SHA-256 `9d16039a…76cb` matches `sources/manifests/document_manifest.csv`. The transcript names Ministerial Decree 532/2026 and states no date. The call date comes from GoTo's announcement of 15 Jul 2026: "conference call ... on 29 July 2026 at 7:00 PM Jakarta Time". The results press release and presentation are dated 29 Jul 2026.
- Replacement:

> GoTo Gojek Tokopedia. (2026, July 29). *PT GoTo Gojek Tokopedia 2Q26 earnings call transcript* [Transcript]. https://content.goinfra.co.id/asts/InvestorRelation/FinancialInformation/2026-07-31/PT%20GoTo%20Gojek%20Tokopedia%202Q26%20Earnings%20Call%20Transcript.pdf

### 10. Government of the Republic of Indonesia (2026), PP 20/2026: CORRECTED
- Checked: https://jdih.kemenkeu.go.id/dok/pp-20-tahun-2026 (via WebFetch) gives set and promulgated 22 Apr 2026, LNRI 2026 (43), status Berlaku. I downloaded its PDF (https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf, 23 pp.). The text reads "Ditetapkan ... pada tanggal 22 April 2026 / Diundangkan ... pada tanggal 22 April 2026".
- Two other copies exist: a scanned copy at pajak.go.id (`/sites/default/files/2026-06/Peraturan Pemerintah nomor 20 Tahun 2026.pdf`), and the repo copy from jdih.setneg.go.id. They have different file hashes, which is expected for different scans. The Surabaya JDIH gives 21 Apr, but the primary text says 22 Apr.
- jdih.setneg.go.id timed out, so no setneg detail URL could be confirmed.
- The current title in the entry stops after "Nomor 55 Tahun 2022"; the full title continues.
- Replacement:

> Government of the Republic of Indonesia. (2026). *Peraturan Pemerintah Nomor 20 Tahun 2026 tentang perubahan atas Peraturan Pemerintah Nomor 55 Tahun 2022 tentang penyesuaian pengaturan di bidang pajak penghasilan* [Government Regulation No. 20 of 2026 amending Government Regulation No. 55 of 2022 on adjustments to income tax rules]. Lembaran Negara Republik Indonesia Tahun 2026 Nomor 43. https://jdih.kemenkeu.go.id/dok/pp-20-tahun-2026

### 11. Government of Viet Nam (2025), Decree 117/2025/ND-CP: VERIFIED from the primary text
- Checked: https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/6/117-ndcp.signed.pdf, the Government e-portal's signed PDF (23 pp., a scanned image read page by page). It reads:
  - "Số: 117/2025/NĐ-CP", "Hà Nội, ngày 09 tháng 6 năm 2025".
  - Title: "Quy định quản lý thuế đối với hoạt động kinh doanh trên nền tảng thương mại điện tử, nền tảng số của hộ, cá nhân".
  - Art. 13: "có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2025".
  - Signed for the Government by Deputy Prime Minister Hồ Đức Phớc.
- The EY English title is accurate.
- Replacement:

> Government of Viet Nam. (2025). *Nghị định số 117/2025/NĐ-CP quy định quản lý thuế đối với hoạt động kinh doanh trên nền tảng thương mại điện tử, nền tảng số của hộ, cá nhân* [Decree No. 117/2025/ND-CP on tax administration for business activities on e-commerce and digital platforms of households and individuals; issued June 9, 2025; effective July 1, 2025]. https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/6/117-ndcp.signed.pdf

### 12. Ministry of Trade (2023), Permendag 31/2023: VERIFIED
- Checked: the JDIH Kemendag detail page below (via WebFetch). It shows set 25 Sep 2023, promulgated 26 Sep 2023, BN 2023 (763), 29 pp. Its status is "Tidak Berlaku"; it was revoked by Permendag 19/2026. The title matches the entry and the repo text (`sources/policy_primary/Permendag_31_2023_PMSE_full.txt`). The BPK mirror (Details/265202) returns 403.
- Replacement:

> Ministry of Trade of the Republic of Indonesia. (2023). *Peraturan Menteri Perdagangan Nomor 31 Tahun 2023 tentang perizinan berusaha, periklanan, pembinaan, dan pengawasan pelaku usaha dalam perdagangan melalui sistem elektronik* [Trade Minister Regulation No. 31 of 2023 on licensing, advertising, guidance and supervision of businesses in e-commerce]. Berita Negara Republik Indonesia Tahun 2023 Nomor 763. https://jdih.kemendag.go.id/peraturan/peraturan-menteri-perdagangan-nomor-31-tahun-2023-tentang-perizinan-berusaha-periklanan-pembinaan-dan-pengawasan-pelaku-usaha-dalam-perdagangan-melalui-sistem-elektronik-1

### 13. Ministry of Trade (2026), Permendag 19/2026: VERIFIED
- Checked: the JDIH Kemendag detail page below (via WebFetch). It shows set 04 Jun 2026, promulgated 08 Jun 2026, BN 2026 (367), 36 pp., status Berlaku. The title matches the repo text, whose promulgation date is blank in the local copy.
- Replacement:

> Ministry of Trade of the Republic of Indonesia. (2026). *Peraturan Menteri Perdagangan Nomor 19 Tahun 2026 tentang penyelenggaraan usaha perdagangan melalui sistem elektronik* [Trade Minister Regulation No. 19 of 2026 on conducting e-commerce business]. Berita Negara Republik Indonesia Tahun 2026 Nomor 367. https://jdih.kemendag.go.id/peraturan/peraturan-menteri-perdagangan-republik-indonesia-nomor-19-tahun-2026-tentang-penyelenggaraan-usaha-perdagangan-melalui-sistem-elektronik-1

### 14. Momentum Works (2024): STILL UNVERIFIED for the primary; secondary source confirmed
- Tried:
  - https://momentum.asia/insights/detail/ecommerce-in-southeast-asia-2024 and the 16 Jul 2024 press release on thelowdown.momentum.asia: both 403 through curl and WebFetch.
  - beta.momentum.asia: TLS name mismatch.
  - From search snippets only: the report page exists, is listed as July 2024, is paid (US$42.95), and covers 2023 data. Region GMV US$114.6 bn, Indonesia 46.9%, Indonesia growth 3.7%.
- Confirmed live: the Katadata article by Desy Setyowati, 15 Jul 2024, 15:45. It quotes a Momentum Works press statement of Monday 15/7 and lists "Shopee 40% atau US$ 21,52 miliar (Rp 348 triliun)", "Tokopedia 30% atau US$ 16,14 miliar". The Indonesia total is US$53.8 bn. This is the figure in the Shopee row of the ch5 platform table (ch5:37).
- Note: the repo's local file `katadata_momentumworks_indonesia_2023.htm` is a different page. It is a Databoks premium page by Erlina Fury Santika, dated 11 Jan 2025, with the body hidden behind a paywall. It is not the source of the quoted line.
- Option A (APA secondary-source rule): replace the Momentum Works entry with the entry below. In text, write "(Momentum Works, as cited in Setyowati 2024)" at ch4:128 and ch5:41.

> Setyowati, D. (2024, July 15). Transaksi Shopee hingga TikTok Shop Tokopedia di RI Rp 867 triliun [Transactions from Shopee to TikTok Shop Tokopedia in Indonesia reach Rp867 trillion]. *Katadata*. https://katadata.co.id/digital/e-commerce/6694e1bf09ec8/transaksi-shopee-hingga-tiktok-shop-tokopedia-di-ri-rp-867-triliun

- Option B: keep both entries. The Momentum Works entry would read:

> Momentum Works. (2024). *Ecommerce in Southeast Asia 2024* [Report]. https://momentum.asia/insights/detail/ecommerce-in-southeast-asia-2024 [Primary not seen; figures as quoted in Setyowati (2024)]

- **Gap found:** the thesis also uses the **2025 edition** (data for 2024), and no reference covers it. It appears at ch5:231 ("Momentum Works' marketplace estimate of about US$57 billion" for 2024) and in the ch5 Figure 5.3 / Appendix D growth inputs. The repo source is `katadata_momentumworks_indonesia_2024.html`, a live Katadata page: "Kontribusi Indonesia ... US$ 56,5 miliar ... pasar 44%". Proposed entry:

> Setyowati, D. (2025, June 26). Transaksi belanja online di Indonesia melambat, Thailand dan Malaysia melesat [Online shopping in Indonesia slows while Thailand and Malaysia surge]. *Katadata*. https://katadata.co.id/digital/e-commerce/685ba4184c37a/transaksi-belanja-online-di-indonesia-melambat-thailand-dan-malaysia-melesat

### 15. United Nations et al. (2025), SNA 2025: CORRECTED
- Checked:
  - https://unstats.un.org/unsD/nationalaccount/docs/2025_SNA_Pre-edit.pdf (14.5 MB). The title pages list "European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, United Nations, World Bank", "ST/ESA/STAT/SER.F/2/Rev.6", "New York, 2025", "Pre edit version".
  - Crossref (api.crossref.org/works/10.18356/9789211073225): title "System of National Accounts 2025", container "Studies in Methods (Ser. F)", issued 2025-04-23, publisher United Nations.
  - The UN iLibrary says this pre-edited version will be replaced by a final edited one.
- Replacement:

> European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, United Nations, & World Bank. (2025). *System of national accounts 2025* (Pre-edit version; Studies in Methods, Series F, No. 2/Rev.6). United Nations. https://doi.org/10.18356/9789211073225

- Knock-on change: ch2:19 becomes "European Commission et al. 2025", and the entry moves to E in the list. The author may prefer to keep "United Nations et al." for readability, but APA orders authors as the title page does.

### 16. Grab Holdings Limited (2026), not flagged: CORRECTED (author attribution)
- Checked: the AOL URL. Headline "Grab (GRAB) Q2 2026 Earnings Call Transcript", by "Motley Fool Transcribing, The Motley Fool", published 11 Aug 2026 14:15 UTC. The call is "Monday, August 3, 2026 at 8:00 p.m. ET" (4 Aug in Singapore). The quote supports ch6:37: "the 2-wheel taxi business or as we call it Ojol in Indonesia represents 6% of our total mobility GMV" (Alex Hungate).
- Grab's own "Q2 2026 Earnings Prepared Remarks" (investors.grab.com, dated August 4, 2026) do not contain the 6% figure. It was said in Q&A, so no first-party text exists.
- Replacement:

> Motley Fool Transcribing. (2026, August 11). *Grab (GRAB) Q2 2026 earnings call transcript* [Transcript of call held August 3, 2026]. The Motley Fool via AOL. https://www.aol.com/articles/grab-grab-q2-2026-earnings-141515000.html

- If this replacement is used, ch6:37 changes to (Motley Fool Transcribing 2026). Otherwise keep the Grab author and change only the bracket to "[Third-party transcript by The Motley Fool, published August 11, 2026]".

### URL issues found in entries that were not flagged (curl, 16 Oct)
- OECD (2021): the oecd.org PDF URL now redirects to a general topic page. Use https://doi.org/10.1787/8ffb8d09-en instead; Crossref lists "Model Reporting Rules for Digital Platforms", OECD Publishing.
- CNN Indonesia (2026a): the URL redirects to `.../pemerintah-ogah-atur-tarif-admin-shopee-tiktok-shop-usai-seller-ngeluh`. That address matches the cited title, so use it.
- Publisher DOIs (AEA, Wiley, OUP, INFORMS, OECD, UN iLibrary) return 403 to bots. The doi.org redirect itself worked for every DOI, so none is broken. bps.go.id publication pages also returned 403 to curl and were not re-checked.

---

## Task 2: in-text citations and entries

All citation keys were extracted from the nine files (script in the session scratchpad).

**Entries with no in-text citation:** none. All 64 entries are cited at least once.

Three entries are cited only by statute name, not by author-year:
- BPS-Statistics Indonesia 2023 is cited as "BPS Regulation 4/2023" (ch6 table).
- Ministry of Trade 2026 is cited as "Trade Minister Regulation 19/2026" (ch6 table).
- Government of the Republic of Indonesia 2026 is cited as "Government Regulation 20/2026" (ch6 table).

Two more are cited in both forms: Ministry of Finance 2025 ("Finance Minister Regulation 37/2025" in ch6, author-year in ch1 and ch2) and Ministry of Trade 2023 ("Trade Minister Regulation 31/2023" in ch6, author-year in ch1). Under strict APA, a reader cannot match a statute-name citation to the list. Either add the author-year key in the ch6 table or keep the statute names as a deliberate legal-citation style.

**Citations with no reference entry:**
1. ch6 table: "Transport Minister Decree KP-PHB 532/2026" has no entry, and its text is not public. GoTo's 2Q26 transcript is the only document naming it, so cite (GoTo Gojek Tokopedia 2026) in that cell.
2. ch6 table: "Presidential Regulation 27/2026" has no entry, and its text is not public. CNN Indonesia 2026b reports its release, so cite (CNN Indonesia 2026b) in the cell.
3. ch5:231 and Figure 5.3: the Momentum Works 2025 edition (2024 data) is used without any entry. See item 14.
4. ch4:33: "the World Bank's average rate for the year" has no citation. The proposal cited World Bank (2026), WDI PA.NUS.FCRF.
5. ch5:229 and the ch4:130 table: QRIS, e-money and mobile-banking growth have no citation. The proposal cited Bank Indonesia (2025), SPIP/QRIS reports.
6. The header comment in `references.md` already lists the World Bank Enterprise Surveys, LSEG and BPS national accounts as data citations still to add.

**Key-form mismatches:**
- "(AFP 2023)" at ch1:5 does not match the entry "Agence France-Presse", and the abbreviation is never defined. Use "(Agence France-Presse [AFP] 2023)" at first use.
- "BPS 2025a/b" does not match the entry "BPS-Statistics Indonesia". ch1:5 names "BPS" in prose. Either write "(BPS-Statistics Indonesia [BPS] 2025a)" at first use or rename the author in the entry.
- "OECD" is defined at ch2:19 before ch2:27, which is fine.
- "Berg, Burg, Gombovic and Puri" (ch2) vs "Gombović" in the entry: diacritic only.
- "Directorate General of Taxes n.d." becomes 2025, and "United Nations et al." becomes "European Commission et al.", as noted in Task 1.
- Style, for the author to decide once: the chapters use "Author and Author Year" with no comma and list three or four authors in full (e.g., "Givoly, Li, Lourie and Nekrasov 2019"). APA 7 uses "&" and a comma inside parentheses, and "et al." for three or more authors. This matters only if APA is kept; the header notes YZU may switch to numbered citations.

---

## Task 3: comparison with the examined proposal (27 Sep 2026)

The proposal lists 40 references.

### Proposal references the thesis dropped (13)

| Proposal reference | Proposal used it for | Where it would naturally sit in the thesis |
|---|---|---|
| Bank Indonesia (2025). *Payment System Statistics (SPIP) and QRIS reports* | Payment measures | ch4 sources table (ch4:130), ch5:229 (QRIS +187%). Currently uncited. **The thesis reuses the key "Bank Indonesia 2025" for a different document (Cerita BI).** |
| World Bank (2026). *World Development Indicators*: GDP and official exchange rate, Indonesia 2023 | FX at 15,236.88 Rp/US$; GDP magnitude | ch4:33 (FX rule; currently uncited). Any GDP comparison in ch5. |
| Google, Temasek & Bain (2020). *e-Conomy SEA 2020* | US$100 bn (2020) to US$263 bn (2024) | ch1 opening, if that growth sentence returns |
| Business Times (2026). Indonesia's new e-commerce tax mechanism | PMK 37/2025 explainer | ch6 marketplace tax; now covered by primary DGT sources, so not needed |
| De Franco, Kothari & Verdi (2011). Financial statement comparability | Comparable accounting bases for V and R | ch2 finance and accounting section; ch3 (ratio defined on comparable bases); ch4 pair-comparability rules (ch4:33) |
| Barrios, Hochberg & Yi (2022). Gig economy and new business formation | Traces outside conventional records | ch2 (H2: more businesses); ch5 extra-sellers result |
| Denes, Lagaras & Tsoutsoura (2025). Entrepreneurship and the gig economy | Same | Same as above |
| La Porta & Shleifer (2014). Informality and development | Informal-sector evidence is sparse | ch2, beside McKenzie & Paffhausen (2019); ch5 World Bank survey of unregistered firms |
| Ulyssea (2018). Firms, informality, and development | Same | Same |
| Medina & Schneider (2019). Shadow economy database | Same | Same; also ch7 limitations if the size of informality is mentioned |
| Kleven, Kreiner & Saez (2016). Why can modern governments tax so much? | Third-party reporting | ch2 table row 2.3 "Third-party information" beside Kleven et al. 2011 and Naritomi 2019; ch6 |
| Slemrod (2019). Tax compliance and enforcement | Same | Same |
| Parker & Van Alstyne (2005). Two-sided network effects | Platform pricing literature | ch2 two-sided markets line (Rochet & Tirole; Armstrong; Evans & Schmalensee) |

### Shared entries whose details differ

| Entry | Proposal | Thesis | Comment |
|---|---|---|---|
| Bank Indonesia 2025 | SPIP and QRIS payment reports | Cerita BI article "Sinergi jadi energi..." | **Different document under the same key.** Decide whether both are needed. If so, use 2025a and 2025b. |
| BPS 2025 | One entry: "E-Commerce Statistics 2023 and 2024" (English) | Two entries: 2025a and 2025b, Indonesian titles with translation and URLs | The thesis is more correct (two publications: 30 Jan 2025 and 28 Nov 2025) |
| GoTo 2024 | One press release, 19 Mar 2024 | 2024a (same press release) plus 2024b (annual report) | Consistent |
| Ministry of Finance 2025 | "PMK 37 Tahun 2025; Directorate General of Taxes marketplace guidance" (combined) | PMK 37/2025 only; DGT documents listed separately | The thesis is cleaner |
| Momentum Works 2024 | *Ecommerce in Southeast Asia*. Singapore: Momentum Works. | *Ecommerce in Southeast Asia 2024* (no publisher, note) | Title adds "2024"; see item 14 |
| Google, Temasek & Bain 2024 | "e-Conomy SEA 2024: Profits on the Rise" | Adds ", harnessing SEA's advantage" plus a URL | Subtitle only |
| Caillaud & Jullien 2003 | "Chicken and egg" | "Chicken & egg" | The journal title uses "&", so the thesis is right |
| Berg et al. 2020 | Gombovic; "Review of Financial Studies" | Gombović; "The Review of Financial Studies" | Diacritic and article only |
| Armstrong 2006 / Caillaud & Jullien 2003 | "RAND Journal of Economics" | "The RAND Journal of Economics" | Article only |
| United Nations et al. 2025 | Title only | Adds series and DOI | Both need the co-issuer fix (item 15) |
| Hagiu & Wright 2015; La Porta & Shleifer 2014 | "162174", "109126" | n/a | Page-range hyphens lost in the proposal's text extraction; not a real difference |

All other shared entries match on year, title and journal: Ahmad & Schreyer; EU 2021; Evans & Schmalensee; Givoly et al.; Henderson et al.; Hummels & Klenow; IASB; IMF; Kleven et al. 2011; Mann & Whitney; Naritomi; OECD 2020 and 2023; Pomeranz; Rajgopal et al.; Rochet & Tirole; Trueman et al. 2001. The thesis has 37 entries that are not in the proposal; they are not listed here.

### Checks not completed
- jdih.setneg.go.id (timeout), peraturan.bpk.go.id (403), bir.gov.ph CDN (403), officialgazette.gov.ph (403) and momentum.asia (403) were unreachable. bi.go.id and jdih.kemendag.go.id were reachable only through WebFetch, not curl.
- No Google cache was used. Hash checks were run against the repo's SHA256SUMS and document manifests where a local copy existed.
