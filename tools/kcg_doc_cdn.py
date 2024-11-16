#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Purpose:

This script automatically replaces image links in KeepChatGPT documentation (README.md)

"""

import os, re

def save(data, outfile):
    if not os.path.exists('test'):
        os.mkdir('test')
    open(outfile, 'wb').write(data.encode())

def main():
    rm = open('README.md', 'rb').read().decode()
    kcg_code = open('KeepChatGPT.user.js', 'rb').read().decode()

    cdn_pre = 'https://hub.gitmirror.com/https://raw.githubusercontent.com/xcanwin/KeepChatGPT/main'
    version = re.findall(r'// @version\s+(\S*?)\s', kcg_code)[0]
    # version = '24.6'

    rm_new = re.sub(r'src="(/assets/.*?)"', r'src="{}\1?v={}"'.format(cdn_pre, version), rm)
    print(rm_new)
    save(rm_new, 'test/README_CDN.md')

main()
