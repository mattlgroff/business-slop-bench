# MiMo ZDR route refresh

The saved pilot-v19 catalog advertised no ZDR route for `xiaomi/mimo-v2.6-pro`, and its ZDR-enforced request returned HTTP 400 with no available ZDR provider. That failure remains recorded, including its retained reservation.

The pilot-v22 and pilot-v23 snapshots advertise some ZDR routes. A fresh public Gateway catalog lookup confirms that status; see [timestamped catalog evidence](catalog.json). This warrants a new attempt with ZDR enforcement, not a non-ZDR exception. Catalog availability and successful routing do not independently audit provider retention practices.

The new pilot-v23 collection uses the unchanged task set and writer settings, including no output-token cap or harness deadline. All 16 calls completed with ZDR enforcement and are reviewed in [assistant-v42](../assistant-v42/REPORT.md). Sonnet scheduling was held at its between-call wait to avoid competing for the shared ledger lock. The exit trap resumed it, its process state returned to running, and its next request completed successfully. The seven-minute minimum spacing was preserved.
