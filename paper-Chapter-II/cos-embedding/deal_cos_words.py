#coding = utf-8
import numpy as np
from numpy import linalg as la
from bert_serving.client import BertClient
import math
def deal_words_cos():
    model = BertClient()
    word_en = model.encode(['学生'])
    word_my = model.encode(['student'])
    dotmultiply = la.norm(word_en - word_my)
    word_en = math.sqrt(sum( map(lambda tmp_en: tmp_en * tmp_en, word_en.T) ))
    word_my = math.sqrt(sum( map(lambda tmp_my: tmp_my * tmp_my, word_my.T) ))
    #ret_cos = tmp_cos / (word_en * word_en)

    print ( la.norm(word_en - word_my) )

if __name__ == '__main__':
    deal_words_cos()