#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:12:34 2019

@author: qindongliang
"""

import json

data = [{'c': 3.0, 'b': (2, 4), 'a': 'A'}]
print('DATA   :', repr(data))

unsorted = json.dumps(data)
print('JSON:', json.dumps(data))
print('SORT:', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('UNSORTED MATCH:', unsorted == first)
print('SOERTED MATCH :', first == second)