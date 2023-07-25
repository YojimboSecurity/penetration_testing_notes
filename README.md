<h1 align="center">
  <a href="https://github.com/YojimboSecurity/penetration-testing-notes">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.svg" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  penetration_testing_notes
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
  <br />
  <a href="https://github.com/YojimboSecurity/penetration-testing-notes/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/YojimboSecurity/penetration-testing-notes/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/YojimboSecurity/penetration-testing-notes/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/YojimboSecurity/penetration-testing-notes.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/YojimboSecurity/penetration-testing-notes/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by YojimboSecurity](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-YojimboSecurity-ff1414.svg?style=flat-square)](https://github.com/YojimboSecurity)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

Take better notes.
This is a framework for taking notes on an engagement or if you are just messing
around on HTB.

Original repo: <https://gitlab.com/yojimbo-security/penetration_testing_notes>

This is just a mirror.

<details>
<summary>Screenshots</summary>
<br>


|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

### Built With

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)

## Getting Started

### Prerequisites

- [install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

### Installation

- [install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

## Usage

- [use cookiecutter](https://cookiecutter.readthedocs.io/en/stable/usage.html)

Locally:

First create a zip

```
(SOURCE_DIR=$(basename $PWD) ZIP=cookiecutter.zip && # Set variables
pushd && # Set parent directory as working directory
zip -r $ZIP $SOURCE_DIR --exclude $SOURCE_DIR/$ZIP --quiet && # ZIP cookiecutter
mv $ZIP $SOURCE_DIR/$ZIP && # Move ZIP to original directory
popd && # Restore original work directory
echo  "Cookiecutter full path: $PWD/$ZIP")
```

```
cookiecutter "$PWD/$ZIP"
```

Repo:

```
cookiecutter gh:YojimboSecurity/penetration_testing_notes
```

You can add multipule IP addresses by selecting `network` from the `engagement_type`
and when presented with `network` add `{"base": "192.168.1", "sets": [1,2,3]}`.
Naturaly replace `192.168.1` with your IP base and replace `1,2,3` whith your
values.

For example, I have the following IPs I want to add to my notes.

192.168.64.1
192.168.64.22
192.168.64.23

I would add the following dictionary to the `network` option.

```
{"base": "192.168.64", "sets": [1,22,23]}
```

## Roadmap

See the [open issues](https://github.com/YojimboSecurity/penetration-testing-notes/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/YojimboSecurity/penetration-testing-notes/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/YojimboSecurity/penetration-testing-notes/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/YojimboSecurity/penetration-testing-notes/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/YojimboSecurity/penetration-testing-notes/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/YojimboSecurity)

## Project assistance

If you want to say **thank you** or/and support active development of penetration_testing_notes:

- Add a [GitHub Star](https://github.com/YojimboSecurity/penetration-testing-notes) to the project.
- Tweet about the penetration_testing_notes.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make penetration_testing_notes **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [YojimboSecurity](https://github.com/YojimboSecurity).

For a full list of all authors and contributors, see [the contributors page](https://github.com/YojimboSecurity/penetration-testing-notes/contributors).

## Security

penetration_testing_notes follows good practices of security, but 100% security cannot be assured.
penetration_testing_notes is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

I would like to acknowledge the amazing work by the cookiecutter team.
