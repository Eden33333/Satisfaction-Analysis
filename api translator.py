# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:15:03 2024

@author: Administrator
"""

import pandas as pd
import numpy as np

import altair as alt

from deep_translator  import GoogleTranslator
import re

raw_data=pd.read_csv(r"C:\Users\Administrator\NLP\Satisfied Analysis.csv")
# =============================================================================
# raw_data.isna().sum()
# =============================================================================

#Translate comments into English
for i,records in enumerate(raw_data.iloc[:,1]):
    raw_data.iloc[i,1]=GoogleTranslator(source='auto', target='en').translate(records) 
#Translate comments
map_dic={"正":"Postive","负":"Negative","中":"Neutral"}
raw_data["sentiment"]=raw_data["sentiment"].map(map_dic)

#write new data set
raw_data.to_csv("C:/Users/Administrator/NLP/train_data.csv")