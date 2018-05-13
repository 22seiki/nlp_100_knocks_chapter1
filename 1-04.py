#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = re.sub('[./,]', " ", s)
l = {}
id = 0
for n in s.split():
    id += 1
    if id % 2 == 1:
        l[id] = n[0:1:]
    else:
        l[id] = n[0:2:]
print(l)
