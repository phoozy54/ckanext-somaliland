# Somaliland Open Data Portal — CKAN Extension

🇸🇱 **Open-source branding and customisation extension for the Somaliland Open Data Portal** — Somaliland's first open data platform, built on [CKAN](https://ckan.org), the open-source data portal engine used by the UK, US, Canada, Oman, and the Humanitarian Data Exchange.

This repository contains `ckanext-somaliland`, a CKAN extension that customises the platform with Somaliland's identity: branding, navigation, a custom homepage, and an "About" page — without modifying CKAN's core code.

## About the Project

The Somaliland Open Data Portal aims to give citizens, researchers, journalists, NGOs, and government institutions free, reliable access to public data about Somaliland — population, health, education, economy, agriculture, infrastructure, displacement, and geospatial information.

Modeled conceptually on portals like Singapore's [data.gov.sg](https://data.gov.sg), London's [Datastore](https://data.london.gov.uk), and Oman's [National Open Data Portal](https://opendata.gov.om), this project uses entirely original code, design, and branding tailored to Somaliland's own identity and needs.

## What This Extension Does

- Custom homepage with a hero section, search, and topic-based dataset browsing
- Original logo and visual identity using Somaliland's national colours
- Custom "About" page describing the portal's mission
- Customised footer (Feedback, Open Data Licence, Privacy & Terms)
- Dark, cohesive navigation theme

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

🚧 **Active development — v0.1.0.** Branding and homepage are complete. Real datasets and public deployment are in progress.

## Roadmap

- [ ] Publish first real Somaliland datasets (population, health, education)
- [ ] Public deployment with a registered domain
- [ ] Submission to [DataPortals.org](https://dataportals.org), the global open data portal directory
- [ ] Partnership outreach to Somaliland government institutions

## License

This extension is released under the [AGPL-3.0 License](LICENSE), consistent with CKAN's own licensing.

## Author

Built by **Foosi Mohamed Jama** — [github.com/phoozy54](https://github.com/phoozy54)

---

*This project is an independent, community-built initiative and is not yet an official government platform.*