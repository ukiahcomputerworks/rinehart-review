# Rinehart Oil Website Review

Owner-requested, local-computer website redesign published as a staged, noindex review at https://ukiahcomputerworks.github.io/rinehart-review/. The existing production website and DNS are outside this preview release.

## Current Features

- Seventeen pages with original RINO branding, original and owner-supplied photography, Title Case headings, polished silver framing and independently timed shimmer.
- Compact mobile layouts, full-card service links, grouped navigation, one quiet service/history assurance strip and the ComputerWorks.ai colophon integrated into the existing footer.
- Documents: sixteen downloads in two searchable folders. Links: seventeen external resources in full category lists with a silver selection-transfer effect and portrait photo detail card.
- Contact: aligned image actions, a choice between the 707 and 800 office numbers, three department disclosures, office hours, and an always-visible Google map. The directions artwork opens the selected station Street View.
- Seven-page credit packet with 246 fillable PDF fields and checkboxes. Users download, fill, save, sign, then email an attachment or print and mail it. The website does not collect credit-application data.
- Seven-step driver application preview with all ten owner-specified qualification requirements. It sends no application data and uses no browser storage. Secure HR processing and verified delivery remain pending.

## Build And Verification

On the CWU workstation, run `python scripts/driver_form.py` to build all pages and the driver preview. This requires the owning coordination folder's source inventory and BeautifulSoup dependency. The fillable-PDF generator uses the preserved original packet in coordination and the bundled Python runtime with pypdf.

Run these release guards:

```text
python scripts/check_release_links.py
python scripts/check_action_intent.py
python scripts/apply_colophon.py --check
```

Configure a fresh clone with `git config core.hooksPath .githooks`. The pre-push hook checks local destinations, forbidden legacy-site handoffs, owner-approved artwork actions and the shared colophon.

For browser verification, use `node scripts/verify.cjs <site-base-url>` with Playwright available. Serve the repository locally with `python -m http.server 8769 --bind 127.0.0.1`, then use `http://127.0.0.1:8769/` as the base. Dated interaction, PDF save/reopen, motion and desktop/mobile evidence is kept in the coordination folder. `verification.json` records its tested source commit and date; it is evidence of those checks, not production acceptance.

## Source, Privacy And Ownership

Public migration source: https://www.rinehartoil.com/. Captures, original documents, provenance and acceptance records belong to `AI/Projects/Rinehart-Oil-Website-Redesign-Content-Migration`; implementation belongs to this repository.

The site has no first-party analytics, advertising tracker, login or application backend. The host can log visitor IP addresses. The Contact page embeds Google Maps, which connects to Google; the privacy notice identifies that service. Phone and email links open the visitor's own applications. No old-site fallback, comparison or placeholder links are permitted in visitor-facing pages.

The owner instructed removal of the former photographer credit and states that they assume material ownership. Provenance records preserve that instruction; it is not an independent chain-of-title finding. The review retains recognizable source and supplied photographs. Historical documents remain labeled as historical references.

## Outstanding Acceptance

COM-493 owns approved secure HR processing, server-side validation, retention/access ownership and an authorized synthetic receipt at the selected HR destination. COM-492 remains in owner review. Native saved On computer project registration is not established by this repository or by Linear. Production cutover remains a separate phase.
