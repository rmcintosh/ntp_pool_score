#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

import bs4
import requests

NTP_POOL_SCORE_URL = "http://www.ntppool.org/scores/"
"""str: ntppool.org URL for retrieving server NTP pool score"""


class ScoreNotFound(Exception):
    pass


def get_server_ntp_pool_score(server_ip: str) -> float:
    """Retrieves a server's NTP pool score by scraping ntppool.org

    Arg(s):
        server_ip: An IPv4 or IPv6 address.

    Returns:
        The NTP pool score for the specified IP address.
    """
    url = f"{NTP_POOL_SCORE_URL}{server_ip}"
    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")

    for p in soup.find_all("p"):
        if match := re.search("Current score:(.+?) ", p.getText().strip()):
            return float(match.group(1).strip())

    raise ScoreNotFound(f"Couldn't find score for {server_ip}")
