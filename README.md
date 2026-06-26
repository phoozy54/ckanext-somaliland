# Somaliland Open Data Portal — CKAN Extension

🇸🇱 **The first open data infrastructure built for Somaliland.**

## Why This Exists

Somaliland gained its first recognition by a United Nations member state in late 2025, marking a turning point in its standing on the world stage. Diplomats, international organisations, investors, journalists, and researchers are now paying attention to Somaliland in a way they never have before — and most of them have nowhere reliable to turn for basic facts about the country.

There is no public, centralised source for Somaliland's population figures, health statistics, education data, or economic indicators. Information that should take minutes to find is scattered across PDF reports, outdated spreadsheets, or simply does not exist online at all. This is the gap the Somaliland Open Data Portal exists to close.

This repository contains `ckanext-somaliland`, the CKAN extension that powers the portal's identity, branding, and public-facing experience — built independently, in the open, by a Somaliland developer.

## What This Means for Somaliland

A functioning national open data infrastructure is not a luxury — it is groundwork for almost everything else a young, internationally re-engaging country needs to do:

- **Government planning** improves when ministries can see and share reliable data on population, health, and infrastructure rather than relying on outdated estimates.
- **International partners** — the UN, World Bank, NGOs, and foreign governments — move faster and commit more confidently when they can verify facts about Somaliland themselves, instead of relying on secondhand or incomplete sources.
- **Transparency and trust** grow when budgets, statistics, and public records are open by default, which matters enormously for a nation building credibility as a newly recognised state.
- **Local businesses and entrepreneurs** gain a foundation to build on — market data, demographic data, and geographic data that startups in more established countries take for granted.
- **Somaliland's own institutions** gain a reusable, low-cost platform rather than needing to build expensive, one-off systems from scratch.

## What This Means Internationally

Open data portals are how the rest of the world already operates. Singapore's data.gov.sg, the UK's data.gov.uk, the United States' Data.gov, and Oman's National Open Data Portal all run on the same underlying philosophy — and several, including the UK and US, run on the very same open-source platform this project is built on: CKAN.

By building Somaliland's portal on this same proven foundation, the country is not starting from zero or improvising something makeshift — it is adopting the same standard of data infrastructure used by national governments worldwide, including a fellow open data initiative for the African continent, openAFRICA. That matters for how seriously international partners take what Somaliland is building.

## About the Project

This extension customises CKAN — the open-source data portal engine used by the UK, US, Canada, Oman, the Humanitarian Data Exchange, and dozens of governments worldwide — with Somaliland's own identity: branding, navigation, a custom homepage, and an About page, without modifying CKAN's core code.

Modeled conceptually on portals like Singapore's [data.gov.sg](https://data.gov.sg), London's [Datastore](https://data.london.gov.uk), and Oman's [National Open Data Portal](https://opendata.gov.om), this project uses entirely original code, design, and branding tailored to Somaliland's own identity.

## What This Extension Does

- Custom homepage with a hero section, search, and topic-based dataset browsing
- Original logo and visual identity using Somaliland's national colours
- Custom About page describing the portal's mission
- Customised footer (Feedback, Open Data Licence, Privacy & Terms)
- A cohesive, dark navigation theme

## Tech Stack

- **CKAN 2.10** — core data portal engine (Python/Flask)
- **PostgreSQL** — database
- **Solr** — search
- **Redis** — caching
- **Docker** — local development and deployment
- **Jinja2** — template overrides (no core CKAN files modified)


## Local Development

This extension is designed to run inside a CKAN Docker environment. See [ckan/ckan-docker](https://github.com/ckan/ckan-docker) for the base setup instructions.

1. Clone this repository into your CKAN project's `src/` directory
2. Install the extension: `pip install -e .`
3. Add `somaliland` to your `CKAN__PLUGINS` environment variable
4. Restart CKAN


## Status

🚧 **Active development — v0.1.0.** Branding, identity, and homepage are complete. Real datasets and public deployment are in progress.

## Roadmap

- [ ] Publish first real Somaliland datasets (population, health, education)
- [ ] Public deployment with a registered domain
- [ ] Submission to [DataPortals.org](https://dataportals.org), the global open data portal directory maintained by the Open Knowledge Foundation
- [ ] Partnership outreach to Somaliland government institutions and international organisations

## License

Copyright (C) 2026 SOMALILAND OPEN DATA

This project's original code, templates, and design (the `ckanext-somaliland` extension) are licensed under the **GNU Affero General Public License v3.0** — the same license used by CKAN itself. See [LICENSE](LICENSE) for the full text.

This means: anyone is free to use, modify, and redistribute this code — including running it as a public service — provided that any modified version is also made available under the same license, with its source code accessible to users.

## License

Copyright (C) 2026 Foosi Morris

This project's original code, templates, and design (the `ckanext-somaliland` extension) are licensed under the **GNU Affero General Public License v3.0** — the same license used by CKAN itself. See [LICENSE](LICENSE) for the full text.

This means: anyone is free to use, modify, and redistribute this code — including running it as a public service — provided that any modified version is also made available under the same license, with its source code accessible to users.

## Author

Built by **Foosi Morris** — [github.com/phoozy54](https://github.com/phoozy54)
---

*This is an independent, community-built initiative and is not yet an official government platform.*
