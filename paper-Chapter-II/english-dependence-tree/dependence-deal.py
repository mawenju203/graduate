#获得每一行的依存句法分析过程数据
def deal_line_sentence(line_depen , line_en , lineno):
    line_depen = line_depen.split('\t')
    line_en = line_en.split(' ')
    minlen = min(len(line_depen) , len(line_en))
    tmpdep = []
    dicdep = dict()
    intnum = 0
    for line in range(minlen):
        strdep = line_depen[line].split(' ')
        intnum = int(strdep[2])
        dicdep[intnum] = [strdep[2] , line_en[intnum - 1] , strdep[1] , strdep[0]]
    listdic = list(dicdep.keys())
    listdic.sort()
    for li in listdic :
        tmpdep.append('\t'.join(dicdep[li]))

    return ' '.join(tmpdep)

def deal_process(fread_token ,fread_depen , fwrite):
    fr_en_tok = open(fread_token, 'r', encoding='utf-8')
    fr_en_depen = open(fread_depen,'r', encoding='utf-8')
    fw_file = open(fwrite, 'a+', encoding='utf-8')
    fr_en_tok = fr_en_tok.readlines()
    fr_en_depen = fr_en_depen.readlines()
    tmpWrite = []
    for line in range(len(fr_en_tok)) :
        fr_en_depen[line] = fr_en_depen[line].strip()
        fr_en_tok[line] = fr_en_tok[line].strip().split('\t')[1]
        tmpWrite.append(deal_line_sentence(fr_en_depen[line] , fr_en_tok[line] , line))
    fw_file.write('\n'.join(tmpWrite))
    fw_file.close()


def dependence_en_process(list_en_depen , list_en_pos) :
    list_en_depen = list_en_depen.split('\t')
    list_en_pos = list_en_pos.split('\t')
    ret_answer = []
    for nline in range(len(list_en_depen)) :
        ret_answer.append('')

    for nli in range(len(list_en_depen)):
        tmpdepen = list_en_depen[nli].split(' ')
        tmpInt = int(tmpdepen[2]) - 1
        ret_answer[tmpInt] = ' '.join([tmpdepen[2] ,list_en_pos[tmpInt] , tmpdepen[1] , tmpdepen[0]])
    return '\t'.join(ret_answer)

def deal_en_dependence(fread_depen , fread_pos , fwrite) :

    fr_en_depen = open(fread_depen,'r', encoding='utf-8')
    fr_en_pos = open(fread_pos, 'r', encoding='utf-8')
    fw_answer = open(fwrite, 'w', encoding='utf-8')
    fr_en_depen = fr_en_depen.readlines()
    fr_en_pos = fr_en_pos.readlines()
    tmpAnswer = []
    for line in range(len(fr_en_depen)):
        fr_en_depen[line] = fr_en_depen[line].strip()
        fr_en_pos[line] = fr_en_pos[line].strip()
        tmpAnswer.append(dependence_en_process(fr_en_depen[line] , fr_en_pos[line]))
    fw_answer.write('\n'.join(tmpAnswer))
    fw_answer.close()

def read_file(fwrite) :
    fread_file = open(fwrite,'r', encoding='utf-8')
    fread_file = fread_file.readlines()

    for cnum in range(len(fread_file)) :
        fread_file[cnum] = fread_file[cnum].strip().split('\t')

        for cl in fread_file[cnum] :
            cl = cl.split(' ')
            try:
                if len(cl[0]) == 0 or len(cl[1]) == 0 or len(cl[2]) == 0 or len(cl[3]) == 0 or len(cl[4]) == 0:
                    print(cnum)
            except ValueError :
                print(cnum)

    print('over')


def get_answer(fread_data , fwrite) :
    fread_file = open(fread_data,'r', encoding='utf-8')
    fread_file = fread_file.readlines()
    fw_answer = open(fwrite, 'w', encoding='utf-8')
    write_answer = []
    for cnum in range(len(fread_file)) :
        fread_file[cnum] = fread_file[cnum].strip().split('\t')
        line_dep = []
        for cnext in fread_file[cnum] :
            cnext = cnext.split(' ')
            try :
                if int(cnext[3]) > -1 :
                    pass
            except :
                print (str(cnum) + str(cnext))
                continue
            cnext = '\t'.join([cnext[0] , cnext[1] , '_' , cnext[2] , cnext[2] , '_' , cnext[3] , cnext[4] ,  cnext[3] , cnext[4] ])
            line_dep.append(cnext)
        write_answer.append('\n'.join(line_dep))
    fw_answer.write('\n\n'.join(write_answer))
    print('over')

def uni_data(fread_data3 , fread_data4 ,fread_data2 , fread_data , fwrite) :
    fw_answer = open(fwrite, 'a+', encoding='utf-8')

    fread_file = open(fread_data2, 'r', encoding='utf-8')
    fread_file = fread_file.readlines()
    fw_answer.write(''.join(fread_file))
    fread_file = open(fread_data, 'r', encoding='utf-8')
    fread_file = fread_file.readlines()
    fw_answer.write(''.join(fread_file))
    fread_file = open(fread_data3, 'r', encoding='utf-8')
    fread_file = fread_file.readlines()
    fw_answer.write(''.join(fread_file))
    fread_file = open(fread_data4, 'r', encoding='utf-8')
    fread_file = fread_file.readlines()
    fw_answer.write(''.join(fread_file))

    fw_answer.close()


if __name__ == '__main__':
    fread_token = 'D:/TestData/data_my.en-tok'
    fread_depen = 'D:/TestData/4-30/data_my.en_depen.txt'
    fread_pos = 'D:/TestData/4-30/data_my.en_pos.txt'
    fw_answer = 'D:/TestData/4-30/data_pro.txt'
    fw_answer_last = 'D:/TestData/4-30/data_pro_last.txt'
    fread_data = 'G:/cwmt_dependence/dependence_answer/Book17_depen_answer_last.txt'
    fread_data2 = 'G:/cwmt_dependence/dependence_answer/Book18_depen_answer_last.txt'
    fread_data3 = 'G:/cwmt_dependence/dependence_answer/Book19_depen_answer_last.txt'
    fread_data4 = 'G:/cwmt_dependence/dependence_answer/Book20_depen_answer_last.txt'
    fwrite = 'G:/cwmt_dependence/dependence_answer/Bookunit_depen_last.txt'
    #deal_en_dependence(fread_depen , fread_pos , fw_answer)
    #uni_data(fread_data3 , fread_data4 ,fread_data2 , fread_data , fwrite)
    #read_file(fread_data)
    get_answer(fw_answer , fw_answer_last)
    #deal_process(fread_token ,fread_depen , fwrite)