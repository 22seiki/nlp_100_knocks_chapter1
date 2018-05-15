#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def templete(x, y, z):
    print("{0}時の{1}は{2}".format(x, y, z))


x = 12
y = "気温"
z = 22.4

templete(x, y, z)
