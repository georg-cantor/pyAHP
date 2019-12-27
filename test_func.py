#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:57:56 2019
test the functions of pyAHP
@author: qindongliang
"""
import json
from pyahp import parse

with open('./examples/car.json') as json_model:
    # model can also be a python dictionary
    model = json.load(json_model)

ahp_model = parse(model)
priorities = ahp_model.get_priorities()
print(priorities)