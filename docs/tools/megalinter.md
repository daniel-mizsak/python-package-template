# Megalinter

[Megalinter](https://megalinter.io/latest/){target} is a many-in-one linter solution.
It supports a lot of file types like `markdown`, `yaml`, `json`, or `Dockerfile`.

The `megalinter` related settings are defined in the `.github/linters/megalinter.yml` file. (This is a custom path.) I also put the configurations of the linters running within `megalinter` into `.github/linters/`. (Such as `.yamllint.yml`). The important thing is to either name the file to what `megalinter` expects or to specify the path in the `megalinter.yml` configuration file.

Call `megalinter` by running:

```bash
npx mega-linter-runner --flavor cupcake -e "MEGALINTER_CONFIG=.github/linters/.megalinter.yml"
```

Or (preferably) use `just`:

```bash
just megalinter
```

Since running `megalinter` requires `nodejs` and `docker`, plus it is a bit slow, for some projects I only run it in `GitHub Action` or not at all.
