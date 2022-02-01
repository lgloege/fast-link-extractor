import fast_link_extractor
# import pytest


def test_extractor():
    url = 'https://www.ncei.noaa.gov/data/sea-surface-temperature-optimum-interpolation/v2.1/access/avhrr/'
    links = fast_link_extractor.link_extractor(url, search_subs=True, regex='.nc$')
    _ = fast_link_extractor.prepend_with_baseurl(links, url)
    return None
