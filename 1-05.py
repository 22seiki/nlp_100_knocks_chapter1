#!/usr/bin/env python
# -*- coding: utf-8 -*-


def n_gram(n, text):
    l = []
    for i in range(len(text)):
        if len(text[i:i+n]) > n-1:
            l.append(text[i:i+n])
    return l


if __name__ == "__main__":
    s = "I am an NLPer"
    print(n_gram(2, s))
    s = s.split()
    print(n_gram(2, s))
