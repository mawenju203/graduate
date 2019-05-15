# -*- coding: UTF-8 -*-
from stanfordcorenlp import StanfordCoreNLP
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def create_dependence_file(raw_english_token , fwrite) :
    fraw = open(raw_english_token, mode="r")
    nlp = StanfordCoreNLP(r'D:\test\paper\stanford-corenlp-full-2018-02-27')
    fraw = fraw.readlines()
    try :
        tmp = []
        for line in range(len(fraw)):
            strtmp = fraw[line].strip().split('\t')
            if (len(strtmp) < 2) :
                print strtmp ,
                tmp.append('')
                continue
            linetmp = []
            DataDependence = nlp.dependency_parse(str(strtmp[1]))
            for lnum in DataDependence :
                liststr = list(lnum)
                liststr = [str(liststr[0]) , str(liststr[1]) , str(liststr[2])]
                linetmp.append(' '.join(liststr))
            tmp.append('\t'.join(linetmp))
        fwriteDependece = open(fwrite, mode="w")
        fwriteDependece.write('\n'.join(tmp))
    finally:
        print line ,
        nlp.close()

def create_token_file(raw_english_token , fwrite) :
    fraw = open(raw_english_token, mode="r")
    nlp = StanfordCoreNLP(r'D:\test\paper\stanford-corenlp-full-2018-02-27')
    fraw = fraw.readlines()
    try :
        tmp = []
        for line in range(len(fraw)):
            strtmp = fraw[line].strip().split('\t')
            if (len(strtmp) < 2) :
                print strtmp ,
                tmp.append('')
                continue
            linetmp = []
            DataDependence = nlp.pos_tag(str(strtmp[1]))
            for lnum in DataDependence :
                liststr = list(lnum)
                liststr = [str(liststr[0]) , str(liststr[1])]
                linetmp.append(' '.join(liststr))
            tmp.append('\t'.join(linetmp))
        fwriteDependece = open(fwrite, mode="w")
        fwriteDependece.write('\n'.join(tmp))
    finally:
        print line ,
        nlp.close()

if __name__ == '__main__':
    fread = 'G:/cwmt_dependence/raw_data/Book17_en.txt'
    fwrite_token = 'G:/cwmt_dependence/token_data/Book17_en_token.txt'
    fwrite_dependence = 'G:/cwmt_dependence/depen_data/Book17_en_depen.txt'
    create_token_file(fread, fwrite_token)
    #create_dependence_file(fread , fwrite_dependence)