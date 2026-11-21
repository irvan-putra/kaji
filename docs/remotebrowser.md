# Remote Browser

Checked21November2026 against source commit b872ef227d815be4ff9e93c7a0e72335fbfbcbb7. Public generic explainer only, no install/runtime test/account activity.

## Important distinctions

- Browser fleet versus automation client/model.
- Dedicated VM design is documented, not audited here; no negligible-overhead guarantee repeated.
- Local Docker socket quick start is not a production deployment recipe.
- Harness forwards page/task content to configured model; script verification is explicitly not sandboxing.
- Production PostgreSQL requirement versus source-development PGlite fallback.
- VM defaults are2vCPU/4G per browser, not total-host sizing.
- AGPL network clause is conditional on modified program; no blanket legal conclusion.

## Sources

- https://github.com/remotebrowser/remotebrowser/blob/main/docs/index.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/getting-started.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/self-hosting.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/setup.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/isolation.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/sandboxing.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/api.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/sdk.md
- https://github.com/remotebrowser/remotebrowser/blob/main/docs/harness.md
- https://github.com/remotebrowser/remotebrowser/blob/main/package.json
- https://github.com/remotebrowser/remotebrowser/blob/main/Dockerfile
- https://github.com/remotebrowser/remotebrowser/blob/main/src/config.js
- https://github.com/remotebrowser/remotebrowser/blob/main/LICENSE
- https://remotebrowser.ai
