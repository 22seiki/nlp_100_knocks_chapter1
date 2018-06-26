#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
l = {}
for i, n in enumerate(s.split()):
    if i+1 in only:
        l[n.strip(',.')[0:1]] = i+1
    else:
        l[n.strip(',.')[0:2]] = i+1
print(l)
