#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cipher(text):
    s = ""
    for wd in text:
        if wd.islower():
            s += chr(219-ord(wd))
        else:
            s += wd
    return s


if __name__ == "__main__":
    s = "I am an NLPer"
    print(s)
    s = cipher(s)
    print(s)
