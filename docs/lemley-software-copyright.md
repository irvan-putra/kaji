# Reading note: The End of Software Copyright

Read: 16 November 2026

## Assessment

Important as a warning about ownership claims in AI-heavy software, but the title is a forecast and argument, not a statement that software copyright has already been abolished. The strongest practical point is that owning a repository or receiving an assignment of AI output does not by itself establish copyright in machine-generated expression. The paper itself preserves protection for human contributions and ultimately describes human-AI collaboration as perhaps the most likely future.

## Paper and access

Mark A. Lemley, *The End of Software Copyright*, date written 29 October 2026; SSRN posted 11 November 2026. Full 32-page PDF obtained from SSRN and read, including footnotes. This is a doctrinal/policy essay, not a new experiment measuring model outputs. No journal publication or peer-review status was established. The downloaded version contains unfinished citation placeholders, so treat it as a draft.

Original: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7682724

PDF download link observed on that page: https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=7682724&mirid=1

## Argument

- **Copied proprietary code, pp. 13-14:** the output may infringe. Lemley argues that infringement pervading a derivative work can also defeat protection for intermingled original contributions. He distinguishes fully separable contributions.
- **Copied copyleft code, pp. 14-16:** compliance can require licensing a covered distributed derivative work on copyleft terms. This is not the same as absence of copyright. The original copyright and enforceable license conditions are what make copyleft possible.
- **New machine-generated code, pp. 16-18:** lack of human authorship can leave the generated expression without copyright under U.S. law. The paper expressly says this does not infect separately human-authored material.
- **Business responses, pp. 19-31:** patents, secrecy and contracts are imperfect substitutes. Four scenarios are free software, widespread infringement, legal expansion of copyright, and mixed human-AI authorship. He calls widespread infringement least likely (p. 25), and "muddling through" perhaps most likely (p. 28).

## What is well supported

The U.S. Copyright Office confirms that purely machine-generated expression is different from human authorship, and that prompts alone generally do not by themselves establish sufficient human control over the resulting expression. But it also confirms that AI assistance does not disqualify a work and that creative human arrangements or modifications can qualify. This supports a narrower warning about the scope and proof of protection, rather than a blanket rule that all AI-assisted software is uncopyrightable.

Provenance matters in two directions: establishing what a human authored and identifying third-party material and license conditions. The paper's pp. 30-31 make the evidentiary problem especially clear. An ordinary commit records who committed a change, not necessarily whether the expression came from that person or a model.

## Reservations and errors

1. **The open-source branch is overbroad.** Footnote 52 (p. 15) admits non-copyleft licenses have been most popular for some time, despite the abstract's claim about "most" open-source licenses being viral. Footnote 7 (p. 3) incorrectly calls MIT "weak copyleft." The MIT text permits use, modification, sublicensing and sale subject to preserving its copyright and permission notice; it does not require publishing the surrounding program's source. Copyleft obligations also depend on the actual license, covered material, kind of combination and triggering acts. Neither public GitHub visibility nor use of an AI tool establishes those facts.
2. **The adoption statistic is overstated.** The introduction says nearly 90% of coders use AI tools to write software. Its cited 2025 Stack Overflow source actually says 84% of respondents use **or plan to use** AI tools in their development process. Intent is not current use, and use somewhere in development is not proof AI authored a particular program. The same survey reports most respondents were not vibe coding. The paper itself quotes the broader survey wording correctly in footnote 4. This limits the statistic's support for the scale and timing of the forecast; it does not refute the conditional legal analysis. Even widespread AI-tool adoption would not establish what proportion of a program's expressive content was machine-authored.
3. **One copied snippet does not automatically erase an entire repository's copyright.** Section 103(a) excludes parts employing material unlawfully, and the legislative notes explicitly preserve unaffected parts. How extensively infringement pervades a derivative work is material. Lemley acknowledges separability on p. 14. Applying his broad conclusion to a specific codebase needs facts and legal analysis.
4. **Forecasts are not measured findings.** The essay does not supply a new representative audit of current AI-generated code, a measured split between copied and novel output, or evidence that cheap generation guarantees inexpensive reliable maintenance. It acknowledges uncertainty about memorization (fn. 56, p. 16). Draft placeholders include "[cite]" in fn. 33 and unresolved supra references. These do not refute the legal argument, but they lower confidence in categorical empirical claims.
5. **Jurisdiction matters.** The analysis is mainly U.S.-law-based and acknowledges differing treatment elsewhere (fn. 58, p. 17). This reading is not an assessment of Indonesian law, a worldwide ownership conclusion, or advice about a particular project's license.


### Notice requirements are not the same as copyleft

MIT is not obligation-free. Its license requires preserving the copyright and permission notice in copies or substantial portions of the software. But it permits modified and larger works to be distributed under different terms and without source code. That is why it is classified as permissive, not weak copyleft.

Copyleft concerns reciprocal licensing of covered downstream material. "Weak" copyleft limits the scope of that reciprocity; it does not mean merely that a license has a small condition such as retaining a notice. For example, Mozilla describes MPL 2.0 as file-level copyleft. When distributing modified MPL-covered source files, those files stay under MPL; when distributing executable form, the covered source must be made available and recipients told how to obtain it. Separate new files containing no MPL code can remain under different, including proprietary, terms. This does not automatically require opening the entire combined application.

The distinction matters to the paper's argument: copying MIT-licensed code can create a notice obligation without forcing the surrounding application to become open source. Copying copyleft code calls for a different, license-specific analysis of the covered material and the acts that trigger its conditions.

Sources checked 16 November 2026:

- MIT's actual terms: https://opensource.org/license/mit
- MIT classification and downstream terms: https://choosealicense.com/licenses/mit/
- MPL scope and examples, especially Q1 and Q8-12: https://www.mozilla.org/en-US/MPL/2.0/FAQ/
- MPL 2.0, sections 1.10 and 3.1-3.4: https://www.mozilla.org/en-US/MPL/2.0/

## Practical reading

Do not infer "AI code is free of legal risk," "all open source forces disclosure," or "all software ownership has disappeared." A more defensible takeaway is: claim only rights actually held; preserve evidence of substantive human expression; check dependencies and third-party licensing; and do not confuse inability to claim copyright with permission to copy someone else's protected material. No existing license or copyright notice should be changed solely because of this essay.

## Sources checked

1. Full paper and identity/version: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7682724
2. U.S. Copyright Office's official explanation of AI-assisted authorship and creative human arrangements/modifications: https://newsroom.loc.gov/news/copyright-office-releases-part-2-of-artificial-intelligence-report/s/f3959c36-d616-498d-b8f9-67641fd18bab
3. Copyright Office report status: https://www.copyright.gov/ai/
4. U.S. statute and legislative explanation of unlawful material and unaffected contributions: https://uscode.house.gov/us/usc/t17/s103/
5. Actual MIT license terms: https://opensource.org/license/mit
6. Actual cited adoption survey: https://survey.stackoverflow.co/2025/ai

These primary/official sources were opened, not inferred from search snippets. The GNU GPL page fetch failed; no claim of independently reviewing the complete GPL text is made. This is a reading assessment, not an exhaustive case-law or international-law audit.
