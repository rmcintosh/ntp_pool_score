#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import ntp_pool_score


parser = argparse.ArgumentParser(prog="ntp_pool_score")
parser.add_argument("IPAddress", help="An IPv4 or IPv6 address")
arguments = parser.parse_args()


try:
    score = ntp_pool_score.get_server_ntp_pool_score(arguments.IPAddress)
except ntp_pool_score.ScoreNotFound as e:
    sys.exit(e)

print(score)
sys.exit()
