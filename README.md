# Fast Link Extractor
### Project under active deveopment, not production ready

A Python 3.6+ package to extract links from a webpage. Asyncronous functions allows the code to run fast when extracting from many sub-directories.

A use case for this tool is to extract download links for use with `wget` or `fsspec`.

### Functions Implemented
- `.link_extractor()`: top-level function to extract links from a URL.

# Installation


## PyPi
```sh
pip install fast-link-extractor==0.1.0
```

## GitHub
```sh
pip install -e git+https://github.com/lgloege/fast-link-extractor.git#egg=fast-link-extractor
```

# Usage

Simply import the package and call `link_extractor()`. This will output of list of extracted links
```python
import fast-link-extractor as fle

# url to extract links from
base_url = "https://lukegloege.com"

# extract all links that end with .nc
links = fle.link_extractor(base_url, 
                           search_subs=True,
                           prepend_base=True, 
                           regex='.nc$')
```

# ToDo
- **more tests**: need more tests
- **documentation**: need to setup documentation
