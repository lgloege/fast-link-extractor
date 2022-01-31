import fast_link_extractor as fle
# import pytest


def test_extractor():
    url = 'https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/'
    _ = fle.link_extractor(url, search_subs=True, prepend_base=True, regex='.nc$')
    return None
