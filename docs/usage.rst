Quickstart Guide
================

Installation
------------

.. code-block:: bash

   # PyPi
   pip install fast-link-extactor

   # for bleeding-edge up-to-date commit
   pip install -e git+https://github.com/lgloege/fast-link-extactor.git


Example
-------

# Example
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