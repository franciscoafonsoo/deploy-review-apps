# Heroku Review App in Bitbucket


<p align="center">
<a href="https://pypi.org/project/black/"><img alt="PyPI" src="https://img.shields.io/pypi/v/black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/psf/black"><img alt="Checker: flake8" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/psf/black/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
</p>

_pyra_ is a deploy tool for Heroku Review App using Bitbucket Pipelines.

---

Heroku Review App is a great tool to make ephemeral apps in Heroku. The problem is
that this tool only plays nice with Github. Outside of it, the integration with a CI system
is frustrating and hard and still in a very early stage of development.

This tool is an effort to automate the creation of Review Apps using Bitbucket Pipelines. It
should be easy to fork this project and adapted it to another CI system (or abstract the CI at all).

---

## *THIS IS A WORK IN PROGRESS*

This does the work, but don't expect many flexibility at this point. You are welcome to contribuite
by opening a issue or a Pull Request. Any code should 
