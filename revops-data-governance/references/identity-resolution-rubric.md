# Identity Resolution Rubric

Use this rubric to evaluate proposed account and contact matches before creating or merging records. Every strong key earns points; conflicting evidence blocks automatic decisions. Pass scores clear records for creation or linking; fail scores require human review.

## Account Identity Matching

| Evidence | Strength | Points | Criteria |
|---|---|---|---|
| **Verified Domain (strong)** | Exact canonical domain match (e.g., acme.com) | 30 | Domain extracted from corporate email or verified enrichment source |
| **Verified Domain + Legal Entity** | Domain + exact legal name match | 40 | Both verified from third-party source (e.g., CMS, Crunchbase) |
| **Account Relationship** | Already linked in CRM (e.g., subsidiary/parent, merged entity) | 25 | Account hierarchy clearly documents relationship |
| **Normalised Name Match** | Company names align after removing legal suffixes (Inc, LLC, Ltd) and whitespace | 10 | Fuzzy matching; e.g., "Acme Corp" = "ACME CORPORATION" |
| **Address Match** | Physical HQ address verified; country + city confirm | 15 | Verified from enrichment; addresses drift (M&A, relocation) so use with caution |
| **Employee Count + Country** | 80%+ headcount match + country, no legal entity conflict | 5 | Corroborating signal only; not sufficient alone |

### Decision Thresholds

| Total Score | Decision | Action |
|---|---|---|
| 40+ | **LINK** | Sufficient strong evidence. Merge or link records. Log merge survivor. |
| 25-39 | **REVIEW** | Multiple weak signals but no strong conflict. Show to human. If survivor is clear (older record or more complete), link; else hold. |
| <25 | **CREATE** | Insufficient identity evidence. Create new record. Log search evidence and why no match was found. |

### Conflict Rule (Overrides Score)

If any of these hold, escalate to REVIEW even if score >40:
- Verified legal entities differ (e.g., acme-us.com vs acme-uk.com with different legal names)
- Multiple accounts already tied to the same canonical domain
- Account status contradicts (one is customer, one is prospect, no parent/subsidiary relationship)
- Revenue figures differ materially (e.g., $10M vs $1B ARR on same domain)

## Contact Identity Matching

| Evidence | Strength | Points | Criteria |
|---|---|---|---|
| **Verified Email** | Email address exactly matches existing contact | 35 | Only if email is not a consumer domain (@gmail, @yahoo); corporate emails only |
| **Email + Account** | Email matches AND account linked correctly | 50 | High confidence if account relationship is clear |
| **LinkedIn URN** | Verified LinkedIn profile URN matches exactly | 25 | Less reliable than email; people change jobs, profiles go private |
| **Full Name + Account + Title** | All three match; all verified | 20 | Corroborating; names are common, title changes, so use with caution |
| **Phone Number** | Business phone verified (e.g., from enrichment) | 15 | Often incomplete or outdated |
| **Domain + Full Name** | Email domain matches account domain + full name confirmed in 2+ sources | 20 | Corroborating; not sufficient alone |

### Decision Thresholds

| Total Score | Decision | Action |
|---|---|---|
| 50+ | **LINK** | Strong evidence (verified email + account, or email alone). Merge duplicates. |
| 30-49 | **REVIEW** | Multiple corroborating signals but no single strong key. Show to human; if historical activity or role stability favors one record, link; else hold. |
| <30 | **CREATE** | Insufficient evidence. Create new record. Log account relationship and why no match was found. |

### Contact Conflict Rule (Overrides Score)

Escalate to REVIEW if:
- Verified emails differ (e.g., john@acme.com vs john.smith@acme.com; these may be the same person, may not)
- Accounts linked differ and are not parent/subsidiary
- Title or role differs materially (VP Sales vs Customer)
- No account linked on existing record (ownerless contact is high-risk match candidate)

## Scoring Guidance

**"Verified" = third-party or system-generated evidence.** Not what the person wrote in a form (forms lie; people typo). Verified sources: corporate email, LinkedIn profile API, enrichment vendor, your own transactional system (e.g., closed-won deal associated with the account).

**Do NOT score on:**
- First name alone ("John" appears 10,000 times)
- Company size guesses
- "Similar-sounding" names (soundex matching is too loose for names)
- Blank fields treated as matches (no email vs blank email = no match)

**When in doubt, REVIEW.** False links (merging wrong records) are costlier than false creates (orphan records). Over-reviewing is inefficient but safer.
