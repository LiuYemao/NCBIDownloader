# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:24:47 2015

@author: ymliu
"""

#epost

import urllib2

def epost(id_list,db="pubmed"):
    url="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/epost.fcgi?db=" + db + "&id=" + ",".join(id_list)
    #print url
    return urllib2.urlopen(url).read()