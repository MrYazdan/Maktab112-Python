#! /usr/bin/env python

import os

print(f"Your ip: {os.popen('curl -s https://icanhazip.com').read()}")
