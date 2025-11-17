# GitHub Pages

[GitHub Pages](https://docs.github.com/en/pages/){target} is a static site hosting service.

Once the documentation is built (for example with `zensical` from the previous section), the generated static files can be deployed to GitHub Pages.

Make sure that for the repository `Settings > Pages > Source` is set to `GitHub Actions`.

My publishing workflow is the following (see it in action in `.github/workflows/cd.yml`):

- Every time a tag is pushed to the `main` branch, I run the `.github/workflows/ci.yml` workflow.
- This workflow generates the documentation (using my [reusable python-ci GitHub Workflow](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/python-ci.yml){target}) and uploads the generated static files as an artifact.
- Once this job ran successfully, the `github-pages-publish` job downloads the artifact and deploys it using the `actions/deploy-pages` action.
