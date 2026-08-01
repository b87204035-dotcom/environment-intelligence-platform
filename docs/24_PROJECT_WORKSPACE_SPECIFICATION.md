# 24 Project Workspace Specification

## Core entities
Organization, project, client, contact, site, parcel, address, project member, task, milestone, observation, media, document, report, sample, borehole, monitoring well, legal assessment and approval.

## Project states
Lead → Proposal → Active → On hold → Review → Completed → Archived.

## Workspace tabs
- Overview and status
- Sites/parcels/addresses
- Timeline and tasks
- Environmental baseline
- GIS
- Field survey
- Samples/boreholes/wells
- Documents and media
- Article 8/9 assessment
- Control/remediation plans
- Reports and exports
- Approvals and audit

## Document control
Each document stores type, version, status, owner, confidentiality, checksum, source, effective date and superseded relation. Published documents are immutable; corrections create a new version.

## Timeline
Automatically records material events while permitting user-entered milestones. Events link to the actor and affected object.

## Search
Search project names, clients, addresses, parcels, pollutants, industries, methods, documents and observations subject to permission.

## Reuse and knowledge
Approved, non-confidential project content may be deliberately promoted to the organization knowledge base. Private project content is not reused by default.

## Acceptance
A project manager can create a project, add a site/parcel, invite members, capture field observations, attach documents, run environmental baseline retrieval, draft reports, request approval and export a versioned deliverable.