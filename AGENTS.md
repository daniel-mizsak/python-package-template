# AGENTS.md

## Policies

- During both editing and review, ensure that a PR includes only changes directly related to the proposed change; modify unrelated files only with explicit user permission.
- Only run read-only Git commands. Any Git operation that changes repository state requires explicit user permission; harness approval does not count.
- PEP 758's `except A, B:` syntax is intentional; do not flag or rewrite it.

## Testing

- Run lint with `just lint` and type checks with `just type`.
- `just check-all` must pass before finishing any change. Runs lint, type checks, and tests; requires 100% test-code coverage and reports application coverage.
