# Jakarta Smart City feasibility sketch for .jakarta

Research addition checked 16 November 2026. This is a companion to [What it would take to create .jakarta](https://github.com/irvan-putra/kaji/blob/main/docs/jakarta-tld.md); the main note covers the ICANN application route, fixed registry fee, transaction threshold, geographic-name rules, and .amsterdam background. This addition focuses on indicative Rupiah conversions and a possible Jakarta Smart City feasibility case. It is research, not a city commitment.

## What the fees look like in Rupiah

Exchange rate: Bank Indonesia's latest published JISDOR USD/IDR reference rate when checked on 16 November 2026 was Rp 18,250.00 per USD (dated 16 November 2026; see the daily table at the source link). BI's transaction-rates page displayed USD selling Rp 18,309.09 and buying Rp 18,126.91 when checked that day; that page did not expose a matching date in the fetched table, so the calculations below use dated JISDOR only. Sources: https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/default.aspx and https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx

- Application fee (2026 round): USD 227,000 x 18,250 = **Rp 4,139,750,000** (~Rp 4.14 billion).
- Ongoing ICANN fixed registry fee at the pinned January 2025 baseline: US$6,437.50 x 18,250 = Rp 117,484,375 per quarter, i.e. US$25,750 x 18,250 = **Rp 469,937,500 per year** (~Rp 470 million). CPI-adjustable; whether any per-transaction fee is owed on top depends on actual transaction volumes against the transaction threshold described in the main .jakarta note - that cannot be predicted from domain counts alone.
- Caveats: these are 2026-round and January-2025 fee-schedule figures; no future round or its fees have been announced, and a later round could cost more or less. The Rupiah amounts are indicative - the actual IDR cost depends on the exchange rate on the day of payment.

## Could Jakarta Smart City fund it? A proposal sketch

This section is research on how the case could be made. It is not a commitment, and no one has approved or requested it on the city's side.

**What Jakarta Smart City is.** Jakarta's official portal describes Jakarta Smart City as a regional public service agency (BLUD) under Diskominfotik, established in 2014, with seven smart-city indicators including Smart Branding. Gubernatorial Regulation 57/2022, as amended by Regulations 17/2023 and 40/2023, is the current organization regulation. These sources establish the institutional context, not JSC's specific spending authority; that needs separate review under the applicable BLUD and provincial rules.

**A possible budget path - authority needs review.** If the proposal depended on APBD funding, the standard regional budget process under Government Regulation 12/2019 includes the KUA-PPAS (general budget policy and interim ceilings), draft APBD, and DPRD agreement before the budget is enacted. Jakarta's 2026 APBD, for example, was approved on 12 November 2025. JSC is a BLUD under Diskominfotik, so its actual spending authority, budget route and any delegated flexibility must be checked against the applicable BLUD and provincial rules; this note does not assume that APBD is the only route or that JSC can commit the city. A back-end registry service would require the applicable procurement process. Presidential Regulation 16/2018, as amended by 12/2021 and 46/2025, may be relevant, but which procurement rules and method apply - including any BLUD-specific rules - needs legal and procurement review. This note makes no affordability argument.

**Cost realism - the application fee is not the whole story.** A budget proposal has to cover recurring costs indefinitely:

- The ICANN fixed registry fee, about Rp 470 million per year at the January 2025 baseline (CPI-adjustable).
- A back-end registry services contract: city TLDs typically outsource technical operations to an established registry service provider (SIDN was involved in the .amsterdam launch). The real cost range is unknown until providers are actually asked, through market consultation or procurement - no figure is estimated here.
- Internal staffing, DNS abuse handling, and outreach.

**Possible offsets - not established.** Whether a city-operated .jakarta registry could charge registration fees through JSC's existing service-tariff mechanism is an open legal question. Pergub 44/2021 lists tariffs for existing JSC services; that list alone does not establish authority to charge for registry names. Any revenue projection would also be speculation; one observable data point is .amsterdam, which had 18,404 domains under management when nTLDstats was checked on 16 November 2026. That third-party count is a limited adoption snapshot, not evidence of cost recovery. (It says nothing about transaction volumes and cannot be used to predict ICANN per-transaction fees.)

**The value case, and the honest case against.** For: an official city namespace could support Smart Branding for city services, tourism, and local business, with technical operations handled by a contracted registry backend, as in the .amsterdam precedent. There is also a conditional defensive angle: ICANN's rules do not universally reserve non-capital city names, so if Jakarta falls within that non-capital rule and a non-city applicant took the string in a future round without city-associated intent, the city's remedies would be a formal objection or a competing application. Against: the city already runs jakarta.go.id, and a normal .id registration is much cheaper for an individual name: when checked on 16 November 2026, DomaiNesia listed a Rp 249,000 price and a Rp 99,000 first-year promotion requiring two years at once (Rp 298,000 total, with Rp 199,000 for year two). Promotional, tax, renewal and provider terms vary. A per-name retail price is not a direct comparison with the total cost of operating a TLD, but it shows that existing .id names are a low-cost alternative for many practical needs. Adoption precedent is modest (.amsterdam's ~18,400 names after ten years), no future round is announced and its fees are unknown, and applying does not guarantee delegation. For most practical needs, subdomains and .id names already work.

**Recommendation (as a proposal, not a commitment).** A phased approach keeps the decision honest:

- Phase 1 - feasibility study, a small budget line in a future APBD cycle, with defined deliverables: demand research (would Jakarta's residents, businesses and agencies actually register and use .jakarta names?), an indicative cost range gathered from registry back-end providers through market consultation, a legal opinion on tariff authority for registration fees, and monitoring for ICANN's next-round announcement.
- Decision gate: proceed to Phase 2 (an actual application budget) only if a next ICANN round is announced AND the study supports the case on demand and total cost of ownership. If either fails, the city stops, having spent only the study cost.

### Sources for this section

- Bank Indonesia JISDOR USD/IDR, dated daily table (16 November 2026: Rp 18,250.00; checked 16 November 2026): https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/default.aspx
- Bank Indonesia transaction rates (checked 16 November 2026; USD sell 18,309.09 / buy 18,126.91): https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx
- Current DKI organization regulation - Pergub 57/2022, Lampiran XIX (Diskominfotik; UP Jakarta Smart City task and reporting line), as amended: https://jdih.jakarta.go.id/dokumen/detail/5877/peraturan-gubernur-nomor-57-tahun-2022-tentang-organisasi-dan-tata-kerja-perangkat-daerah and amendments: https://peraturan.bpk.go.id/Details/254787/pergub-prov-dki-jakarta-no-17-tahun-2023 , https://peraturan.bpk.go.id/Details/273068/pergub-prov-dki-jakarta-no-40-tahun-2023
- Regional financial management cycle (KUA-PPAS, draft APBD, DPRD agreement) - PP 12/2019: https://peraturan.bpk.go.id/Details/103888/pp-no-12-tahun-2019
- Government procurement rules - Perpres 16/2018, as amended by Perpres 12/2021 and 46/2025: https://peraturan.bpk.go.id/Details/73586/perpres-no-16-tahun-2018 , https://peraturan.bpk.go.id/Details/161828/perpres-no-12-tahun-2021 , https://peraturan.bpk.go.id/Details/318647/perpres-no-46-tahun-2025
- JSC as BLUD and the seven indicators including Smart Branding (official Jakarta portal): https://www.jakarta.go.id/jakarta-smart-city
- Pergub DKI 44/2021 (UP Jakarta Smart City tariffs for existing services): https://peraturan.bpk.go.id/Details/195012/pergub-prov-dki-jakarta-no-44-tahun-2021
- APBD 2026 approval timing example (passed 12 November 2025): https://megapolitan.kompas.com/read/2025/11/12/16573491/tok-apbd-dki-2026-disahkan-rp-813-triliun
- .amsterdam domains under management (~18,400, checked 16 November 2026): https://ntldstats.com/tld/amsterdam
- DomaiNesia .id list/promotion price (checked 16 November 2026; two-year and renewal terms noted above): https://www.domainesia.com/domain/
