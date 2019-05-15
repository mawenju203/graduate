#coding = utf-8
from nltk.tree import Tree

def  deal_phrase_tree(phrase_file, deal_conclusion):
    phrase_deal = open(phrase_file, 'r', encoding='utf-8')
    deal_conclu = open(deal_conclusion, 'a+', encoding='utf-8')
    phrase_lines = phrase_deal.readlines()
    for phrase_single in phrase_lines:
        phrase_single = phrase_single.split('\t')[1].strip()
        if len( phrase_single ) == 0:
            continue
        else :
            conclu = Tree.fromstring(phrase_single)
            tmp_conclu = str (conclu.productions())
            print ( tmp_conclu )
            deal_conclu.write(tmp_conclu + '\n')
    deal_conclu.close()
    phrase_deal.close()




if __name__ == '__main__':
    phrase_file = 'D:/TestData/data_my.my-syn'
    conclusion_file = 'D:/TestData/deal_cos/data_my.my-syn-line'
    deal_phrase_tree(phrase_file, conclusion_file)