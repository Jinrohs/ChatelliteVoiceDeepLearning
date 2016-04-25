#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]

with open(filename) as fp:
    for line in iter(fp.readline, ""):
        line = line.rstrip()
        sent = []

        for w in line.split(" "):
            if w == "<bos>":
                continue

            if "<eos>" in w:
                w = w.replace("<eos>", "")
                w = w.replace("<bos>", "")
                sent.append(w)
                print "".join(sent)
                break
            sent.append(w)

