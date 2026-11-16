# Crypto in Indonesia: supervision, how a seller's trades are taxed, and wallet design choices

Status: general information from official texts, read 2026-11-16. Not financial, legal or tax advice. Rules change; check the sources. Where a point could not be confirmed from a current official source it says so.

## Using crypto as payment: a 2018 statement, not checked for today
Bank Indonesia's press release of 13 January 2018 (No. 20/4/DKom) says virtual currency, including bitcoin, "tidak diakui sebagai alat pembayaran yang sah" (is not recognised as a legal means of payment), may not be used as payment in Indonesia, and bars payment-system providers from processing payments in it. https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_200418.aspx
This is a historical statement. Whether later BI rules changed it was not verified, so it is not stated here as current law.

## Supervision
The recital of PMK 50/2025 (see below) says the regulation and supervision of digital financial assets, including crypto assets and financial derivatives, was transferred to OJK under Government Regulation 49/2024 ("peralihan tugas pengaturan dan pengawasan ... kepada Otoritas Jasa Keuangan"). This note does not say how duties are divided between OJK and Bank Indonesia; the sources read here do not set that out.
OJK publishes lists of licensed digital financial asset trading providers (the page read was the 12 March 2026 list): https://ojk.go.id/en/Fungsi-Utama/ITSK/Perizinan-ITSK-Aset-Keuangan-Digital-Aset-Kripto/Pages/List-of-Digital-Financial-Asset-Trading-Providers-as-of-12-March-2026.aspx

## Income tax on a seller's trades (PMK 50/2025): how the rate depends on who runs the platform
Source: the regulation text, https://jdih.kemenkeu.go.id/api/download/66a7633b-9e1b-4a54-9046-5320aa96c7e1/2025pmkeuangan050.pdf (Arts. 10-22 read on 2026-11-16). The tax base is the transaction value (Art. 12(5): for fiat sales, the money paid by the buyer). All of these are final Article 22 income tax. This is a summary of the articles, not a complete or advisory reading.
- Art. 10-11: a crypto seller's income from trades made through an electronic trading platform is taxable; fiat sales, swaps and other transactions are covered.
- Art. 12: 0.21% of transaction value. It is collected, paid and reported by the platform operator, which Art. 12(4) defines as a Pedagang Aset Keuangan Digital (PAKD, a licensed digital financial asset trader).
- Art. 13: platforms that only offer e-wallet services, only match buyers and sellers, or do not facilitate trading are not required to collect. For trades through them the rate is also 0.21%, and the seller pays it.
- Art. 17-20: a foreign platform can be appointed as tax collector by the Minister (the Director General of Taxes under Art. 18(4)); appointment follows set criteria (transaction value or traffic from users in Indonesia above thresholds) or the platform's own choice. For trades on an appointed foreign platform the rate is 1% of transaction value, collected by the platform (Art. 20). Foreign income tax already paid on such income is not creditable in Indonesia (Art. 20(3)).
- Art. 22: for a foreign platform with no collector appointment under Art. 17(1), the rate is 1%, and the seller pays and reports it.
- Art. 14 lists exemptions (for example for certain foreign taxpayers); not summarised.
So 0.21% applies to licensed domestic traders (and to non-collecting platform types, self-paid), and 1% to foreign platforms, whether appointed (collected) or not (self-paid). Details such as thresholds are set by the Minister or the Director General of Taxes and were not read.
- VAT: Art. 4 imposes VAT on the platform's electronic-facility service. The tax office's explainer says the crypto trades themselves are not subject to VAT from 1 August 2025: https://pajak.go.id/id/artikel/aspek-pajak-transaksi-kripto-dulu-dan-sekarang
- Mining (Art. 24-26) and platform income (Art. 23) were not summarised.

## Wallet design choices (general, not a guarantee)
- A custodial account at a platform means the provider holds the keys; signup rules and whether rupiah can be deposited or withdrawn depend on the provider and were not checked for any specific one.
- A self-custody wallet app puts the keys with you. ethereum.org's security page says the recovery phrase is the master key, not to be shared or screenshotted (screenshots may sync to cloud storage), and that transactions are irreversible. https://ethereum.org/security/
- Which tax and licensing rules apply to a given wallet type was not worked out here.
