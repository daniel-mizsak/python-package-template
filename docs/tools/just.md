# Just

[Just](https://just.systems/man/en){target} is a command runner.

It is used to define commands that can be invoked with a shorter alias.
This is useful for typing less and it also helps new developers get familiar with commands used by the project.

It is configured with the `Justfile`.

I mainly use `just` to have a reproducible setup configuration for both my local development and the CI/CD pipelines running in GitHub. One way to achieve this is by having a single command for setting up the environment (`just install`) and another command to run all checks on the code (`just check-all`).

I learned about `just` from [Hynek Schlawack's YouTube video](https://www.youtube.com/watch?v=TiBIjouDGuI&t=596s){target}.

<!-- prettier-ignore-start -->

!!! note
    Since the target commands in the `Justfile` are there for humans, I like being verbose and
    try using long command arguments (e.g., `--verbose` instead of `-v`). It makes it easier to
    understand what the command does exactly.
<!-- prettier-ignore-end -->
