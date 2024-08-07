<p align="center">
  <a href="https://fast-link-extractor.readthedocs.io/en/latest/"><img src="./docs/img/logo.png" alt="fast-link-extractor"></a>
</p>

<p align="center">
    <em>Python package to quickly extract links in HTML</em>
</p>

<p align="center">
<a href="https://fast-link-extractor.readthedocs.io/en/latest/?badge=latest" target="_blank">
    <img src="https://readthedocs.org/projects/fast-link-extractor/badge/?version=latest" alt="documentation">
</a>
<a href="https://opensource.org/licenses/MIT" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="license">
</a>
<a href="https://github.com/python/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="code style">
</a>
<a href="https://github.com/lgloege/fast-link-extractor/issues" target="_blank">
    <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="contributions">
</a>
</p>

---

**Documentation**: <a href="https://fast-link-extractor.readthedocs.io" target="_blank">https://fast-link-extractor.readthedocs.io</a>

**Source Code**: <a href="https://github.com/lgloege/fast-link-extractor" target="_blank">https://github.com/lgloege/fast-link-extractor</a>

---

A Python 3.7+ package to extract links from a webpage. Asyncronous functions allows the code to run fast when extracting from many sub-directories. A use case for this tool is to extract download links for use with `wget` or `fsspec`.


# Installation

Install using PyPi
```
pip install fast-link-extractor
```

Insatll using GitHub
```
pip install git+https://github.com/lgloege/fast-link-extractor.git
```

## Example
Simply import the package and call `link_extractor()`. This will output of list of extracted links
```python
import fast_link_extractor as fle

# url to extract links from
base_url = "https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/"

# extract all links from sub directories ending with .nc
# this may take ~10 seconds, there are a lot of sub-directories
links = fle.link_extractor(base_url,
                           search_subs=True,
                           regex='.nc$')
```

If using inside Jupyter or IPython, set `ipython=True`
```python
import fast_link_extractor as fle

# url to extract links from
base_url = "https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/"

# extract all links from sub directories ending with .nc
# this may take ~10 seconds, there are a lot of sub-directories
links = fle.link_extractor(base_url,
                           search_subs=True,
                           ipython=True,
                           regex='.nc$')
```

## License

This project is licensed under the terms of the MIT license.
