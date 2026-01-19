GitHub Workflow: The Vibe Iterate Method

This guide defines the repeatable process for adding features or fixes using the Vibe Coding Framework. The goal: every AI-assisted change is scoped, test-backed, reviewable, and reversible.

1) Prerequisites (before you start)
- On main: git status clean, then git pull.
- Name branches as vibe/<type>-<summary> (examples: vibe/feature-auth-rate-limit, vibe/fix-null-logging).
- Never commit directly to main.

2) Define the Vibe (what you will build)
Capture this before coding so prompts stay focused and traceable.

Template:
Goal: <what changes for users or systems>
Scope: <what is included / explicitly out of scope>
Acceptance: <bullet list of observable outcomes>
Risks/Edge cases: <empty input, long strings, timing, error paths>
Affected areas: <modules, endpoints, UI flows>

Use-case snippet (required, keeps AI prompts precise):
- Title
- Primary actor(s)
- Preconditions
- Trigger
- Main success path (short steps)
- Alternate/edge paths
- Postconditions/output

When using AI assistance, include the use-case snippet in your prompt. If any part is missing or unclear, the assistant should ask for those details before coding. Keep it 5–8 lines.

Definition of Ready (DoR) — required before starting a vibe
- Use-case snippet complete (title, actors, preconditions, trigger, main/alternate paths, postconditions).
- Goal, scope, acceptance criteria, and risks/edge cases captured.
- Affected areas listed (modules, endpoints, UI flows).
- Test plan noted (what layers: unit/integration/contract/regression).
- If missing, do not start coding; update the prompt/issue first.

3) The Vibe Iterate Cycle (per chunk)
1. Sync & Branch: start from updated main; git checkout -b vibe/<name>.
2. Define the vibe: fill the template above in your IDE/PR description.
3. Tests: write/extend tests first for new behavior; run the suite before accepting code.
4. Validate (self-audit): lint/style, inputs validated, errors handled, logs appropriate, edge cases covered.
5. Commit: small, atomic commits using git commit -m "vibe: <brief change>".

4) Test expectations
- Prefer test-first when adding behavior; always add coverage for fixes.
- Name tests by scenario and outcome (e.g., validates_invalid_email_returns_400).
- Tests must cover the edge cases listed in the vibe/use-case (empty/null, long strings, alternates), not just the happy path.
- Include regression tests when fixing bugs.
- Group tests by use case: keep tests for one use case together (e.g., tests/usecase_<name>.py or a describe/fixture named after the use case). Reference the use-case title/ID in test names or descriptions.
- Code changes should stay within the use case’s declared scope. If you must touch out-of-scope code, add tests for that area first, then change it.

Definition of Done (DoD) — required before merge
- Tests added/updated and passing locally and in CI (lint + test suite).
- Docs updated where relevant (API docs, README, changelog).
- PR reviewed/approved; branch aligned with main; branch deleted post-merge.
- Rollback/feature-flag plan documented if change is risky.
- For services: health endpoint intact, logging at appropriate level, and any new env vars documented.

5) Quality checklist before commit
- Tests pass locally (and new tests added when behavior changes).
- Lint/style run (if configured).
- Input validation and error handling present; avoid silent failures.
- Edge cases checked: empty/null, long strings, concurrency/timing (if relevant).
- No unrelated refactors bundled with features unless documented.

6) Commit rules
- Format: vibe: <summary> (present tense, concise).
- Keep commits small and purposeful; split behavior changes from large refactors when possible.

7) Integration via Pull Request
- Push: git push origin vibe/<name>.
- PR must describe goal, scope, approach, tests run (with commands), and edge cases considered.
- Require green CI (tests + lint) before merge. If CI is absent, manually rerun the full test command and note results.
- Merge only via PR; delete the branch after merge to avoid drift.

Suggested PR outline (can be a template):
Goal: …
Approach: …
Tests: <commands and outcomes>
Edge cases: …
Notes/Risks: …

8) Traceability and rollback
- Link vibes to issues/tickets when available.
- If feasible, add a feature flag or describe a rollback plan (revert commit/PR) for risky changes.

9) Recommended project structure
- /tests for automated checks.
- VIBE_GUIDE.md (this file).
- .github/PULL_REQUEST_TEMPLATE.md to enforce the PR outline above.

Lifecycle alignment (lightweight SDLC mapping)
- Stages: Idea/Backlog → Ready (DoR met) → In Progress (branch created) → In Review (PR open) → Done (merged) → Released (deployed/tagged).
- Traceability: Link vibes/PRs to issue IDs; reference the issue/use-case in branch names, commits, and test names when relevant.
- Risk/impact note: Briefly capture impact (data, security, perf, UX) and rollback plan in the PR for higher-risk changes.
- Release hygiene: Tag releases (e.g., vX.Y.Z), update CHANGELOG, note deployment steps and container image tag/env vars if shipping via Docker.

Why this works
Isolated branches keep changes contained, tests guard behavior, and the PR ritual documents intent and validation so AI-generated code remains reviewable and reversible.