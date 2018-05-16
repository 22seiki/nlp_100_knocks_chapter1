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


if __name__ == "__main__":
    s = "I am an NLPer"
    print(n_gram(2, s))
