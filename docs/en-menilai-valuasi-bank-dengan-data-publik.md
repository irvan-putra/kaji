# Assessing bank valuation with public data and independent evidence

Research note. Source examined 17 November 2026; verification status is stated per section.

## Research question

How can a bank's equity value be estimated without relying only on figures from the bank itself? One focus is testing whether a bank that looks cheap against its book value is still cheap after credit risk and the cost of retaining customers are taken into account.

## Five-step framework (design)

1. **Examine borrowers.** Sample borrowing companies that disclose their creditor bank in financial statements; examine debt, cash flow, interest payments, and business conditions. A public sample does not represent the whole credit portfolio.
2. **Compare funding costs and market assessment.** For bond-issuing banks, compare yields with government bonds of comparable tenor; account for liquidity and seniority.
3. **Test customer relationships.** Sampling customers and merchants can test which accounts are used for payroll, savings, and transactions. This needs surveys or interviews, not just public data.
4. **Separate external assessments from independent data.** Credit ratings provide a comparative view, but their underlying figures may still come from the bank.
5. **Value the equity.** A residual income model can start from adjusted book value of equity, then add the present value of earnings above the return required by shareholders.

This note focuses on bank equity valuation. Cash-flow-based valuation for non-bank companies is a separate topic; residual income is not exclusive to banks.

The material also proposes reverse valuation as follow-up research: estimating the ROE, cost of equity, and growth implied in the current market price. The goal is to test price assumptions without requiring the reader to accept a single fair-value estimate. This is a proposal, not yet computed.

## Public data and field work

Public data can be used to find borrowers that disclose their creditors, test interest-paying ability, compare published deposit rates and bond yields, read rating rationales, and build models with credit-loss, ROE, growth, and cost-of-equity scenarios.

Borrower interviews, business and collateral inspections, lawful access to credit documents, special offers for large customers, and customer and merchant interviews require appropriate access and human work. A public sample alone does not answer those questions.

The research design should set primary indicators, control factors, data-exclusion rules, and results that would weaken the hypothesis before processing data. Later changes need to be recorded so exploratory analysis is not confused with the original plan.

## Public sources and examination status

The existence of a page or document does not by itself prove the contents of the valuation framework.

- **PHEI/IBPA.** PHEI is identified as a securities-pricing institution and the IBPA page displays benchmark rates. Sources: Antara (https://www.antaranews.com/berita/108722/proyeksi-pasar-obligasi-melonjak-100-persen-pasca-bpa), CNN Indonesia (https://www.cnnindonesia.com/ekonomi/20160307142505-78-115830/phei-nilai-531-jenis-obligasi-senilai-rp2330-triliun), IBPA (https://siso.phei.co.id/).
- **PEFINDO.** Two public rating reports contain statements that ratios are calculated from company information and published reports. Example sources: https://ftp.ptsmi.co.id/cfind/source/files/rating/smi-pefindo-ratings-2026.pdf and https://investor.jasamarga.com/newsroom/20260306_JSMR_Laporan_Hasil_Pemeringkatan_32041576_lamp2.pdf. This is not an examination of all PEFINDO reports.
- **Damodaran.** The material mentions the DDM approach, regulatory-capital-based FCFE, and excess return for banks. The "Financial service companies: Value drivers" page is accessible (https://pages.stern.nyu.edu/adamodar/New_Home_Page/littlebook/bankvaluedriver.htm), and the paper "Valuing Financial Service Firms" is available (https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/finfirm.pdf); the fit of each part with the framework above has not been examined.
- **Deposit rates.** The BCA Time Deposit page is available (https://www.bca.co.id/id/Individu/produk/simpanan/Deposito-Berjangka). Current rate figures are not recorded here.
- **Issuer reports.** The Astra 2024 Annual Report is available (https://r2.astra.co.id/annual-reports/documents/Astra-Annual-Report-2024.pdf); whether bank-creditor details can be read in it has not been examined page by page.
- **Southeast Asia study.** The thesis "A Comparative Analysis of Bank Valuation Approaches in Southeast Asia" by Amos Timothy Ong (2020) is in the Fordham repository (https://research.library.fordham.edu/gabelli_thesis/73/). The material states the Residual Income Model is closest to price for 32 ASEAN banks, adjusted R-squared 90.29%, and Capital IQ market data; those figures, methods, and results are unverified.
- **Indonesia study.** A JIMFEB Universitas Brawijaya article (2021) is available and uses BBRI, BBCA, BMRI, and BBNI; the article reports different results between the Excess Return Model and DDM (https://jimfeb.ub.ac.id/index.php/jimfeb/article/view/7678).
- **Bank report transparency.** The SEOJK 29/SEOJK.03/2025 page on transparency and publication of conventional commercial bank reports is available (https://ojk.go.id/id/regulasi/Pages/29-SEOJK03-2025-Transparansi-dan-Publikasi-Laporan-Bank-Umum-Konvensional.aspx). The page mentions POJK 18/2025 as the legal basis and states the SEOJK takes effect 2 September 2026. The effective date of POJK 18/2025 has not been checked separately; that instrument is different from the SEOJK. The publication-column details in the annex have not been examined.

## Input design and testing

- Set quarterly valuation dates on the first trading day after both banks release comparable quarterly reports; use only information already public at that time.
- Proposed inputs: book value per share from consolidated statements; TTM earnings; dividends and payout from corporate-action announcements; a residual income estimate with ROE fading linearly from the current year to a long-term level; forecast book value with clean surplus accounting; DDM with the same assumptions as residual income; and peer median P/B with criteria set in advance.
- For same-date comparison, test value estimate V(t) against price P(t). For predictive ability, relate the discount V(t)/P(t) - 1 to total return over the following 12 months. Comparing V(t) with P(t+12) mixes the estimation date with a future price, so it is not used.
- Unresolved items in the design: consistency of OCI with clean surplus; the risk of double counting country premium and equity premium; the total-return benchmark; and observation dependence from overlapping 12-month windows.

## Proposed forensic screening from public data

The proposed screening design covers comparing Stage 2 and Stage 3 credit against NPL, restructuring and write-offs; backtesting provisions against subsequent defaults and recoveries; interest income quality compared with cash flow; Stage 3 coverage before and after collateral; quarter-end credit spikes that reverse afterward; related-party, sector, and large-borrower concentration; restatements and auditor changes; and revaluation using normalized earnings and stressed ECL.

This is a research proposal not yet tested on data. The availability of public columns and backtest feasibility have not been confirmed. The design distinguishes two timing questions: structural vulnerability and whether the probability of failure is rising. The relationship between the two signals, thresholds, and predictive performance have not been set or tested. No conclusion is drawn about evergreening, hidden relationships, or collateral manipulation. The intended output is a signal for further examination, not a fraud verdict; findings still require evidence from supervisors, auditors, or authorized insiders.

## Regulator-reported case examples

Two public examples help formulate research questions but do not test whether the indicators above can predict bank failure.

- **Banco Master, Brazil.** The official Banco Central do Brasil FAQ states that on 18 November 2025 it ordered the extrajudicial liquidation of Banco Master S/A and several related entities, and applied a temporary administration regime to Banco Master Múltiplo S/A. BCB cited a severe liquidity crisis and serious violations as reasons. Source: https://www.bcb.gov.br/estabilidadefinanceira/banco-master-liquidacao. The detailed claims in the material, credit growth of 81% in a year, R$8.73 billion in judicial receivables, and a Basel ratio of 11.54%, are unverified.
- **Ueno Bank, Paraguay.** BCP announced on 3 November 2026 that the resolution process began after financial-statement adjustments during the regularization process showed a solvency ratio of less than half the required minimum; the board decision is dated 2 November 2026. Official source: https://www.bcp.gov.py/web/institucional/w/banco-central-inicia-el-procedimiento-de-resolucion-de-ueno-bank. The detailed claims in the material, credit growth of 49.1% year-on-year, liquidity of 20.7% of deposits, a negative Fitch outlook on 16 October, and Ueno bond price and yield movements, are unverified against sources.

## Unverified precedent and supervision designs

Beyond the case examples above, the material mentions SEC findings on Regions Bank (US$168 million of troubled loans reported as still current in 2009), EBA monitoring of Stage 1 to Stage 3 migration, the ECB 2014 asset quality review, Basel Committee 2024 principles, and the PMC Bank India case in 2019. The exact references and detailed claims have not been examined.

The material also proposes tiered monitoring: watch aggregate data first, open debtor-level analysis only after anomalies appear, and set consequences for data misuse. This is a policy proposal, not an external analyst capability or a running procedure.

The material raises the possibility of using risk research results for trading decisions, including bond shorts, CDS, or pair trades. This only records the application question raised; no strategy is recommended, tested, or executed. Accessible instruments, liquidity, catalysts, costs, and model risk have not been determined. Claims about Ueno bond price or yield movements are also unverified.

## Unverified research claims and additional figures

Several claims accompanying this design have not been matched with primary sources. They are recorded so they are not lost, not as findings:

- One study cited in the material is said to use 2,263 analyst reports in the United States and Europe and to find P/E and P/BV more dominant than DDM and residual income. The study and its results are unverified.
- The material states that the open-source valuation platforms found focus on general or US/Hong Kong markets. The platform list and market coverage have not been examined.
- Banco Fassil in Bolivia is cited as an intervention example on 26 April 2023, with an earlier Moody's downgrade. The dates, events, and downgrade sequence are unverified.
- The claimed warning ranges of 12-24 months for watchlist, 6-12 months for high risk, and 1-3 months for liquidity events are retrospective claims in the material; no predictive-performance evidence accompanies them.
- The proposal slides state BBCA assets of Rp1,661 trillion as of 30 June 2026 and Bank Mandiri ROE of 20.9% for H1 2026, 16.0% for 2016-2025, and 19.8% for 2021-2025. These figures and periods have not been matched against issuer reports or presentations.
- The Astra 2024 Annual Report is available at https://r2.astra.co.id/annual-reports/documents/Astra-Annual-Report-2024.pdf, but whether its details disclose creditor banks has not been examined page by page. The Upwork financial analyst rates page (https://www.upwork.com/hire/financial-analysts/cost/) is cited as a comparison; the exact rates are unverified and are not an offer.

## Budget and funding design (assumptions, not offers)

The planning material contains different, unreconciled estimates:

- One rupiah estimate states Rp28.8 million for a two-bank pilot over four weeks. The stated calculation consists of Rp24 million of costs and a 20% reserve of Rp4.8 million; the public-data audit stage is stated at Rp8.4 million. This is only planning arithmetic and assumptions, not vendor prices or agreed costs.
- Another proposal document uses a parametric dollar estimate based on working hours and a range of comparison rates, including an example of 25 hours times USD25-70 for a source audit. No rupiah total is set.
- A more concise proposal version lists no money estimate and asks for quotes per work package first. The revision order cannot be determined because the version labeling is inconsistent.

Costs not yet counted include taxes, paid data licenses, travel, and permit or donation-channel fees. No vendor quote, funding target, verified organizer, or field data is included in the examined material. The figures above must not be read as a final budget or an invitation to pay.

## Governance and status of proposal material

The proposal material proposes that use of funds follow a published budget, spending and balances be reported, supporter affiliations with researched banks be disclosed, research-team share ownership be stated, input be submittable through a correction channel, and analysis decisions remain with the research team. These are proposed principles; there is no evidence in the examined material that fundraising, a chosen vendor, fund collection, valuation results, or predictive tests have been carried out.

The material includes slide decks (one 15-slide proposal, one 9-slide version without money estimates and a narrowed donation appeal for a two-bank pilot), several slide PDFs, task lists and executive summaries inside slides rather than as separate files, pitching material as draft text (not quoted in this note), and a fundraising page that exists only as a draft (no live site or receipt of funds is proven). An audio recording is mentioned but no audio file is available for examination. An academic paper is also mentioned in the plan list, but no paper file is available; claims about its submission status conflict with each other. The available PDFs are slide exports, not a paper. No video was received. A one-page gap analysis is also referenced, but the file is not available for examination and its private link is not published.

So this package still has proposal status. There is no evidence of fieldwork, a selected vendor, fundraising, valuation results, or executed predictive tests.

## Limits

This is a design, not a valuation result or a forensic examination. No sampling, bank data extraction, computed model, price assessment, backtest, or field test has been done in this note. Figure claims not matched with issuer documents are not presented as fact. No trading strategy has been constructed or tested.
