#!/usr/bin/env python
# -*- coding: utf-8 -*-


def n_gram(n, text):
    l = []
    for i in range(len(text)):
        if " " in text[i+n-1:i+n:]:
            l.append(text[i:i+n-1:])
        elif len(text) >= i+n:
            l.append(text[i:i+n:])
    return l


s1 = "paraparaparadise"
s2 = "paragraph"
X = set(n_gram(2, s1))
Y = set(n_gram(2, s2))
print("union:{0},\nintersection:{1},\ndifference:{2}"
      .format(X | Y, X-Y, X & Y))

if "se" in X and "se" in Y:
    print("X & Y:true")
elif "se" in X:
    print("X:true")
elif "se" in Y:
    print("Y:true")
else:
    print("false")
