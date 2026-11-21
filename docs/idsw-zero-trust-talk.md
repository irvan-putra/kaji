---
id: idsw-zero-trust-talk
type: research-note
---
# import zerotrust: an IDSW talk, checked (source note)

Public page: https://vanipy.com/kaji/zero-trust/ . Reading of the IDSW 2026 session "import zerotrust: Network Security as a Dependency, Not a Ticket" (21 Nov 2026, 14:20-14:50, listed speaker Affan Basalamah per the official agenda), based on seven photographed slides that are not reproduced.

## Claim-check results (checked 21 Nov 2026)

- CVE-2026-109618 (php2shell): confirmed, PHP Group CNA CVSS 4.0 9.2; CISA KEV 26 Oct; fixed 8.2.35/8.3.36/8.4.27/8.5.12. Sources: NVD, CISA 21 Oct alert, Cyber Centre AL26-026.
- "Node2Shell CVE-2026-111947 9.2": identifier mismatch. CVE-2026-111947 is a WordPress Pricing Table plugin authorization bypass, CVSS 3.1 5.5 (WPScan CNA, GHSA-42jx-58g4-6w6f). No Node.js RCE under this ID found.
- CVE-2026-114938 (Java4Shell): real, CISA 17 Nov alert, HotSpot x86-64 Base64 decoder; NVD lists Oracle CVSS 3.1 8.1, not 9.2.
- CVE-2026-42533 (NGINX map regex): confirmed; Ubuntu shows CVSS 4.0 9.2 and CVSS 3.1 8.1 for the same flaw; RCE needs ASLR disabled/bypassed, otherwise DoS; data plane only.
- CVE-2026-121481 (OpenSSL EVP_EncodeBlock): Ireland NCSC prints 9.8, but its body says no attacker-triggerable path identified and the caller must supply a near-INT_MAX length; NVD awaiting enrichment; OpenSSL PR 33652 labeled severity important, project discussion says Low.
- FBI/ARTEX: verified. IC3 FLASH-20261113-001, 13 Nov 2026, TLP:CLEAR. Sub-3-hour intrusions, ~67k records (South Korean financial institutions), ConnectWise 2,250+ tenants; recommends moving enterprise apps behind Zero Trust access where feasible, alongside patching and identity hardening. IOCs are point-in-time.

## Deployment models (OpenZiti docs)

Network access (edge router, no code changes, port still open inside zone), host access (tunneler, localhost only, host OS is boundary), application access (SDK in-process, no listening ports, strongest). Quickstart recommends starting with host access. NIST SP 800-207: no implicit trust from network location; per-session authorization; continual re-evaluation.

## Limits stated on the page

Zero trust reduces exposure; it does not patch CVEs; it cannot see caller-side defects (OpenSSL case); it moves trust to the controller/enrollment/policy plane, which then needs the same care as any identity system.

## Speaker takeaway slide (added 21 Nov 14:49 WIB)

Eighth photo from the user (WhatsApp 14:48:31, message id ending QzhBNTU4AA==), relayed through main agent's inline inspection: the speaker's closing position revises indiscriminate immediate patching toward (1) prioritizing urgent patches with orderly scheduled backend patching, (2) active mitigation instead of doing nothing, (3) machine/device identity over IP-based trust, (4) hiding/restricting exposure through zero trust. Rendered as the speaker's takeaway with the page's own cautions: exploited and internet-facing defects remain patch-now items, and zero trust mitigates exposure without closing the defects.
