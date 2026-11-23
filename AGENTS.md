# AGENTS.md

## Writing style

- Do not use semicolons. Write separate sentences.
  Within a list, place related guidance on an indented continuation line under the same bullet.

## Dependencies

- Dependencies are managed with uv.
  The `exclude-newer` setting in `pyproject.toml` is intentional.

## Testing

- Name tests `test_<operation>__<scenario_or_behavior>`, using existing terminology.
  Keep one scenario per test, but multiple actions are appropriate when testing a sequence.
- When a test module covers multiple functions, group tests in the same order as their definitions in the source module.
  Within each group, follow the function's control flow, including validation and early exits before later operations.
  Preserve the existing order when the relative flow order is unclear.
- Parametrize only cases sharing setup and assertions, without conditional logic or varying patch targets.
  Split cases when sharing assertions requires indirect logic.
- Separate Arrange, Act, Assert with blank lines, without routine section comments.
  Store results before asserting, except with `pytest.raises`.
- Keep assertions focused on the named scenario. Add supporting checks only when needed to prove its outcome or state transition.

## Validation

- Before finishing, pass `just check-all` except for documentation-only changes.
  This runs lint, type checks, and tests on all supported Python versions, with 100% coverage required for test code.
  Application coverage is reported without a minimum threshold.
