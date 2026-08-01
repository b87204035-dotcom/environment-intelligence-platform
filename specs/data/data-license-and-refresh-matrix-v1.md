# Data License and Refresh Matrix v1

## Refresh policy

The platform checks every active source at least monthly, even when the publisher's stated update frequency is annual or irregular. A check is not the same as a new data publication.

| Publisher frequency | Check cadence | Stale threshold | Publication behavior |
|---|---:|---:|---|
| Daily | Daily | 3 days without successful retrieval | Publish validated snapshot automatically |
| Monthly | Weekly | 45 days after expected update | Publish after schema and count validation |
| Six-monthly | Monthly | 210 days | Retain prior version and flag overdue |
| Annual | Monthly | 400 days | Retain prior version and show source year |
| Irregular | Monthly | No artificial stale claim; show last publisher date | Alert only for endpoint failure or announced replacement |

## License classes

1. Government Open Data License v1: reusable subject to attribution and license terms.
2. Public viewing only: may be linked or viewed but not necessarily copied into the database.
3. Application required: unavailable until credentials and terms are recorded.
4. Restricted/confidential: project-only storage with tenant access control.
5. Unknown: blocked from production use.

## Mandatory UI fields

Every section, table, chart and GIS layer shall display or expose:

- source agency
- dataset title
- data period
- publisher update date
- platform last successful synchronization
- refresh frequency
- license class
- source status: current, due, stale, unavailable or retired

## Failure rules

- Never overwrite a valid production version with a failed or incomplete import.
- Preserve immutable raw files and checksums.
- Create a validation report for row counts, null rates, geometry validity, duplicates, units and code lists.
- Notify operations when a source becomes stale, changes schema, redirects, disappears or changes license.
- Do not silently substitute another source.