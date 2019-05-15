# 处理英缅词之间的对应关系，分别生成对应的文本
def deal_one_line_rela(strRela) :
    strRela = strRela.split(' ')
    dic_en = dict()
    str_en = []
    dic_my = dict()
    str_my = []
    for c_i in range(len(strRela)) :
        tmp = strRela[c_i].split('-')
        startInt, endInt = int(tmp[0]) + 1 , int(tmp[1]) + 1
        if startInt in dic_en :
            dic_en[startInt].append(str(endInt))
        else :
            dic_en[startInt] = [str(endInt)]
        if endInt in dic_my:
            dic_my[endInt].append(str(startInt))
        else:
            dic_my[endInt] = [str(startInt)]
    tmp_en = list(dic_en.keys())
    tmp_en.sort()
    for c_l in range(len(tmp_en)) :
        singe_en = dic_en[tmp_en[c_l]]
        for c_r in singe_en :
            str_en.append(str(tmp_en[c_l]) + '\t' + c_r)

    tmp_my = list(dic_my.keys())
    tmp_my.sort()
    for c_m in range(len(tmp_my)) :
        singe_my = dic_my[tmp_my[c_m]]
        for c_t in singe_my :
            str_my.append(str(tmp_my[c_m]) + '\t' + c_t)
    return ' '.join(str_en) , ' '.join(str_my)



def deal_word_rela(fre_m,fe_m,fm_e) :
    fren_my = open(fre_m, 'r', encoding='utf-8')
    fren_my = fren_my.readlines()
    list_tar_my = []
    list_tar_en = []
    for c_line in range(len(fren_my)) :
        tmp = fren_my[c_line].split('\t')[1].strip()
        if len(tmp) == 0 :
            list_tar_my.append('')
            list_tar_en.append('')
        else :
            single_tar_en , single_tar_my = deal_one_line_rela(tmp)
            list_tar_en.append(single_tar_en)
            list_tar_my.append(single_tar_my)

    f_tar_my = open(fe_m,'a+',encoding='utf-8')
    f_tar_my.write('\n'.join(list_tar_my))
    f_tar_en = open(fm_e,'a+',encoding='utf-8')
    f_tar_en.write('\n'.join(list_tar_en))
    f_tar_my.close()
    f_tar_en.close()

if __name__ == '__main__':

    fre_m = 'D:/TestData/data_my.en-my'
    fe_m = 'D:/TestData/4-30/en_my.txt'
    fm_y = 'D:/TestData/4-30/my_en.txt'
    deal_word_rela(fre_m,fe_m,fm_y)