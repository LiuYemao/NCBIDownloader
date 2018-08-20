# -*- coding: utf-8 -*-

import os,pickle

def saveData(year,pmid,title,abstracts,keywords):
    op = os.path.abspath(str(year))
    if os.path.exists(op) != True:os.mkdir(op)
    filename = op + '/PMID_' + pmid + '.txt'
    write_in = open(filename,'w')
    print "Writing %s into %s" % (pmid,filename)
    write_in.write(title + '\n'
                    + ' '.join(abstracts) + '\n'
                    + ';'.join(keywords))
    write_in.flush(); write_in.close()
    
def savePickle(data,saveTo):    
    #import pickle    
    output = open(saveTo,'wb')
    pickle.dump(data, output)
    output.close()
