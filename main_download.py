# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 20:13:32 2015

@author: ymliu

从pubmed下载需要的文件，并保存下来
"""

import os,time
import efetch,getEfetchKey
from save_data import savePickle

def download(terms_dic,term_keys,year = False,getAbstract=False):
    """    
    Write online abstracts into xml file!
    If given the parameter year:
        1) False: download the abstract by the term list;
        2) True: download the abstract year by year from 2004 to 2014.
    """    
    
    uis = {}    
    tmp = [terms_dic[term].replace(" ","+") for term in terms_keys if " " in terms_dic[term]]    
    
    if year == True:
        term_value = "[ALL]+OR+".join(tmp)+"[ALL]+AND+human[ALL]+AND+drug[ALL]"
        for i,pdate in enumerate(range(2004,2015)):
            key_value = getEfetchKey.getEfetchKey(term_value,str(pdate))
            if len(key_value) == 2:                
                #write uis into pkl
                uilist = efetch.efetch(key_value[0],key_value[1],rettype="uilist")
                uis[pdate] = [int(ui) for ui in uilist.split('\n')[:-1]]
                print "Number of term %d : %d" % (pdate,len(uis[pdate]))
                
                #download abstract
                if getAbstract == True:
                    times = (len(uis[pdate])/10000) + 1
                    for j in range(times):
                        abstract_xml = efetch.efetch(key_value[0],key_value[1],start=j+1,retmode="xml")
                        write_file = 'pdate' + str(pdate) +'_' + str(j+1) + '.xml'
                        with open(write_file,'a') as write_in:
                            write_in.write(abstract_xml)
                        print "Work done for downloading the abstracts of the year:",pdate,"part",j+1
                        time.sleep(1)
            else:
                print "There is something wrong when downloading the avstracts of the year:",pdate
            time.sleep(1)
        savePickle(uis,"uids_year.pkl")

    else:
        for i,t in enumerate(tmp):
            #term_value = t + "[ALL]+AND+human[ALL]+AND+drug[ALL]"
            term_value = t + "[ALL]"
            key_value = getEfetchKey.getEfetchKey(term_value)
            if len(key_value) == 2:                
                #write uis into pkl                
                uilist = efetch.efetch(key_value[0],key_value[1],rettype="uilist")
                uis[term_keys[i]] = [int(ui) for ui in uilist.split('\n')[:-1]]
                print "Number of term %s : %d" % (terms_dic[term_keys[i]],len(uis[term_keys[i]]))                
                
                #download abstract                
                if getAbstract == True:
                    times= len(uis[term_keys[i]])/10000 + 1
                    for j in range(times):                
                        try:                        
                            abstract_xml = efetch.efetch(key_value[0],key_value[1],start=j+1,retmode="xml")
                            write_file = term_keys[i] + '_' + str(j+1) + '.xml'
                            with open(write_file,'a') as write_in:
                                write_in.write(abstract_xml)
                            print "Work done for downloading the abstracts of the term:",t.replace("+"," "),\
                                'of part',j+1
                        except:
                            log_file = term_keys[i] + '.log'
                            with open(log_file,'a') as write_in:
                                write_in.write(key_value[0] + "\t" + key_value[1] + "\t" + str(j+1) + "\n")
                            pass
                        time.sleep(1)
                
            else:
                print "There is something wrong when downloading the abstracts of the term:",t.replace("+"," ")
            time.sleep(1)
        savePickle(uis,"uids_term.pkl")


if __name__ == "__main__":

    #设置工作路径
    os.chdir('/public8/ymliu/schizophrenia/20160104')
    
    terms_dic = {"SzD":"Schizophrenic Disorders"}
    terms_keys = ["SzD"]
    
    download(terms_dic,terms_keys,getAbstract=True)
    