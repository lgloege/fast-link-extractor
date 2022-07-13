"""fast_link_extractor
a program to quickly extract links from a url
"""
from bs4 import BeautifulSoup
from itertools import chain
import asyncio
import aiohttp
import re


def _format_base_url(base_url: str):
    """properly format a url

    Args
    ------
    base_url (str): the original URL supplied

    Returns
    ------
    str:
    """
    base_url = 'https://' + \
        base_url if not base_url.startswith(
            ('http://', 'https://')) else base_url
    base_url = base_url + '/' if not base_url.endswith('/') else base_url
    return base_url


async def _async_get_html(base_url: str, ssl: bool = None):
    """get html for a url

    Parameters
    ------
    base_url (str): the original URL supplied

    Returns
    ------
    str: html for base_url
    """
    if ssl is None:
        ssl = False

    # may need to add this to ClientSession() connector=aiohttp.TCPConnector(ssl=False)
    conn = aiohttp.TCPConnector(ssl=ssl)
    async with aiohttp.ClientSession(connector=conn, trust_env=True) as client:
        async with client.get(base_url) as resp:  # ssl=False
            return await resp.text() if (resp.status == 200) else ""


def _get_links(html_page: str, base_url: str):
    """gets all links from html

    Parameters
    ------
    html_page (str): document html
    base_url (str): the original URL supplied

    Returns
    ------
    list: list of all the links in the html document
        these could be files or sub-directories
    """
    # "lxml" supposed to be faster than "html.parser
    soup = BeautifulSoup(html_page, "html.parser")
    regex = ".|(/$)"
    links = [f"{link.get('href')}"
             for link
             in soup.findAll('a', attrs={'href': re.compile(regex)})]

    return links


def _get_sub_dirs(links: list, base_url: str):
    """gets sub-directories from list of links

    Parameters
    ------
    links (list): list of links, contains files and sub-directories
    regex (str): filter links based on a regular expression

    Returns
    ------
    list: only the links that point to sub-directories are returned
    """
    sub_dirs = [f"{base_url}{link}" for link in links if re.search(r'/$', link)]
    return sub_dirs


def _get_files(links: list, regex: str = None):
    """gets files from list of links

    Parameters
    ------
    links (list): list of links, contains files and sub-directories
    regex (str): filter links based on a regular expression

    Returns
    ------
    list: only the links that point to files are returned
    """
    if regex is None:
        regex = r'[^/]$'
    file_links = [link for link in links if re.search(regex, link)]
    return file_links


def _filter_with_regex(files: list, regex: str):
    """filters files by regular expressions

    Parameters
    ------
        files (list): list of files
        regex (str): regular expression string

    Returns
    ------
        list: a list of files with regular expression applied
    """
    return [file for file in files if re.search(regex, file)]


def _prepend_with_baseurl(files: list, base_url: str):
    """prepend url to beginning of each file

    Parameters
    ------
        files (list): list of files
        base_url (str): base url

    Returns
    ------
        list: a list of files with base url pre-pended
    """
    return [base_url + file for file in files]


async def _gather_with_concurrency(n: int, *tasks):
    """Limits open files to avoid 'too many open files' error

    Parameters
    ------
        n (int): number of files to open at once

    Returns
    ------
        awaitable: gathered coroutines that need to awaited

    Notes
    ------
        https://stackoverflow.com/questions/48483348/how-to-limit-concurrency-with-python-asyncio/61478547#61478547
    """
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def _async_link_extractor(base_url: str, search_subs: bool = None, regex: str = None, *args, **kwargs):
    """ asyncronous extract links from url

    Parameters
    ------
        base_url (str): URL you want to search
        seach_subs (bool): True is want to search sub-directories
        regex (str): filter links based on a regular expression

    Returns
    ------
        list: list of files
    """
    files = []
    base_url = _format_base_url(base_url)
    html_page = await _async_get_html(base_url)
    links = _get_links(html_page=html_page, base_url=base_url)
    sub_dirs = _get_sub_dirs(links, base_url)
    filenames = _get_files(links, regex=regex)
    base_files = _prepend_with_baseurl(filenames, base_url)
    files.extend(base_files)

    # gathers files from sub-directories
    if search_subs:
        coros = [_async_link_extractor(sub) for sub in sub_dirs]
        # new_files = await asyncio.gather(*coros)
        new_files = await _gather_with_concurrency(200, *coros)
        files.extend(chain(*new_files))

    if regex is not None:
        files = _filter_with_regex(files, regex)
        # files = [file for file in files if re.search(regex, file)]

    return files


def link_extractor(base_url: str, search_subs: bool = None, regex: str = None, ipython: bool = None, *args, **kwargs):
    """extract links from base_url

    to get output in jupyter you need to await the result first
        ```
        links = await link_extractor(*args)
        ```

    Parameters
    ------
        base_url (str): URL you want to search
        seach_subs (bool): True is want to search sub-directories
        regex (str): filter links based on a regular expression

    Parameters
    ------
        list: list of files

    """
    if not ipython:
        return asyncio.run(_async_link_extractor(base_url=base_url,
                                                 search_subs=search_subs,
                                                 regex=regex))
    else:
        print(" ** this is a coroutine. await the result ** ")
        return _async_link_extractor(base_url=base_url,
                                     search_subs=search_subs,
                                     regex=regex)