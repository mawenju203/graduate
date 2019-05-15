# -*- coding: UTF-8 -*-

#建立对应的english 和 my 词对应的位置关系
def deal_rela(line_rela):
    dic_rela = dict()
    list_rela = line_rela.split(' ')
    for single_meta in list_rela:
        rela_one, rela_two = single_meta.split('\t')
        if rela_one in dic_rela :
            dic_rela[rela_one].append(rela_two)
        else :
            dic_rela[rela_one] = [rela_two]
    return dic_rela

#建立对应的english 和 my 词对应的关系
def deal_rela_words(line_rela, en_tok, my_tok):
    en_tok = en_tok.split(' ')
    my_tok = my_tok.split(' ')
    # 建立对应的单词对词典:dic_rela_words
    dic_rela_words = dict()
    line_rela = line_rela.split(' ')
    for single_meta in line_rela:
        rela_one, rela_two = single_meta.split('\t')
        tmp_en = ''
        tmp_my = ''
        try :
            tmp_en = en_tok[int(rela_one)]
            tmp_my = my_tok[int(rela_two)]
        except IndexError:
            continue
        if tmp_en in dic_rela_words:
            dic_rela_words[tmp_en].append(tmp_my)
        else :
            dic_rela_words[tmp_en] = [tmp_my]
    return dic_rela_words


def deal_words_en_my(fr1, fr2, fr3, fw):
    fr1 = open(fr1, 'r', encoding='utf-8')
    fr2 = open(fr2, 'r', encoding='utf-8')
    fr3 = open(fr3, 'r', encoding='utf-8')
    fw = open(fw, 'a+', encoding='utf-8')
    fr1_lines = fr1.readlines()
    fr2_lines = fr2.readlines()
    fr3_lines = fr3.readlines()
    for c_i  in range(len(fr2_lines)):
        tmp_en_tok = fr1_lines[c_i].strip()
        tmp_my_tok = fr2_lines[c_i].strip()
        tmp_rela = fr3_lines[c_i].strip()
        if len(tmp_en_tok) == 0 or len(tmp_my_tok) == 0 or len(tmp_rela) == 0:
            continue
        else :
            tmp_en_tok = 'root ' + tmp_en_tok
            tmp_my_tok = 'root ' + tmp_my_tok
            dic_rela_words = deal_rela_words(tmp_rela, tmp_en_tok, tmp_my_tok)
            for single_dic in dic_rela_words:
                fw.write(single_dic + '\t' + ' '.join(dic_rela_words[single_dic]) + '\n')
    fw.close()
    fr1.close()
    fr2.close()
    fr3.close()



if __name__ == '__main__':
    file_en_sentence_tok = 'D:/TestData/deal_cos/english_new_tok.txt'
    file_my_sentence_tok = 'D:/TestData/deal_cos/data_my.my-tok-line'
    file_en_my_rela = 'D:/TestData/deal_cos/deal_en-my-line'
    file_relat_words = 'D:/TestData/deal_cos/ans.txt'
    deal_words_en_my(file_en_sentence_tok, file_my_sentence_tok, file_en_my_rela, file_relat_words)
