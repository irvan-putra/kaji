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

## Latency and alternatives section (added 21 Nov 14:52 WIB)

User follow-up 14:50:17 WIB: research how much latency zero trust could add, and the alternatives. Grounding: OpenZiti characterization wiki (control-plane Create Session mean ~12-29 ms by model size), OpenZiti discourse thread 4625 (maintainer, May 2025: no independent overhead studies, measure your own network, scale horizontally with routers), Tailscale official performance best practices (direct connections nearly always lower latency, relay fallback slower), and one developer's June 2026 small-VPS benchmark comparing Cloudflare Tunnel / Tailscale / Nebula / OpenVPN vs direct (used for pattern, labeled as one setup). Alternatives table covers app-embedded (OpenZiti SDK, tsnet, SPIFFE/mTLS, service mesh), host mesh (Tailscale, NetBird, ZeroTier), managed edge (Cloudflare Tunnel), identity-aware proxies (Teleport, Pomerium, Boundary) and classic VPNs. No benchmark against user infrastructure was run or authorized.

## Controller hiding section (added 21 Nov 14:53 WIB)

User question 14:52:37 WIB: the speaker said the new version also hides the controller, user confused. Verified against OpenZiti v2.0 announcement (controller APIs bindable over the overlay, "the controller is dark", --network-identity login), the 1.8 management-plane blog (XWeb overlay bindPoints), and the add-by-URL blog (enrollment bootstrap: enrollment JWT out-of-band vs URL + IdP sign-in, auto-enroll in 2.0). Page section attributes the claim, confirms it for the management/control plane, and keeps the two boundaries explicit: routers still accept connections, and one small enrollment path stays reachable.

Correction pass 14:53 WIB after main review: management API is not the whole control plane. Section now names the three API surfaces (management, fabric/router control channel, client edge API for auth and enrollment), states management+fabric are the surfaces that can bind over the overlay, keeps the client edge API and routers as the reachable remainder, and notes overlay binding is a supported configuration, not the out-of-box default.

## Naming sidebar (added 21 Nov 14:59 WIB)

User asked whether ziti pasta inspired the name and asked to add it to Kaji. Added a short sourced aside after the intro: NetFoundry's own blog (Philip Griffiths) says Ziti is a code name from the letters Z T, connected to Zero Trust, with pasta mascot Ziggy leaning into the coincidence. Attribution preserved; the aside does not claim the pasta played no role.

## Daughter explanation addition (21 Nov 2026, 15:06 WIB)
- User asked to bring the NetFoundry article's explanation into the page, especially the explanation to the daughter (WhatsApp 15:04:50 and 15:05:15).
- Source: Philip Griffiths, "Demystifying the Magic of Zero Trust Networking with my Daughter", NetFoundry blog, July 2024: https://netfoundry.io/ziti-openziti/demystifying-the-magic-of-zero-trust-networking-with-my-daughter/
- Added section "Zero trust, explained to a daughter": castle-and-moat-to-city background, three tiers (relabeled VPN/firewall proxy, software-defined perimeter, app-embedded SDK) in fresh wording with attribution and link; vendor "impossible" claim labeled as such.
