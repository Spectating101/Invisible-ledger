#!/usr/bin/env python3
"""Build a definition-aware global e-commerce corroboration module.

The reviewed source transcriptions below pair each issuer's own annual
transaction measure with a revenue measure from the same reported perimeter.
They are not country observations and are not pooled with the proposed
Indonesia main sample. Cross-issuer comparisons are descriptive because GMV,
GMS, GTV and revenue definitions differ materially by business model.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "global_ecommerce"
FIGURES = ROOT / "reports" / "figures"


def row(
    issuer: str,
    segment: str,
    region: str,
    year: int,
    transaction_metric: str,
    transaction_value: float,
    revenue_metric: str,
    revenue_value: float,
    currency: str,
    unit: str,
    source_url: str,
    source_file: str,
    source_locator: str,
    precision: str,
    scope_break: str = "no",
    scope_note: str = "",
    transaction_definition: str = "",
    revenue_definition: str = "",
) -> dict[str, object]:
    return locals()


ROWS = [
    # eBay: transaction value is inclusive of shipping and taxes and is not
    # adjusted for returns/cancellations; revenue is consolidated net revenue.
    row("eBay", "Marketplace", "Global", 2020, "GMV", 100000, "net_revenue", 10271, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2021/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-and-Full-Year-2020-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2020_results.html", "Full Year Financial Highlights and income statement", "GMV rounded to USD0.1bn; revenue USD1m", "yes",
        "2020/2021 comparisons were affected by the eBay Korea disposal and continuing-operations presentation.",
        "Paid marketplace transactions including shipping and taxes, before returns/cancellations.", "Consolidated net revenue."),
    row("eBay", "Marketplace", "Global", 2021, "GMV", 87400, "net_revenue", 10420, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2022/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-and-Full-Year-2021-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2021_results.html", "Full Year Financial Highlights and income statement", "GMV rounded to USD0.1bn; revenue USD1m", "yes",
        "eBay Korea disposal; do not treat the 2020-2021 transition as a clean perimeter comparison.",
        "Paid marketplace transactions including shipping and taxes, before returns/cancellations.", "Consolidated net revenue from continuing operations."),
    row("eBay", "Marketplace", "Global", 2022, "GMV", 73900, "net_revenue", 9795, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2023/eBay-Inc.-Reports-Better-Than-Expected-Fourth-Quarter-2022-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2022_results.html", "Full Year Financial Highlights and income statement", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Paid marketplace transactions including shipping and taxes, before returns/cancellations.", revenue_definition="Consolidated net revenue."),
    row("eBay", "Marketplace", "Global", 2023, "GMV", 73200, "net_revenue", 10112, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2024/eBay-Inc.-Reports-Fourth-Quarter-and-Full-Year-2023-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2023_results.html", "Full Year Financial Highlights and income statement", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Paid marketplace transactions including shipping and taxes, before returns/cancellations.", revenue_definition="Consolidated net revenue."),
    row("eBay", "Marketplace", "Global", 2024, "GMV", 74700, "net_revenue", 10283, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2025/eBay-Inc.-Reports-Fourth-Quarter-and-Full-Year-2024-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2024_results.html", "Full Year Financial Highlights and income statement", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Paid marketplace transactions including shipping and taxes, before returns/cancellations.", revenue_definition="Consolidated net revenue."),
    row("eBay", "Marketplace", "Global", 2025, "GMV", 79600, "net_revenue", 11100, "USD", "million",
        "https://investors.ebayinc.com/investor-news/press-release-details/2026/eBay-Inc--Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx",
        "sources/global_ecommerce/raw/ebay/ebay_fy2025_results.html", "Full Year 2025 Financial Highlights; income statement; GMV footnote", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Paid marketplace transactions including shipping and taxes, before returns/cancellations.", revenue_definition="Consolidated net revenue."),

    # Etsy consolidated marketplace portfolio. Acquisition/disposal years are
    # preserved but excluded from clean-transition summaries.
    row("Etsy", "Consolidated marketplaces", "Global", 2019, "GMS", 4974.944, "total_revenue", 818.379, "USD", "million",
        "https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-21-000009/exhibit99112312020.htm",
        "sources/global_ecommerce/raw/etsy/etsy_fy2020_results.htm", "Fourth Quarter and Full Year 2020 Financial Summary, 2019 comparative", "USD0.001m",
        transaction_definition="Dollar value of items sold excluding shipping, net of refunds.", revenue_definition="Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2020, "GMS", 10281.101, "total_revenue", 1725.625, "USD", "million",
        "https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-21-000009/exhibit99112312020.htm",
        "sources/global_ecommerce/raw/etsy/etsy_fy2020_results.htm", "Fourth Quarter and Full Year 2020 Financial Summary", "USD0.001m",
        transaction_definition="Dollar value of items sold excluding shipping, net of refunds.", revenue_definition="Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2021, "GMS", 13491.828, "total_revenue", 2329.114, "USD", "million",
        "https://investors.etsy.com/news-events/press-releases/detail/64/etsy-inc-reports-fourth-quarter-and-full-year-2021-results",
        "sources/global_ecommerce/raw/etsy/etsy_fy2021_results.html", "Full-year financial metrics table", "USD0.001m", "yes",
        "Depop and Elo7 entered consolidated results from their July 2021 acquisition dates.",
        "Dollar value of items sold excluding shipping, net of refunds.", "Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2022, "GMS", 13318.396, "total_revenue", 2566.111, "USD", "million",
        "https://investors.etsy.com/news-events/press-releases/detail/29/etsy-inc-reports-fourth-quarter-and-full-year-2023-results",
        "sources/global_ecommerce/raw/etsy/etsy_fy2023_results.html", "Full-year table, FY2022 comparative", "USD0.001m",
        transaction_definition="Dollar value of items sold excluding shipping, net of refunds.", revenue_definition="Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2023, "GMS", 13161.196, "total_revenue", 2748.377, "USD", "million",
        "https://investors.etsy.com/news-events/press-releases/detail/29/etsy-inc-reports-fourth-quarter-and-full-year-2023-results",
        "sources/global_ecommerce/raw/etsy/etsy_fy2023_results.html", "Full-year financial metrics table", "USD0.001m", "yes",
        "Elo7 included only through its 10 August 2023 sale date.",
        "Dollar value of items sold excluding shipping, net of refunds.", "Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2024, "GMS", 12586.952, "total_revenue", 2808.332, "USD", "million",
        "https://investors.etsy.com/news-events/press-releases/detail/13/etsy-inc-reports-fourth-quarter-and-full-year-2024-results",
        "sources/global_ecommerce/raw/etsy/etsy_fy2024_results.html", "Full-year financial metrics table", "USD0.001m",
        transaction_definition="Dollar value of items sold excluding shipping, net of refunds.", revenue_definition="Marketplace plus services revenue."),
    row("Etsy", "Consolidated marketplaces", "Global", 2025, "GMS", 11916.900, "total_revenue", 2883.501, "USD", "million",
        "https://investors.etsy.com/sec-filings/all-sec-filings/content/0001370637-26-000019/etsy-20251231.htm",
        "sources/global_ecommerce/raw/etsy/etsy_fy2025_10k.htm", "10-K performance metrics table", "USD0.001m", "yes",
        "Reverb was sold on 30 April 2025 and contributes only through the sale date.",
        "Dollar value of items sold excluding shipping, net of refunds.", "Marketplace plus services revenue."),

    # Shopify includes online, offline/POS and B2B commerce facilitated by its
    # infrastructure; revenue includes subscriptions and merchant solutions.
    row("Shopify", "Commerce platform", "Global", 2019, "GMV", 61100, "total_revenue", 1578.0, "USD", "million",
        "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2019-financial-results", "sources/global_ecommerce/raw/shopify/shopify_fy2019_results.html", "Full-Year Financial Highlights", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2020, "GMV", 119600, "total_revenue", 2929.5, "USD", "million",
        "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2020-financial-results",
        "sources/global_ecommerce/raw/shopify/shopify_fy2020_results.html", "Full-Year Financial Highlights", "GMV rounded to USD0.1bn; revenue USD0.1m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2021, "GMV", 175361.814, "total_revenue", 4611.856, "USD", "million",
        "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2021-financial-results",
        "sources/global_ecommerce/raw/shopify/shopify_fy2021_results.html", "Full-year highlights; exact later comparative in FY2022 SEC exhibit", "USD0.001m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2022, "GMV", 197166.882, "total_revenue", 5599.864, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1594805/000159480523000008/exhibit991pressreleaseq420.htm",
        "sources/global_ecommerce/raw/shopify/shopify_fy2022_results.html", "SEC Exhibit 99.1, years-ended performance and revenue tables", "USD0.001m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2023, "GMV", 235910, "total_revenue", 7060, "USD", "million",
        "https://www.shopify.com/news/shopify-announces-fourth-quarter-and-full-year-2023-financial-results",
        "sources/global_ecommerce/raw/shopify/shopify_fy2023_results.html", "FY2024 annual-report comparative table", "USD1m", "yes",
        "Shopify sold most logistics businesses in May 2023; reported revenue growth differs from comparable-basis growth.",
        "Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", "Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2024, "GMV", 292275, "total_revenue", 8880, "USD", "million",
        "https://www.shopify.com/investors/press-releases/shopify-merchant-success-powers-q4-outperformance-across-both-top-and-bottom-line",
        "sources/global_ecommerce/raw/shopify/shopify_fy2024_annual_report.pdf", "Selected Business Performance Information", "USD1m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),
    row("Shopify", "Commerce platform", "Global", 2025, "GMV", 378441, "total_revenue", 11556, "USD", "million",
        "https://s27.q4cdn.com/572064924/files/doc_financials/2025/q4/Shopify_Investor_Press_Release_Q4-25_FINAL.pdf",
        "sources/global_ecommerce/raw/shopify/shopify_fy2025_results.pdf", "PDF p.1, Selected Business Performance Information", "USD1m",
        transaction_definition="Orders facilitated through Shopify, net of refunds, including shipping, duties and VAT.", revenue_definition="Subscription solutions plus merchant solutions."),

    # Jumia's total revenue deliberately includes first-party sales. The
    # definition map explains why this is not comparable to a pure marketplace
    # commission rate.
    row("Jumia", "E-commerce group", "Africa", 2021, "GMV", 990.6, "total_revenue", 177.934, "USD", "million",
        "https://s205.q4cdn.com/370993272/files/doc_news/2023/02/1/JMIA-Q4-22-ER-16-02-23-vF.pdf",
        "sources/global_ecommerce/raw/jumia/jumia_fy2022_results.pdf", "FY2022 PDF pp.8-9, FY2021 comparative", "GMV USD0.1m; revenue USD0.001m",
        transaction_definition="Orders for products/services including shipping and VAT, before discounts, cancellations and returns.", revenue_definition="Marketplace, first-party and other revenue."),
    row("Jumia", "E-commerce group", "Africa", 2022, "GMV", 1047.6, "total_revenue", 221.882, "USD", "million",
        "https://s205.q4cdn.com/370993272/files/doc_news/2023/02/1/JMIA-Q4-22-ER-16-02-23-vF.pdf",
        "sources/global_ecommerce/raw/jumia/jumia_fy2022_results.pdf", "FY2022 PDF pp.8-9", "GMV USD0.1m; revenue USD0.001m",
        transaction_definition="Orders for products/services including shipping and VAT, before discounts, cancellations and returns.", revenue_definition="Marketplace, first-party and other revenue."),
    row("Jumia", "E-commerce group", "Africa", 2023, "GMV", 749.8, "total_revenue", 186.402, "USD", "million",
        "https://investor.jumia.com/files/doc_financials/2024/q4/Jumia-EX-99-1-Q4-2024_v02192025-v4.pdf",
        "sources/global_ecommerce/raw/jumia/jumia_fy2024_results.pdf", "FY2024 PDF full-year comparative tables", "GMV USD0.1m; revenue USD0.001m",
        transaction_definition="Orders for products/services including shipping and VAT, before discounts, cancellations and returns.", revenue_definition="Marketplace, first-party and other revenue."),
    row("Jumia", "E-commerce group", "Africa", 2024, "GMV", 720.6, "total_revenue", 167.486, "USD", "million",
        "https://investor.jumia.com/files/doc_financials/2024/q4/Jumia-EX-99-1-Q4-2024_v02192025-v4.pdf",
        "sources/global_ecommerce/raw/jumia/jumia_fy2024_results.pdf", "FY2024 PDF pp.1, 9, 12", "GMV USD0.1m; revenue USD0.001m", "yes",
        "Exit from South Africa and Tunisia; issuer also supplies a perimeter-adjusted GMV series.",
        "Orders for products/services including shipping and VAT, before discounts, cancellations and returns.", "Marketplace, first-party and other revenue."),
    row("Jumia", "E-commerce group", "Africa", 2025, "GMV", 818.6, "total_revenue", 188.9, "USD", "million",
        "https://investor.jumia.com/news/news-details/2026/Jumia-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx",
        "sources/global_ecommerce/raw/jumia/jumia_fy2025_results.html", "Full-year 2025 highlights", "USD0.1m",
        transaction_definition="Orders for products/services including shipping and VAT, before discounts, cancellations and returns.", revenue_definition="Marketplace, first-party and other revenue."),

    # Zalando GMV is dynamically reported. Latest available comparative
    # vintages are selected, while the original/revised differences are stored
    # separately by the vintage diagnostics output.
    row("Zalando", "Group", "Europe", 2020, "GMV", 10696.0, "total_revenue", 7982.0, "EUR", "million",
        "https://corporate.zalando.com/en/investor-relations/key-figures-2021",
        "sources/global_ecommerce/raw/zalando/zalando_key_figures_2021.html", "Key figures, FY2020 comparative", "EUR0.1m",
        transaction_definition="Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", revenue_definition="Group revenue including B2B and other revenue outside GMV."),
    row("Zalando", "Group", "Europe", 2021, "GMV", 14332.7, "total_revenue", 10354.0, "EUR", "million",
        "https://corporate.zalando.com/en/investor-relations/key-figures-2022",
        "sources/global_ecommerce/raw/zalando/zalando_key_figures_2022.html", "Key figures, revised FY2021 comparative", "EUR0.1m",
        transaction_definition="Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", revenue_definition="Group revenue including B2B and other revenue outside GMV."),
    row("Zalando", "Group", "Europe", 2022, "GMV", 14788.7, "total_revenue", 10344.8, "EUR", "million",
        "https://corporate.zalando.com/en/financials/zalando-full-year-23-results",
        "sources/global_ecommerce/raw/zalando/zalando_fy2023_results.html", "Zalando at a glance, revised FY2022 comparative", "EUR0.1m",
        transaction_definition="Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", revenue_definition="Group revenue including B2B and other revenue outside GMV."),
    row("Zalando", "Group", "Europe", 2023, "GMV", 14631.0, "total_revenue", 10143.1, "EUR", "million",
        "https://corporate.zalando.com/en/investor-relations/key-figures-2024",
        "sources/global_ecommerce/raw/zalando/zalando_key_figures_2024.html", "Key figures, revised FY2023 comparative", "EUR0.1m",
        transaction_definition="Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", revenue_definition="Group revenue including B2B and other revenue outside GMV."),
    row("Zalando", "Group", "Europe", 2024, "GMV", 15311.3, "total_revenue", 10572.5, "EUR", "million",
        "https://corporate.zalando.com/en/investor-relations/key-figures-2025",
        "sources/global_ecommerce/raw/zalando/zalando_key_figures_2025.html", "Key figures, revised FY2024 comparative", "EUR0.1m",
        transaction_definition="Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", revenue_definition="Group revenue including B2B and other revenue outside GMV."),
    row("Zalando", "Group", "Europe", 2025, "GMV", 17560.2, "total_revenue", 12346.1, "EUR", "million",
        "https://corporate.zalando.com/en/investor-relations/key-figures-2025",
        "sources/global_ecommerce/raw/zalando/zalando_key_figures_2025.html", "Key figures, FY2025", "EUR0.1m", "yes",
        "ABOUT YOU acquisition affects the 2025 perimeter.",
        "Merchandise after cancellations/returns, including VAT; excludes B2B and certain other B2C activity.", "Group revenue including B2B and other revenue outside GMV."),

    # Rakuten uses the FY2025 deck's retrospectively adjusted history.
    row("Rakuten", "Domestic EC", "Japan", 2023, "GMS", 6202000, "segment_revenue", 932000, "JPY", "million",
        "https://global.rakuten.com/corp/investors/assets/doc/documents/25Q4MAINPPT_E.pdf",
        "sources/global_ecommerce/raw/rakuten/rakuten_fy2025_results_deck.pdf", "PDF p.16, retrospectively revised chart", "JPY1bn", "yes",
        "FY2025 deck retrospectively realigns businesses and revises Domestic EC GMS scope.",
        "Domestic EC GMS including a broad portfolio of commerce and travel businesses.", "Domestic EC segment revenue."),
    row("Rakuten", "Domestic EC", "Japan", 2024, "GMS", 6106000, "segment_revenue", 967000, "JPY", "million",
        "https://global.rakuten.com/corp/investors/assets/doc/documents/25Q4MAINPPT_E.pdf",
        "sources/global_ecommerce/raw/rakuten/rakuten_fy2025_results_deck.pdf", "PDF p.16, retrospectively revised chart", "JPY1bn", "yes",
        "FY2025 deck retrospectively realigns businesses and revises Domestic EC GMS scope.",
        "Domestic EC GMS including a broad portfolio of commerce and travel businesses.", "Domestic EC segment revenue."),
    row("Rakuten", "Domestic EC", "Japan", 2025, "GMS", 6345000, "segment_revenue", 1023000, "JPY", "million",
        "https://global.rakuten.com/corp/investors/assets/doc/documents/25Q4MAINPPT_E.pdf",
        "sources/global_ecommerce/raw/rakuten/rakuten_fy2025_results_deck.pdf", "PDF p.16", "JPY1bn",
        transaction_definition="Domestic EC GMS including a broad portfolio of commerce and travel businesses.", revenue_definition="Domestic EC segment revenue."),

    # Mercado Libre pairs Marketplace GMV with the issuer's Commerce revenue
    # line, excluding the Fintech revenue line.
    row("Mercado Libre", "Commerce", "Latin America", 2021, "GMV", 28400, "commerce_revenue", 4635, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm", "sources/global_ecommerce/raw/mercadolibre/mercadolibre_fy2023_10k.htm", "FY2023 10-K KPI and revenue-stream comparatives", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Transactions completed through Mercado Libre Marketplace, excluding Classifieds.", revenue_definition="Commerce services plus Commerce product-sales revenue; excludes Fintech."),
    row("Mercado Libre", "Commerce", "Latin America", 2022, "GMV", 34400, "commerce_revenue", 5808, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm",
        "sources/global_ecommerce/raw/mercadolibre/mercadolibre_fy2023_10k.htm", "FY2023 10-K KPI and revenue-stream comparatives", "GMV rounded to USD0.1bn; revenue USD1m",
        transaction_definition="Transactions completed through Mercado Libre Marketplace, excluding Classifieds.", revenue_definition="Commerce services plus Commerce product-sales revenue; excludes Fintech."),
    row("Mercado Libre", "Commerce", "Latin America", 2023, "GMV", 44749, "commerce_revenue", 8201, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1099590/000109959024000008/meli-20231231.htm",
        "sources/global_ecommerce/raw/mercadolibre/mercadolibre_fy2023_10k.htm", "FY2023 10-K KPI and consolidated revenue-stream tables", "USD1m",
        transaction_definition="Transactions completed through Mercado Libre Marketplace, excluding Classifieds.", revenue_definition="Commerce services plus Commerce product-sales revenue; excludes Fintech."),
    row("Mercado Libre", "Commerce", "Latin America", 2024, "GMV", 51467, "commerce_revenue", 12159, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1099590/000109959025000007/meli-20241231.htm",
        "sources/global_ecommerce/raw/mercadolibre/mercadolibre_fy2024_10k.htm", "FY2024 10-K KPI and revenue-stream tables", "USD1m", "yes",
        "Commerce revenue increased partly because more shipping services were reported as principal rather than agent.",
        "Transactions completed through Mercado Libre Marketplace, excluding Classifieds.", "Commerce services plus Commerce product-sales revenue; excludes Fintech."),
    row("Mercado Libre", "Commerce", "Latin America", 2025, "GMV", 65037, "commerce_revenue", 16294, "USD", "million",
        "https://investor.mercadolibre.com/open-file?file=aHR0cHM6Ly9odHRwMi5tbHN0YXRpYy5jb20vc3RvcmFnZS9tbC1jbXMtYmFja2VuZC9jbXMtZG9jdW1lbnRzLXByb2Qvc2VjLzAwMDEwOTk1OTAvMDAwMTA5OTU5MC0yNi0wMDAwMDYvZm9ybTEwLUstMDAwMTA5OTU5MC0yNi0wMDAwMDYucGRm",
        "sources/global_ecommerce/raw/mercadolibre/mercadolibre_fy2025_10k.pdf", "FY2025 10-K pp.42 and 113; KPI table", "USD1m", "yes",
        "Food delivery enters GMV from Q2 2025; principal/agent shipping mix also changed.",
        "Transactions completed through Mercado Libre Marketplace, excluding Classifieds; food delivery from Q2 2025.", "Commerce services plus Commerce product-sales revenue; excludes Fintech."),

    # Sea/Shopee provides the long bridge back to Invisible Ledger.
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2017, "GMV", 4112.9, "ecommerce_revenue", 9.034, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1703399/000114420419011639/tv512574_20f.htm",
        "data/longitudinal/EDGAR_SEA_SHOPEE_GMV_QUARTERLY_2017_2021.csv", "Four quarterly GMV rows summed; annual segment-revenue row", "USD0.001m",
        transaction_definition="Shopee orders as defined in the relevant Sea filing.", revenue_definition="E-commerce segment revenue."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2018, "GMV", 10279.3, "ecommerce_revenue", 269.578, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1703399/000114036120008832/form20f.htm",
        "data/longitudinal/EDGAR_SEA_SHOPEE_GMV_QUARTERLY_2017_2021.csv", "Four quarterly GMV rows summed; annual segment-revenue row", "USD0.001m",
        transaction_definition="Shopee orders as defined in the relevant Sea filing.", revenue_definition="E-commerce segment revenue."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2019, "GMV", 17576.2, "ecommerce_revenue", 834.295, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1703399/000114036120008832/form20f.htm",
        "data/longitudinal/EDGAR_SEA_SHOPEE_GMV_QUARTERLY_2017_2021.csv", "Four quarterly GMV rows summed; annual segment-revenue row", "USD0.001m",
        transaction_definition="Shopee orders as defined in the relevant Sea filing.", revenue_definition="E-commerce segment revenue."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2020, "GMV", 35400, "ecommerce_revenue", 2167.149, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1703399/000114036121013089/brhc10022673_20f.htm",
        "data/longitudinal/EDGAR_SEA_SHOPEE_GMV_QUARTERLY_2017_2021.csv", "Four quarterly GMV rows summed; annual segment-revenue row", "GMV USD0.1bn; revenue USD0.001m",
        transaction_definition="Shopee orders as defined in the relevant Sea filing.", revenue_definition="E-commerce segment revenue."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2021, "GMV", 62600, "ecommerce_revenue", 5122.959, "USD", "million",
        "https://www.sec.gov/Archives/edgar/data/1703399/000114036122015578/brhc10036000_20f.htm",
        "data/longitudinal/EDGAR_SEA_SHOPEE_GMV_QUARTERLY_2017_2021.csv", "Four quarterly GMV rows summed; annual segment-revenue row", "GMV USD0.1bn; revenue USD0.001m",
        transaction_definition="Shopee orders as defined in the relevant Sea filing.", revenue_definition="E-commerce segment revenue."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2022, "GMV", 73500, "ecommerce_revenue", 7300, "USD", "million",
        "https://www.sea.com/investor/annualreports",
        "sources/core_public_documents/sea_2023_20f.htm", "FY2023/FY2024 issuer comparisons", "USD0.1bn", "yes",
        "The reported e-commerce revenue perimeter and monetization mix evolve over time.",
        "Shopee GMV.", "Shopee/e-commerce revenue as retained in the existing annual extension."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2023, "GMV", 78500, "ecommerce_revenue", 9000, "USD", "million",
        "https://www.sea.com/investor/annualreports",
        "sources/core_public_documents/sea_2023_20f.htm", "FY2023 20-F; existing annual extension", "USD0.1bn",
        transaction_definition="Shopee GMV.", revenue_definition="Shopee/e-commerce revenue as retained in the existing annual extension."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2024, "GMV", 100500, "ecommerce_revenue", 12400, "USD", "million",
        "https://www.sea.com/investor/annualreports",
        "sources/core_public_documents/sea_fy2024_20f_official.pdf", "FY2024 20-F; existing annual extension", "USD0.1bn",
        transaction_definition="Shopee GMV.", revenue_definition="Shopee/e-commerce revenue as retained in the existing annual extension."),
    row("Sea / Shopee", "E-commerce", "Southeast Asia and other markets", 2025, "GMV", 127400, "ecommerce_revenue", 16600, "USD", "million",
        "https://www.sea.com/investor/annualreports",
        "sources/core_public_documents/sea_fy2025_20f_yahoo_cdn.htm", "FY2025 20-F; existing annual extension", "USD0.1bn",
        transaction_definition="Shopee GMV.", revenue_definition="Shopee/e-commerce revenue as retained in the existing annual extension."),
]


COVERAGE = [
    ("eBay", "admit", "Six matched annual marketplace GMV/net-revenue periods; 2020-2021 scope break flagged."),
    ("Etsy", "admit", "Seven matched annual consolidated GMS/revenue periods; portfolio acquisitions and sales flagged."),
    ("Shopify", "admit", "Seven matched annual platform GMV/revenue periods; logistics disposal flagged."),
    ("Jumia", "admit", "Five matched annual group GMV/revenue periods; first-party mix and country exits flagged."),
    ("Zalando", "admit", "Six matched annual GMV/revenue periods using latest available dynamic-GMV vintages."),
    ("Rakuten", "admit", "Three matched Domestic EC periods on one retrospectively adjusted FY2025 basis."),
    ("Mercado Libre", "admit", "Five annual Marketplace GMV/Commerce-revenue periods; principal-agent and food-delivery breaks flagged."),
    ("Sea / Shopee", "admit", "Nine matched annual Shopee/e-commerce periods, bridging directly to the project history."),
    ("Amazon", "exclude", "No continuous issuer-reported marketplace GMV series matched to an equivalent revenue perimeter."),
    ("Alibaba", "exclude", "Historical GMV disclosure is not continuous through the retained end period and revenue scope changed."),
    ("PDD Holdings", "exclude", "No continuous issuer-reported GMV series matched to consolidated revenue."),
    ("Coupang", "exclude", "No continuous issuer-reported GMV series matched to revenue."),
    ("Allegro", "candidate", "Issuer key figures indicate GMV and revenue availability; source-vintage extraction remains pending."),
]


VINTAGE_ROWS = [
    ("Zalando", 2021, 2021, 14348.4, "original FY2021 key figures"),
    ("Zalando", 2021, 2022, 14332.7, "FY2022 comparative; selected"),
    ("Zalando", 2022, 2022, 14797.9, "original FY2022 key figures"),
    ("Zalando", 2022, 2023, 14788.7, "FY2023 comparative; selected"),
    ("Zalando", 2023, 2023, 14631.6, "original FY2023 results"),
    ("Zalando", 2023, 2024, 14631.0, "FY2024 comparative; selected"),
    ("Zalando", 2024, 2024, 15296.2, "original FY2024 key figures"),
    ("Zalando", 2024, 2025, 15311.3, "FY2025 comparative; selected"),
]


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    source = pd.DataFrame(ROWS).sort_values(["issuer", "year"])

    assert len(source) == 48
    assert source[["issuer", "segment", "year"]].duplicated().sum() == 0
    assert (source[["transaction_value", "revenue_value"]] > 0).all().all()
    assert (source["unit"] == "million").all()

    source["evidence_class"] = "direct_issuer_disclosure"
    source["analytical_role"] = "global corroboration; never pooled into Indonesia main sample"
    source.to_csv(OUT / "global_platform_source_inputs.csv", index=False)

    matched = source.copy()
    matched["take_rate_pct"] = 100 * matched["revenue_value"] / matched["transaction_value"]
    matched["transaction_minus_revenue"] = matched["transaction_value"] - matched["revenue_value"]
    matched["ecosystem_ratio"] = matched["transaction_minus_revenue"] / matched["revenue_value"]
    matched["ratio_identity_note"] = "ecosystem_ratio = 1/(take_rate_pct/100)-1; descriptive transformation only"
    matched.to_csv(OUT / "global_platform_matched_annual.csv", index=False)

    transitions = []
    for issuer, group in matched.groupby("issuer"):
        group = group.sort_values("year")
        for previous, current in zip(group.iloc[:-1].to_dict("records"), group.iloc[1:].to_dict("records"), strict=True):
            if current["year"] != previous["year"] + 1:
                continue
            tx_growth = 100 * (current["transaction_value"] / previous["transaction_value"] - 1)
            rev_growth = 100 * (current["revenue_value"] / previous["revenue_value"] - 1)
            if tx_growth >= 0 and rev_growth >= 0:
                quadrant = "activity_up_revenue_up"
            elif tx_growth >= 0 and rev_growth < 0:
                quadrant = "activity_up_revenue_down"
            elif tx_growth < 0 and rev_growth >= 0:
                quadrant = "activity_down_revenue_up"
            else:
                quadrant = "activity_down_revenue_down"
            transitions.append({
                "issuer": issuer,
                "from_year": previous["year"],
                "to_year": current["year"],
                "transaction_growth_pct": tx_growth,
                "revenue_growth_pct": rev_growth,
                "revenue_minus_transaction_growth_pp": rev_growth - tx_growth,
                "growth_quadrant": quadrant,
                "clean_scope_transition": "no" if current["scope_break"] == "yes" else "yes",
                "scope_note": current["scope_note"],
                "interpretation": "within-issuer nominal growth; not a causal estimate or cross-country pooled effect",
            })
    growth = pd.DataFrame(transitions)
    growth.to_csv(OUT / "global_platform_growth_divergence.csv", index=False)

    definitions = source.groupby(["issuer", "segment", "region"], as_index=False).agg(
        first_year=("year", "min"),
        last_year=("year", "max"),
        matched_years=("year", "count"),
        transaction_metric=("transaction_metric", "first"),
        revenue_metric=("revenue_metric", "first"),
        transaction_definition=("transaction_definition", "first"),
        revenue_definition=("revenue_definition", "first"),
        currency=("currency", "first"),
    )
    definitions["comparability_warning"] = "Comparable primarily within issuer; cross-issuer levels reflect different transaction and revenue perimeters."
    definitions.to_csv(OUT / "global_platform_definition_map.csv", index=False)

    issuer_summary = matched.groupby(["issuer", "segment", "region"], as_index=False).agg(
        first_year=("year", "min"),
        last_year=("year", "max"),
        matched_years=("year", "count"),
        first_take_rate_pct=("take_rate_pct", "first"),
        last_take_rate_pct=("take_rate_pct", "last"),
        minimum_take_rate_pct=("take_rate_pct", "min"),
        maximum_take_rate_pct=("take_rate_pct", "max"),
    )
    issuer_summary["take_rate_change_pp"] = issuer_summary["last_take_rate_pct"] - issuer_summary["first_take_rate_pct"]
    transition_counts = growth.groupby("issuer", as_index=False).agg(
        annual_transitions=("to_year", "count"),
        clean_scope_transitions=("clean_scope_transition", lambda s: int((s == "yes").sum())),
        opposite_direction_transitions=("growth_quadrant", lambda s: int(s.isin(["activity_up_revenue_down", "activity_down_revenue_up"]).sum())),
    )
    issuer_summary = issuer_summary.merge(transition_counts, on="issuer", how="left")
    issuer_summary["interpretation"] = "within-issuer descriptive trajectory; take-rate levels are not pooled across business models"
    issuer_summary.to_csv(OUT / "global_platform_issuer_summary.csv", index=False)

    coverage = pd.DataFrame(COVERAGE, columns=["issuer", "decision", "reason"])
    coverage["role"] = "global corroboration candidate, not Indonesia main sample"
    coverage.to_csv(OUT / "global_platform_coverage.csv", index=False)

    vintages = pd.DataFrame(VINTAGE_ROWS, columns=["issuer", "observation_year", "publication_vintage", "transaction_value_eur_million", "vintage_note"])
    vintages["change_from_earliest_pct"] = vintages.groupby(["issuer", "observation_year"])["transaction_value_eur_million"].transform(lambda s: 100 * (s / s.iloc[0] - 1))
    vintages["interpretation"] = "same economic period, different publication vintage; never count as extra observation"
    vintages.to_csv(OUT / "global_platform_vintage_diagnostics.csv", index=False)

    clean = growth[growth["clean_scope_transition"] == "yes"].copy()
    summary = pd.DataFrame([
        {"metric": "matched_issuer_years", "value": len(matched), "unit": "rows"},
        {"metric": "issuers", "value": matched["issuer"].nunique(), "unit": "issuers"},
        {"metric": "annual_transitions", "value": len(growth), "unit": "transitions"},
        {"metric": "clean_scope_transitions", "value": len(clean), "unit": "transitions"},
        {"metric": "opposite_direction_transitions_all", "value": int(growth["growth_quadrant"].isin(["activity_up_revenue_down", "activity_down_revenue_up"]).sum()), "unit": "transitions"},
        {"metric": "opposite_direction_transitions_clean", "value": int(clean["growth_quadrant"].isin(["activity_up_revenue_down", "activity_down_revenue_up"]).sum()), "unit": "transitions"},
        {"metric": "median_abs_growth_divergence_clean", "value": clean["revenue_minus_transaction_growth_pp"].abs().median(), "unit": "percentage_points"},
        {"metric": "max_abs_growth_divergence_clean", "value": clean["revenue_minus_transaction_growth_pp"].abs().max(), "unit": "percentage_points"},
    ])
    summary.to_csv(OUT / "global_platform_summary.csv", index=False)

    # Indexed trajectories avoid converting currencies or adding issuer totals.
    fig, axes = plt.subplots(2, 4, figsize=(15, 7.5), sharey=False)
    for ax, (issuer, group) in zip(axes.flat, matched.groupby("issuer", sort=True), strict=True):
        group = group.sort_values("year")
        tx_index = 100 * group["transaction_value"] / group["transaction_value"].iloc[0]
        rev_index = 100 * group["revenue_value"] / group["revenue_value"].iloc[0]
        ax.plot(group["year"], tx_index, marker="o", linewidth=2, label="Transaction measure")
        ax.plot(group["year"], rev_index, marker="s", linewidth=2, label="Revenue")
        for _, point in group[group["scope_break"] == "yes"].iterrows():
            ax.axvline(point["year"], color="#888888", linestyle=":", linewidth=1)
        ax.axhline(100, color="#cccccc", linewidth=0.8)
        ax.set_title(issuer)
        ax.set_xticks(group["year"])
        ax.tick_params(axis="x", rotation=45)
        ax.grid(axis="y", alpha=0.2)
    axes[0, 0].legend(frameon=False, fontsize=8)
    fig.suptitle("Transaction activity and recognized revenue can follow different paths\n(indexed to each issuer's first retained year = 100; dotted lines flag scope breaks)")
    fig.supxlabel("Fiscal year")
    fig.supylabel("Within-issuer index")
    fig.tight_layout(rect=(0.02, 0.03, 1, 0.93))
    fig.savefig(FIGURES / "global_platform_activity_revenue_index.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 7))
    palette = dict(zip(sorted(clean["issuer"].unique()), plt.cm.tab10.colors, strict=False))
    for issuer, group in clean.groupby("issuer"):
        ax.scatter(
            group["transaction_growth_pct"], group["revenue_growth_pct"],
            s=58, alpha=0.82, label=issuer, color=palette[issuer], edgecolor="white", linewidth=0.5,
        )
    low = min(clean["transaction_growth_pct"].min(), clean["revenue_growth_pct"].min()) - 5
    high = max(clean["transaction_growth_pct"].max(), clean["revenue_growth_pct"].max()) + 5
    ax.plot([low, high], [low, high], color="#555555", linestyle="--", linewidth=1, label="Equal growth")
    ax.axhline(0, color="#aaaaaa", linewidth=0.8)
    ax.axvline(0, color="#aaaaaa", linewidth=0.8)
    opposite = clean[clean["growth_quadrant"].isin(["activity_up_revenue_down", "activity_down_revenue_up"])]
    offsets = {
        ("Etsy", 2022): (8, 10),
        ("Etsy", 2024): (8, -18),
        ("eBay", 2023): (8, 8),
        ("Zalando", 2022): (8, -18),
    }
    for _, point in opposite.iterrows():
        offset = offsets.get((point["issuer"], int(point["to_year"])), (5, 5))
        ax.annotate(
            f"{point['issuer']} {int(point['from_year'])}–{int(point['to_year'])}",
            (point["transaction_growth_pct"], point["revenue_growth_pct"]),
            xytext=offset, textcoords="offset points", fontsize=8,
        )
    ax.set_xscale("symlog", linthresh=20)
    ax.set_yscale("symlog", linthresh=20)
    ax.set_xlim(low, high)
    ax.set_ylim(low, high)
    ax.set_xlabel("Transaction-measure growth (%)")
    ax.set_ylabel("Recognized-revenue growth (%)")
    ax.set_title("Within-issuer transaction and revenue growth are not interchangeable\n29 annual transitions without a flagged perimeter break")
    ax.grid(alpha=0.2)
    ax.legend(frameon=False, fontsize=8, ncol=2, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIGURES / "global_platform_growth_divergence.png", dpi=220)
    plt.close(fig)

    print(f"Wrote {len(matched)} matched issuer-years across {matched['issuer'].nunique()} issuers")
    print(f"Wrote {len(growth)} annual transitions, of which {len(clean)} are not flagged for a scope break")


if __name__ == "__main__":
    build()
