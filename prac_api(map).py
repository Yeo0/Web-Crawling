#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:19:31 2018

@author: yeoyoung
"""

import pandas as pd
import os
import sys
import urllib.request

client_id = "6omFMHOiwwWB57x69RFg"
client_secret = "ifUp5rwMNn"

df = pd.read_csv("address_data.csv")
address = df["소재지"]
address = address.fillna(0)