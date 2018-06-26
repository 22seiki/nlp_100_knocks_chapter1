#!/usr/bin/env python
# -*- coding: utf-8 -*-
s = 'Now I need a drink, alcoholic of course,\
    after the heavy lectures involving quantum mechanics.'
l = [len(n.strip(",.")) for n in s.split()]
print(l)
