# Rinehart Oil Website Review

Owner-requested, local-computer website redesign published as a staged, noindex review at https://ukiahcomputerworks.github.io/rinehart-review/. The existing production website and DNS are outside this preview release.

## Current Features

- Five main pages: Home, Fuel Transport (including Fleet), Our Story, Careers, and Contact & Dispatch. Privacy is a footer utility; existing Cardlock customers retain a temporary support page.
- Ten former pages redirect to relevant retained destinations. Retail/wholesale sales pages, historical resource catalogs and the unfinished online application are out of the public journey. Original files and Git history remain preserved.
- Compact shared navigation/footer, native disclosures, direct dispatch contact, office-number chooser and the approved charcoal, riveted-steel and diamond-plate shimmer.
- Four selected fleet photos, with two behind More Fleet Photos. Full company history and driver qualifications expand on request.
- No application collection. Careers directs visitors to the office for current openings and submission instructions. HR replacement and secure processing remain COM-493.

## Build And Verification

Run `python scripts/build.py`. `scripts/transport_site.py` and `scripts/transport-content.json` are the canonical transport-first generator and retained content. The old `driver_form.py` command is a compatibility entry point for the same build; it cannot republish the unfinished form. Earlier migration helpers remain historical and are not part of this build.

```text
python scripts/check_release_links.py
python scripts/check_action_intent.py
python scripts/apply_colophon.py --check
node scripts/verify.cjs http://127.0.0.1:8770/
```

A fresh clone uses `git config core.hooksPath .githooks`. The pre-push hook checks destinations, retired-content boundaries, contact actions and the shared colophon. Serve locally with `python -m http.server 8770 --bind 127.0.0.1` for browser checks. Dated acceptance evidence belongs in the coordination PROJECT.md; deployment is not owner acceptance.

## Source, Privacy And Ownership

Public migration source: https://www.rinehartoil.com/. Captures, original documents, provenance and acceptance records belong to `AI/Projects/Rinehart-Oil-Website-Redesign-Content-Migration`; implementation belongs to this repository.

The site has no first-party analytics, advertising tracker, login or application backend. The host can log visitor IP addresses. The Contact page embeds Google Maps, which connects to Google; the privacy notice identifies that service. Phone and email links open the visitor's own applications. No old-site fallback, comparison or placeholder links are permitted in visitor-facing pages.

The owner instructed removal of the former photographer credit and states that they assume material ownership. Provenance records preserve that instruction; it is not an independent chain-of-title finding. The review retains recognizable source and supplied photographs. Historical documents remain in preserved assets and source records, outside the public marketing journey.

## Outstanding Acceptance

COM-493 owns approved secure HR processing, server-side validation, retention/access ownership and an authorized synthetic receipt at the selected HR destination. COM-492 remains in owner review. Native saved On computer project registration is not established by this repository or by Linear. Production cutover remains a separate phase.
