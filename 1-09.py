#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import re

s = "I couldn't believe that I could actually\
    understand what I was reading :\
    the phenomenal power of the human mind ."
s = re.sub('[./,/:]', "", s)
print(s)
text = ""
for wd in s.split():
    if len(wd) >= 4:
        l = [n for n in wd[1:len(wd)-1:]]
        s1 = wd[0]
        for i in range(1, len(wd)-1):
            c = random.choice(l)
            s1 += c
            l.remove(c)
        s1 += wd[len(wd)-1]
        text += s1 + " "
    else:
        text += wd + " "
print(text)
