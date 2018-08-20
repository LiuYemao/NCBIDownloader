# -*- coding: utf-8 -*-
"""
Created on Tue Sep 01 15:31:37 2015

@author: ymliu
"""

import re,esearch

def getEfetchKey(term,pdate=None):
    key = []      
    if pdate != None: 
        esearch_xml = esearch.esearch(term,usehistory="y",pdate=pdate)
    else:
        esearch_xml = esearch.esearch(term,usehistory="y")
    count_re = re.compile(r'<Count>(.*)</Count>')
    count = int(count_re.findall(esearch_xml)[0])
    if count > 0:        
        QueryKey_re = re.compile(r'<QueryKey>(.*)</QueryKey>')
        key.append(str(QueryKey_re.findall(esearch_xml)[0]))
        WebEnv_re = re.compile(r'<WebEnv>(.*)</WebEnv>')
        key.append(WebEnv_re.findall(esearch_xml)[0])
    else:
        key.append("0")
    return key
