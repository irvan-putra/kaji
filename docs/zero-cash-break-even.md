# A break-even method for zero-cash offers

Method note, checked 16 Nov 2026. Extracted from working through whether a small project can start earning with no budget. The personal numbers from that exercise are removed; what remains is the reusable method, plus worked examples with invented, clearly labeled inputs. Fees cited were checked on official pages on the date above and can change.

## The problem with "zero cash" math

When cash invested is exactly zero, cash ROI is undefined - division by zero - and when the outlay is merely tiny, ROI swings so wildly it stops being a useful signal. The real input is time, and time is exactly what most back-of-envelope plans leave out. A plan that "costs nothing" can still lose months.

So score every offer twice:

1. **Cash break-even** - the sales volume where cash in covers cash out. With free tools this is often the very first sale, which is why zero-cash plans look better than they are.
2. **Economic break-even** - the sales volume where cash in covers cash out *plus* the hours, valued at an explicit hourly rate. The rate is a valuation assumption you choose as a decision rule, not a claim about the market. Say it out loud in the plan.

A scenario that beats cash break-even but misses economic break-even is losing money once time is counted. Write that down openly instead of hiding it in gross revenue.

## The working rules

- **Value time explicitly.** Pick an hourly rate, state it as an assumption, and multiply it through every scenario. Repeatable work drops the hours on later rounds (a second cohort of a workshop reuses its prep), so model round two separately.
- **Scenarios are not forecasts.** Every sales number is an invented input until someone pays. Label scenarios as scenarios, and never let a scenario table read like a ranking of likelihood. No observed demand is not proof of no demand; it is proof you have not measured yet. Asking for payment before the thing is fully built is one way to measure intent instead of applause - but pre-selling creates real obligations: you owe the delivery or the refund, so scope and refund terms need to be written first, and prepayment rules vary by jurisdiction.
- **Verify fees on the official pages, on the day.** Platform fees change. Record the check date next to the numbers and re-verify before relying on them. Your own bank's or payout provider's fees are a separate check - mark them unverified until done.
- **Check the payout route before counting the income.** A platform can accept you as a seller and still have no practical way to pay you where you live. Confirm the payout method works for your country and bank at setup, before the revenue is in the plan.
- **A deposit is not profit.** Money collected before delivery is working capital plus a refund liability - you owe the work or the money back. A deposit-funded offer only makes economic sense if the price beats the hours, and the scope and refund terms must be written before taking anyone's money.
- **Near-zero cash assumes equipment you already have.** A working laptop, internet, and free-tier accounts. Replace any of those and real costs appear. Free tiers also carry limits and pauses; if the offer grows past them, hosting becomes a real cost line.
- **Taxes may apply to any income, depending on your jurisdiction - check yours.** Keep the line in the model even when examples ignore it.

## Worked example (hypothetical)

Inputs are invented to show the arithmetic, not observed results: a digital download priced at $15, sold in USD to a buyer outside the US (Lemon Squeezy's own example applies its 1.5% fee based on the transaction being outside the US, so the buyer side is what matters here), with no sales tax or VAT added. Fee figures are the real published ones as of the check date. Totals are computed unrounded and rounded for display.

- Gumroad charges 10% + $0.50 per direct sale, plus card processing at 2.9% + $0.30. On $15.00 that is $1.50 + $0.50 + $0.435 + $0.30 = $2.735 in fees, so one sale nets **$12.265** (about $12.27) before any payout or tax.
- Lemon Squeezy charges 5% + $0.50 of the total order value, plus 1.5% for international (outside-US) transactions: $0.75 + $0.50 + $0.225 = $1.475, so one sale nets **$13.525** (about $13.53), before its payout fee. Payout fees are separate from the sale fees above and depend on the payout method and the seller's bank region and settlement currency - for example 1% for Stripe payouts to bank accounts outside the US.
- If making the download takes 35 hours valued at an assumed $12 per hour, imputed labor is $420. Economic break-even is $420 / $12.265, about **35 sales** on Gumroad, and $420 / $13.525, about **32 sales** on Lemon Squeezy. Treat both as lower bounds: payout fees, refunds and any taxes would push the real break-even higher.
- Ten sales in month one nets $122.65 in cash against $420 of time: a clear loss on paper, which only turns if copies keep selling after launch without much new work.

That last line is the whole point of the method: the product shapes (downloads, tools, subscriptions) look worst in month one because the hours come before the sales, and only win if later copies need much less work per sale. The hours-first shapes (workshops, mentoring, services) reach cash sooner but repeat the hours with every sale. Neither is better in general; the method exists to make the trade explicit instead of accidental.

## Sources

- [Gumroad pricing](https://gumroad.com/pricing) and [Gumroad's fees](https://gumroad.com/help/article/66-gumroads-fees)
- [Lemon Squeezy fees](https://docs.lemonsqueezy.com/help/getting-started/fees)
