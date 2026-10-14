# Rinehart Oil website review

Independent owner-requested design review. Public source: https://www.rinehartoil.com/. Local computer working project; no cloud execution project.

Working source and staged output live in this repository. Coordination, dated source captures and acceptance evidence: `AI\Projects\Rinehart-Oil-Website-Redesign-Content-Migration`.

Build: `python scripts/build.py` on the CWU workstation (requires its coordination source inventory and BeautifulSoup capture dependency). Browser verification: `node scripts/verify.cjs http://127.0.0.1:8769/` with Playwright available. Serve locally with `python -m http.server 8769 --bind 127.0.0.1`.

The review uses no analytics, login or form backend. Applications and working customer tools link to the official site. Public source files and images have a provenance manifest; production rights and content currency require owner review. Source stock photography with unclear reuse rights is excluded. Original source photo attribution to Kevin Falerios is retained.

The source-linked 2023 driver application returns 404. The review preserves the official handoff; it does not claim that document is available. Historical resource notices and the legacy privacy policy are labeled as retained reference.

Upcoming: owner will announce images in `AI\Media\Incoming`. Incorporate only approved Rinehart images with provenance and rerun responsive checks.


Media attribution update, October 14, 2026: the owner states that they assume ownership of supplied/source material and authorizes removal of the Kevin Falerios public photo credit and link. This records the owner instruction; it is not an independent chain-of-title determination. The photos remain unchanged.


### Required Release Link Guard

Owner forbids public old-site fallback/comparison links. Run `python scripts/check_release_links.py` before release. `site-link-policy.json` records blocked legacy hosts; generation and `.githooks/pre-push` enforce the check. Configure a fresh clone with `git config core.hooksPath .githooks`. Valid supplier services, mailto/tel and retained local documents remain supported. Source provenance belongs to coordination records, never public migration callouts.
