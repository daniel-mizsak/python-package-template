## <div align="center"> 🐍 python-package-template</div>

<div align="center">
<a href="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
<a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/python-package-template/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/python-package-template/main.svg" alt="pre-commit.ci status"></a>
<a href='https://python-package-template-pypi.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/python-package-template-pypi/badge/?version=latest' alt='docs status' /></a>
<a href="ttps://img.shields.io/github/license/daniel-mizsak/python-package-template" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/python-package-template" alt="license"></a>
</div>


## Overview
A GitHub template with my python package configurations.

## GitHub repository settings
Code/About:
- Releases

General/Features:
- Issues
- Preserve this repository

General/Pull Requests:
- Allow merge commits
- Allow squash merging
- Allow rebase merging
- Automatically delete head branches

Branches/Branch protection rules:\
`main`
- Protect matching branches
  - Require pull request reviews before merging
  - Dismiss stale pull request approvals when new commits are pushed
  - Require status checks to pass before merging
    - `pre-commit.ci - pr`
    - `tox / tox`

Environments:\
`pypi`
- Deployment protection rules:
- Required reviewers:
    `daniel-mizsak`
- Allow administrators to bypass configured protection rules

## Setup PyPi trusted publishing

[PyPi publishing settings](https://pypi.org/manage/account/publishing/)

Add a new pending publisher:
- PyPi Project Name: `python-package-template-pypi` (has to match the project name in `pyproject.toml`)
- Owner: `daniel-mizsak`
- Repository name: `https://github.com/daniel-mizsak/python-package-template`
- Workflow name: `release.yml`
