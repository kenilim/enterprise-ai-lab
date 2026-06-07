# Document-to-Spec Pilot Inputs

## Folder Roles

### inbox

Landing zone for newly received files.

Files placed here are not automatically approved, committed or processed.

### canonical-source-pack/raw

Local immutable copy of the approved benchmark source pack.

These raw files remain local and are excluded from GitHub.

### generated-synthetic-evidence

Reproducible artificial enterprise-style evidence generated from the canonical
source pack.

Examples may include synthetic emails, meeting notes, spreadsheets, slides,
PDF summaries, screenshots, stale requirements and conflicting requests.

## Processing Rule

Raw documents must remain local.

Only safe metadata, manifests, scripts, sanitised synthetic fixtures and
reviewed outputs should be committed to Git.
