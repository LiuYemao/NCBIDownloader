# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:03:44 2015

@author: ymliu
"""
import urllib2

def esearch(search_key,db="pubmed",usehistory=None,pdate=None):
    
    url="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=" + db + "&term=" + search_key
    
    if usehistory != None and pdate == None:
        url= url + "&usehistory=" + usehistory        
    elif usehistory == None and pdate != None:
        url= url + '+' + str(pdate) + "[pdat]"
    elif usehistory != None and pdate !=None:
        url= url + '+' + str(pdate) + "[pdat]" + "&usehistory=" + usehistory    

    print url
    return urllib2.urlopen(url).read()
