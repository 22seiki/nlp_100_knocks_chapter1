#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = u"パトカー"
s2 = u"タクシー"
s = ""
for i in range(len(s1)):
    s += (s1[i:i+1:]+s2[i:i+1:])
print(s)
