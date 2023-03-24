import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

ns = {}
with open(os.path.join(here, 'highcharts', 'version.py')) as f:
   exec(f.read(), {}, ns)

with open('README.md', encoding='utf-8') as readme_fh:
    _LONG_DESCRIPTION=readme_fh.read()

setup(
    name='python-highcharts-excentis',
    version=ns['__version__'],
    author='Kyper Developers',
    author_email='developers@kyperdata.com',
    maintainer='Excentis Software',
    maintainer_email='support@excentis.com',
    packages=find_packages(),
    package_data={
        'highcharts.highcharts': ['templates/*.html'],
        'highcharts.highmaps': ['templates/*.html'],
        'highcharts.highstock': ['templates/*.html']
    },
    url='https://github.com/excentis/python-highcharts',
    description='Python Highcharts wrapper',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[
        "Jinja2",
        "future"
    ],
    keywords = ['python', 'ipython', 'highcharts', 'chart', 'visualization', 'graph', 'javascript', 'html'],
    classifiers         = [
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
