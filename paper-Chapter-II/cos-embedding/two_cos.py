#coding = utf-8
import math
import embeddings
import numpy as np
from numpy import linalg as la
from bert_serving.client import BertClient

def share_embedding(words,matrix):
    f = open('word.txt', mode='w', encoding='utf-8', errors='surrogateescape')
    embeddings.write(words, matrix, f)
def get_word_embed():
    fr_ans = open('miandian_w.txt', 'r', encoding='utf-8')
    model = BertClient()
    words = []
    matrix = []
    for word_ans in fr_ans.readlines():
        word_ans = word_ans.strip()
        if len(word_ans) != 0:
            words.append(word_ans)
    matrix = model.encode(words)
    share_embedding(words,matrix)
    fr_ans.close()

def deal_cost_cos():
    fr_ans = open('rela_words.txt', 'r', encoding='utf-8')
    fw_ans = open('rela_words_cos.txt_3', 'a+', encoding='utf-8')
    model = BertClient()
    for words_single in fr_ans.readlines():
        tmp_en, tmp_my = words_single.strip().split('\t')
        tmp_en_em = model.encode([tmp_en])
        tmp_my_em = model.encode([tmp_my])
        tmp_cos = la.norm(tmp_en_em - tmp_my_em)
        tmp_en_sqrt = math.sqrt(sum(list(map(lambda tmp_x : tmp_x * tmp_x , tmp_en_em.T))))
        tmp_my_sqrt = math.sqrt(sum(list(map(lambda tmp_y : tmp_y * tmp_y , tmp_my_em.T))))
        ret_cos = tmp_cos / (tmp_en_sqrt * tmp_my_sqrt)
        ret_cos = 1 - ret_cos
        fw_ans.write(tmp_en + '\t' + tmp_my + '\t' + str(ret_cos) + '\n')
    fw_ans.close()


if __name__ == '__main__':
    deal_cost_cos()
