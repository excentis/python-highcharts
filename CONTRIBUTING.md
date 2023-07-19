# Contributing Guide

Quick reference how to deploy a new update

## Build

1. Update version in `highcharts_excentis/version.py`
1. Build the project

       python -m build

## Release

1. Build beta version (`<major>.<minor>.<patch>b<beta>`) of the project
1. Upload to TestPyPI

       python -m twine upload -r testpypi dist/highcharts_excentis-0.4.3b20230327-py3-none-any.whl dist/highcharts-excentis-0.4.3b20230327.tar.gz

1. Test installation

       pip install -U --extra-index-url https://test.pypi.org/simple/ 'highcharts-excentis==0.4.3b20230327'

1. Build release version (`<major>.<minor>.<patch>`) of the project
1. Upload to PyPI

       python -m twine upload -r pypi dist/highcharts_excentis-0.4.3-py3-none-any.whl dist/highcharts-excentis-0.4.3.tar.gz

1. Test installation

       pip install -U highcharts-excentis

1. Add the git tag

       git tag v0.4.3
       git push --tags
