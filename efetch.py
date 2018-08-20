# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:02:48 2015

@author: ymliu

efetch(query_key,web_value,db="pubmed",rettype=None,retmode=None)
"""

import urllib2

def efetch(query_key,web_value,db="pubmed",start=None,rettype=None,retmode=None):       
    
    if start != None:    
        url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=" + db + "&query_key=" + \
              query_key + "&WebEnv=" + web_value + "&retmax=10000&retstart=" + str(10000*(start-1))
    else:
        url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=" + db + "&query_key=" + query_key + \
              "&WebEnv=" + web_value
    
    if rettype != None and retmode == None:
        url = url + "&rettype=" + rettype
    elif rettype != None and retmode != None:
        url = url + "&rettype=" + rettype + "&retmode=" + retmode    
    elif rettype == None and retmode != None:
        url = url + "&retmode=" + retmode
    
    return urllib2.urlopen(url).read()
