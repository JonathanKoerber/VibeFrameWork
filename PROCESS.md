# The Vibe Framework: Test-Driven Development for AI-Assisted Coding

**Core Principle**: Small steps, tests first, no scope creep.

## 1. Setup
```bash
git checkout main && git pull
git checkout -b vibe/<type>-<description>
```
Never commit to main directly.

## 2. Define ONE Small Behavior
Before any code, answer:
- **What**: One specific behavior in one sentence
- **Where**: Exact file/function (with line ranges)
- **Don't Touch**: What files/functions to avoid
- **Test**: How you'll verify it works

**Size Limit**: Must be <50 lines of code. If bigger, split it.

Example:
```
What: Add email format validation to validate_user()
Where: app.py lines 45-68, tests/test_app.py
Don't Touch: Other functions in app.py, imports
Test: test_validate_user_rejects_invalid_email
```

## 3. TDD Cycle (Red → Green → Refactor)

### Step 1: Write Failing Test (RED)
```bash
# Write test first
pytest tests/ -v  # Should FAIL
git commit -m "vibe: add test for [behavior]"
```

**AI Rule**: MUST refuse to write production code before this step.

### Step 2: Make Test Pass (GREEN)
```bash
# Write minimal code to pass test
pytest tests/ -v  # Should PASS
git commit -m "vibe: implement [behavior]"
```

**Constraints**:

### Step 3: Verify & Refactor (CLEAN)
```bash
git diff --stat  # Verify <50 lines, <3 files
pytest tests/ -v  # Still passing
```

Optional: Clean up code without changing behavior.

### Step 4: Next Iteration
Repeat Steps 1-3 for next small behavior, or merge via PR.

## 4. AI Assistant Rules

**BEFORE writing production code, AI MUST ask:**
1. "Does a failing test exist for this?"
2. "What files/functions should I modify?"
3. "What should I NOT touch?"

**AI MUST REFUSE if**:

**AI Response Template** (when refusing):
```
I need a failing test first (Vibe Step 1).

Please specify:
- Exact behavior to test (one sentence)
- Which file/function to modify
- What NOT to change

Then I'll write the test, run it (should fail), and write code to pass it.
```

## 5. Pull Request Checklist

Before merging:
- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Diff is clean (`git diff --stat` shows expected files only)
- [ ] Commits follow format: `vibe: <summary>`
- [ ] PR describes what changed and why

PR Template:
```
## What
[One sentence description]

## Changes
- [Behavior 1] (commits: abc123, def456)
- [Behavior 2] (commits: ghi789)

## Tests
`pytest tests/ -v` - all passing

## Diff
[Number] files, [Number] lines changed
```

## 6. Quick Reference

| Phase | Command | Expected Result |
|-------|---------|-----------------|
| **Red** | `pytest tests/ -v` | New test FAILS |
| **Green** | `pytest tests/ -v` | All tests PASS |
| **Clean** | `git diff --stat` | <50 lines, <3 files |

**Commit Format**: `vibe: <present tense summary>`

**Branch Format**: `vibe/<feature|fix|refactor>-<short-description>`

---

## Why This Works

- **Small steps** = Easy to review, easy to revert
- **Tests first** = Prevents scope creep, documents intent
- **AI constraints** = Keeps generative code focused and predictable
- **Git discipline** = Every change is traceable and reversible