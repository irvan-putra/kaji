# What it would take to create .jakarta

- Checked: 2026-11-16 (all sources opened that day; URLs at the end)

Seeing a site like https://openbsd.amsterdam might suggest that city top-level domains are easy to get. Two different things are involved: openbsd.amsterdam is a second-level domain registered under the existing .amsterdam top-level domain (the site belongs to a small hosting provider). Having names under .jakarta would require someone to create and operate .jakarta itself as a new top-level domain. This note covers what that takes.

## Current status of .jakarta (as of 2026-11-16)

- .jakarta is not delegated: it does not appear in the public DNS root zone (checked against the live root zone file from internic.net), so .jakarta names are not available through ordinary registrar registration today.
- No published application for a string containing "jakarta" appears in ICANN's public application database for the 2026 new gTLD round. We searched ICANN's Application Publication and Statistics (APS) portal on 2026-11-16 by string, variant string, and applicant name, with no status filter and with a final-states filter (Withdrawn/Terminated/Deactivated): zero matches in every query. The search matches substrings (verified: "abio" returns "abion"), so a string merely containing "jakarta" would have shown up. Applications that were never paid for were never published, so this observation covers published applications only.
- The 2026 round is closed: per ICANN's announcements, the submission window ran 30 April to 12 August 2026 (23:59 UTC); 1,663 applications were submitted and 1,616 paid applications proceeded. The applied-for strings were published on Reveal Day, 7 October 2026.
- The numbers reconcile as follows: ICANN's APS Statistics tab counts 1,615 applications from 481 applicants (data generated 7 October 2026, all "Active" at that point), while the Applications tab lists 2,783 records because each designated replacement string appears as its own record alongside its primary string.
- ICANN has not announced a date for the following round as of 2026-11-16; its program site lists only the 2026 round. For scale, the previous gap was long: the first new gTLD round was 2012, the current one 2026.

## What creating a city TLD requires (2026 round rules)

- A legal entity applicant: only corporations, organizations, institutions, or governmental/non-governmental/inter-governmental entities may apply. Individuals and sole proprietorships cannot (AGB Module 1, Section 1.1.1).
- Money: a USD 227,000 evaluation fee per application (75-85% discounts exist for qualified Applicant Support Program applicants). If the application succeeds, the operator signs a Base Registry Agreement with ICANN and pays ongoing registry-level fees, and must actually run registry infrastructure (DNS, registration systems, escrow, abuse handling) or contract a back-end provider.
- Ongoing fees under the 2026 Base Registry Agreement (approved 12 March 2026, Article 6, Section 6.1(a)): a registry-level fixed fee and a per-transaction fee, both CPI-adjustable over time. The agreement pins the January 2025 amounts: US$6,437.50 per calendar quarter fixed, and US$0.2575 per registration transaction. The transaction fee is gated by a transaction threshold; Section 6.1(a) says it "shall not apply until and unless more than 50,000 Transactions have occurred in the TLD during any calendar quarter or any consecutive four calendar quarter period in the aggregate (the 'Transaction Threshold') and shall apply to each Transaction that occurred during each quarter in which the Transaction Threshold has been met, but shall not apply to each quarter in which the Transaction Threshold has not been met". In plain terms: the per-transaction fee starts only after the TLD passes 50,000 registration transactions in a quarter (or a consecutive four-quarter aggregate), and applies per quarter where the threshold is met - it does not depend on total domains under management.
- Government involvement for city names: under AGB Module 7, strings that are capital city names (in any language), or city names the applicant declares it will use for purposes associated with the city, are "Geographic Names" requiring signed documentation of support or non-objection from the relevant government(s) or public authority(ies) - official letterhead, dated within four months of the application window opening, verified by ICANN's Geographic Names Panel. Whether or not the capital-city rule applies to Jakarta, the city-name rule clearly applies to any application intending city-associated use. (Indonesia's capital arrangements are in transition; this note does not depend on settling that.)
- Limits of city protection: non-capital city names are not universally protected. For an application that matches a non-capital city name but does not intend city-associated use, no government documentation is required; the city government's recourse in that case is to file a formal objection or apply for the string itself. Capital city names (in any language) are excluded from this latitude: they always require government documentation. And for any city-use application, the support/non-objection documentation is mandatory.
- Process after applying: administrative review, string and applicant evaluation, public comment and possible objections, contention resolution if multiple applicants want the same string, contracting, and pre-delegation testing before the TLD enters the root zone.

## The .amsterdam precedent

.amsterdam is a city-run TLD: its sponsoring organization is Gemeente Amsterdam (the Municipality of Amsterdam), per its IANA delegation report. It was applied for in the 2012 round, delegated on 22 December 2014, and opened to public registration through ordinary registrars in 2015, with the Dutch ccTLD operator SIDN involved in the launch. Once the TLD existed, second-level names like openbsd.amsterdam became ordinary domain registrations.

## So what would it take for .jakarta?

Realistically: the Jakarta city government, or an organization with its documented support, would need to apply in a future ICANN new gTLD round (none announced as of 2026-11-16), pay the USD 227,000 application fee, pass evaluation including the Geographic Names Review, sign the registry agreement, and operate the TLD. Until then, Jakarta-related names live under existing TLDs such as Indonesia's .id.

## Sources

- DNS root zone (live file): https://www.internic.net/domain/root.zone
- ICANN APS application search: https://newgtldprogram-aps.icann.org/applications and statistics: https://newgtldprogram-aps.icann.org/statistics
- 2026 round overview: https://newgtldprogram.icann.org/en/application-rounds/round2
- Application window dates: https://newgtldprogram.icann.org/en/application-rounds/round2/2026-round-general/application-submission/faqs/general/when-is-the-application-period-open
- Round close (window closed 12 August 2026; 1,663 applications): https://www.icann.org/en/announcements/details/icann-2026-round-closes-with-more-than-1600-new-gtld-applications-13-08-2026-en
- 1,616 paid applications proceeding (22 September 2026): https://www.icann.org/en/announcements/details/icann-confirms-number-of-applications-proceeding-in-the-2026-round-22-09-2026-en
- Eligibility (AGB Module 1): https://newgtldprogram-2026-agb.icann.org/en/5-module-1-the-applicant-journey.html
- Evaluation fee FAQ (USD 227,000, ASP discounts): https://newgtldprogram.icann.org/en/application-rounds/round2/2026-round-general/gtld-evaluation-fee/faqs
- Geographic Name types (AGB Module 7): https://newgtldprogram-2026-agb.icann.org/en/11-module-7-string-and-application-evaluation-procedures.html
- Government letter requirements (AGB Appendix 2): https://newgtldprogram-2026-agb.icann.org/en/13-appendix-2-materials-related-to-geographic-names.html
- Geographic Names Review scope: https://newgtldprogram.icann.org/en/application-rounds/round2/2026-round-general/application-evaluation/faqs/geographic-names-review/what-does-the-geographic-names-review-evaluate
- City-government recourse for non-city-use applications: https://newgtldprogram.icann.org/en/application-rounds/round2/2026-round-general/application-types/faqs/geographic-names/what-recourse-does-a-city-government-have-if-an-applicant-applies-for-a-string-that-matches-the-city-name-but-the-applicant-does-not-intend-to-use-the-string-in-a-manner
- 2026 Base Registry Agreement (approved 12 March 2026; fee schedule in Section 6.1): https://www.icann.org/en/contracted-parties/registry-operators/registry-agreements/base-agreement/2026
- .amsterdam delegation report (Gemeente Amsterdam, 2014-12-22): https://www.iana.org/reports/c.2.9.2.d/20141222-amsterdam
- .amsterdam 2015 launch: https://www.sidn.nl/en/news-and-blogs/amsterdam-now-open-for-business
