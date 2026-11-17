# BNI Sandbox Tester prototype (source document, not executed)

Research note. Source examined 17 November 2026.

## Summary

The prototype design proposes an Android app to test connectivity to a local backend and request a balance from the BNI sandbox environment through an SDK. This is a design summary, not a build result or an integration test.

## Scope and status

- The design limits scope to the sandbox and balance-read requests; it does not describe transfers or payment transactions.
- Sandbox credentials are proposed to stay on the backend side, not in the phone app. This is a written design choice, not yet tested.
- The generator, project source, dependency installation, unit tests, APK build, lint, dependency audit, and BNI calls have not been run. The code has not been audited line by line.
- The references listed for the initial design, the BNI SDK README and the Android Gradle Plugin 8.7 release notes, have not been re-verified. The authenticity and security of dependencies have not been checked either.
- The design includes an unfinished checklist. No sandbox test results can be concluded from this design.

## Shortlist of Android-to-bank-API connection options (untested)

The next design proposes the order BNI, BCA, then BRI with the SNAP BI pattern, different from the initial BNI One Gate Payment design.

1. **BNI:** uses the Node.js SDK and the `SnapBI.balanceInquiry()` method. The design states it needs application credentials, an RSA private key, and a channel ID.
2. **BCA:** the design mentions the endpoint `POST /openapi/v1.0/access-token/b2b` followed by a SNAP balance inquiry; the stated requirements include a partner/corporate ID, channel ID, a registered KlikBCA Bisnis account, and a request signature.
3. **BRI:** the design mentions `POST /snap/v1.0/access-token/b2b` and `POST /snap/v1.0/balance-inquiry`; the stated requirements include partner registration, an RSA key, an HMAC signature, and AIS service entitlement. The design states a 15-minute token validity.

All endpoints and requirements above are design claims, not yet verified against official documentation. The proposed principle is to keep bank credentials and keys on the backend, with short-lived internal session tokens in the app. No API connection has been made.

**Documentation check:** the `bni-api/bni-nodejs-sdk` repository and BCA developer documentation are available (links below). The BRI SNAP documentation page is cited in the design but could not be read when checked; its existence cannot be confirmed.

## Open items

The source has not been executed; there is no evidence the BNI sandbox flow works. No decision has been made on whether the prototype will be built or tested. All security statements above are written design, not audit results.

## Sources

- The scope of this note is limited to the design summary; the source code is not included.
- References listed for the initial design: the bni-nodejs SDK README (https://github.com/bni-api/bni-nodejs-sdk/blob/main/README.md) and the Android Gradle Plugin 8.7 release notes (https://developer.android.com/build/releases/agp-8-7-0-release-notes).
