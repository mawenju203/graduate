def deal_en(rela_en_my , zh , en ,path_write):
    fr_file = open(rela_en_my, 'r', encoding='utf-8')
    fz_file = open(zh, 'r', encoding='utf-8')
    fe_file = open(en, 'r', encoding='utf-8')
    fw_file = open(path_write, 'a+', encoding='utf-8')
    fr_file = fr_file.readlines()
    fz_file = fz_file.readlines()
    fe_file = fe_file.readlines()
    list_en_zh = dict()
    for line in range(len(fz_file)) :
        list_en_zh[fe_file[line].strip()] = fz_file[line].strip()
    tmp = ''
    for lin in range(len(fr_file)):
        tmp = fr_file[lin].strip().split(' ')
        tmp[0] = list_en_zh[tmp[0]]
        fr_file[lin] = ' '.join(tmp)
    fw_file.write('\n'.join(fr_file))

def deal_en_my_rela(rela_en_my ,path_write):
    fr_file = open(rela_en_my, 'r', encoding='utf-8')
    fw_file = open(path_write, 'a+', encoding='utf-8')
    fr_file = fr_file.readlines()
    fr_file2 = []
    tmp = ''
    for line in range(len(fr_file)):
        tmp = fr_file[line].strip().split(' ')
        for c_l in range(1, len(tmp)) :
            fr_file2.append(' '.join([tmp[0] , tmp[c_l]]))
    fw_file.write('\n'.join(fr_file2))





if __name__ == '__main__':
    mfile_my_en_rela = 'D:/TestData/deal_data/rela.dic'
    mfile_en = 'D:/TestData/deal_data/en.txt'
    mfile_zh = 'D:/TestData/deal_data/zh.txt'
    fwr_file = 'D:/TestData/deal_data/rela_zh_mian_new.txt'
    deal_en_my_rela(mfile_my_en_rela , fwr_file)
    #deal_en(mfile_my_en_rela , mfile_zh , mfile_en , fwr_file)

