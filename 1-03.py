#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

s = 'Now I need a drink, alcoholic of course,\
    after the heavy lectures involving quantum mechanics.'
s = re.sub('[./,]', " ", s)
l = []
for n in s.split():
    l.append(len(n))
print(l)
