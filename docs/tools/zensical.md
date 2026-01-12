# Zensical

[Zensical](https://zensical.org/docs/get-started/){target} is a static site generator for documentation.

It makes it possible to write the documentation in [Markdown](https://www.markdownguide.org/){target} and generate beautiful and responsive websites.

(One thing that sometimes makes `zensical` tricky for me to use, is that some features expect a certain way of formatting markdown files and the code formatter that I am using ([Prettier](https://prettier.io/){target}) reformats the content in a way that breaks those features. I use `<!-- prettier-ignore-start -->` and `<!-- prettier-ignore-end -->` to disable formatting locally.)

The `zensical` related settings are defined in the `zensical.toml` file.

Build the documentation locally by running:

```bash
zensical build --clean --strict
```

Or (preferably) use `just`:

```bash
just build-documentation
```

Serve the documentation locally by running:

```bash
zensical serve
```
