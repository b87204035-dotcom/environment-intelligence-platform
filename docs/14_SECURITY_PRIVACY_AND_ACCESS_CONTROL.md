# 14 Security, Privacy and Access Control

## 1. Roles
- System administrator
- Organization administrator
- Project manager
- Environmental professional
- Field investigator
- Reviewer/approver
- Client read-only user
- Public viewer for explicitly published material

## 2. Access model
Use organization and project scoped role-based access control. Default deny. Sensitive project data, parcel information, field photos, personal contacts and unpublished reports are private.

## 3. Authentication
- External identity provider compatible architecture
- MFA required for administrators and approvers
- Short-lived access tokens and rotated refresh tokens
- Session revocation and device history
- Service accounts for synchronization workers with least privilege

## 4. Data protection
- TLS in transit
- Encryption at rest for databases, object storage and backups
- Secrets in a secret manager, never committed
- Signed URLs for private files
- Malware scanning and file-type validation for uploads
- EXIF privacy controls; preserve GPS only when project policy permits

## 5. Audit
Record logins, exports, source changes, AI generations, approvals, report publication, permission changes, downloads and deletions. Audit logs are append-only and retained by policy.

## 6. AI privacy
- Do not send private project content to an AI provider unless the organization permits it.
- Record provider, model, data-retention setting and prompt version.
- Support redaction of personal data and confidential client identifiers.
- Generated text is never automatically approved.

## 7. Backups and recovery
- Automated encrypted backups
- Point-in-time database recovery
- Object-store versioning
- Quarterly restore test
- Documented RPO/RTO targets before production launch

## 8. Security acceptance criteria
- Authorization tests for every protected API
- No secrets in repository or images
- Dependency and container scanning in CI
- Rate limits and upload limits
- OWASP-oriented API and web tests
- Production security review before public deployment.