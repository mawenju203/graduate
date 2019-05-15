#coding = utf-8
import random
def back_dict(list_rela):
    dic_rela = dict()
    for single_meta in list_rela:
        rela_one, rela_two = single_meta.split('\t')
        if rela_one in dic_rela :
            dic_rela[rela_one].append(rela_two)
        else :
            dic_rela[rela_one] = [rela_two]
    return dic_rela

def back_dict_multi(list_depen):
    dic_depen = dict()
    for single_meta in list_depen:
        dic_depen[single_meta[0]] = single_meta
    return dic_depen


def back_single_dependence_tree(single_my_list, single_my_en_list, single_en_my_list, single_depen_list):
    #print (len(single_my_en_list))
    try :
        dic_my_en = back_dict(single_my_en_list)
        dic_en_my = back_dict(single_en_my_list)
    except ValueError:
        return ''
    single_depen_list = list( map(lambda tmp: tmp.split('\t'), single_depen_list) )
    dic_dependence = back_dict_multi(single_depen_list)
    len_my_list = len(single_my_list)
    ink_note = ''
    c_i = 0
    for c_i in range( len_my_list - 1):
        c_i_add_1 = c_i + 1
        try :
            my_turn_en = dic_my_en[str(c_i_add_1)][0] #找到缅语对应的英文
        except KeyError:
            continue
        try :
            en_depen = [dic_dependence[my_turn_en][2],dic_dependence[my_turn_en][3]] #英语对应的英语，以及依存关系
        except IndexError :
            continue
        except KeyError:
            continue
        if en_depen[0] == '0':
            ink_note = str(c_i_add_1)
            single_my_list[c_i] = str(c_i_add_1) + '\t' + single_my_list[c_i] + '\t0' + '\troot'
            continue
        try :
            en_my_rela_tmp = dic_en_my[en_depen[0]]
        except KeyError:
            continue
        single_my_list[c_i] = str(c_i_add_1) + '\t' + single_my_list[c_i] + '\t' + en_my_rela_tmp[0] + '\t' + en_depen[1]
    if len(ink_note) == 0 :
        single_my_list[len_my_list - 1] = str(len_my_list) + '\t' + single_my_list[len_my_list - 1] + '\t' + str(
            random.randint(1, c_i)) + '\tpunct'
    else :
        single_my_list[len_my_list - 1] = str(len_my_list) + '\t' + single_my_list[len_my_list - 1] + '\t' + str(ink_note) + '\tpunct'
    return single_my_list


def deal_last_process(file_my, file_my_en_rela, file_en_my_rela,  file_depen, fw_file):
    fr_my = open(file_my,'r',encoding='utf-8')
    fr_my_en_rela = open(file_my_en_rela,'r',encoding='utf-8')
    fr_en_my_rela = open(file_en_my_rela, 'r', encoding='utf-8')
    fr_depen = open(file_depen,'r', encoding='utf-8')
    fw_file = open(fw_file, 'a+', encoding='utf-8')
    lines_my = fr_my.readlines()
    lines_my_en_rela = fr_my_en_rela.readlines()
    lines_en_my_rela = fr_en_my_rela.readlines()
    lines_depen = fr_depen.readlines()
    for c_i in range( len(lines_depen) ):
        single_my = lines_my[c_i].strip()
        single_my_en_rela = lines_my_en_rela[c_i].strip()
        single_en_my_rela = lines_en_my_rela[c_i].strip()
        single_depen = lines_depen[c_i].strip()
        if len(lines_my) == 0 or len(lines_my_en_rela) < 2 or len(lines_depen) == 0:
            continue
        else :
            single_my = single_my.split(' ')
            single_my_en_rela = single_my_en_rela.split(' ')
            single_en_my_rela = single_en_my_rela.split(' ')
            single_depen = single_depen.split(' ')
            # back_single_dependence_tree： 返回的是list类型的数据
            try :
                fw_file.write( ' '.join( back_single_dependence_tree(single_my, single_my_en_rela, single_en_my_rela, single_depen) ) + '\n')
            except ValueError:
                continue
    fw_file.close()
    fr_my.close()
    fr_my_en_rela.close()
    fr_en_my_rela.close()
    fr_depen.close()



def deal_dependence_tree(fr_file, fw_file):
    fr_depen_tree = open(fr_file,'r', encoding='utf-8')
    fw_depen_tree = open(fw_file, 'a+', encoding='utf-8')
    fr_lines_tree = fr_depen_tree.readlines()
    for single_tree in fr_lines_tree :
        single_tree = single_tree.strip()
        list_problem = []
        note_ink = -1
        if len(single_tree) < 2 :
            continue
        else :
            single_tree = single_tree.split(' ')
            for line_no in range( len(single_tree) ):
                if len( single_tree[line_no].split('\t') ) == 2:
                    single_tree[line_no] = str(line_no + 1) + '\t' + single_tree[line_no]
                    list_problem.append(line_no)
                else :
                    if single_tree[line_no].split('\t')[3] == '0':
                        note_ink = line_no + 1
            for c_i in range (len(list_problem)):
                if note_ink == -1:
                    single_tree[list_problem[c_i]] = single_tree[list_problem[c_i]] + '\t0\troot'
                    note_ink = list_problem[c_i]
                else :
                    single_tree[list_problem[c_i]] = single_tree[list_problem[c_i]] + '\t' + str(note_ink) + '\tRandom'
        fw_depen_tree.write(' '.join(single_tree) + '\n')
    fw_depen_tree.close()
    fr_depen_tree.close()




def deal_dependence_tree_two(fr_file, fw_file):
    fr_depen_tree = open(fr_file,'r', encoding='utf-8')
    fw_depen_tree = open(fw_file, 'a+', encoding='utf-8')
    fr_lines_tree = fr_depen_tree.readlines()
    for single_tree in fr_lines_tree :
        single_tree = single_tree.strip().split(' ')
        for tmp_no in range( len(single_tree) ) :
            single_tree[tmp_no] = single_tree[tmp_no].split('\t')
            single_tree[tmp_no] = [single_tree[tmp_no][0], single_tree[tmp_no][1], '_',
                                   single_tree[tmp_no][2], single_tree[tmp_no][2], '_', single_tree[tmp_no][3],
                                   single_tree[tmp_no][4], single_tree[tmp_no][3], single_tree[tmp_no][4]]
            #single_tree[tmp_no] = [single_tree[tmp_no][0], single_tree[tmp_no][1], single_tree[tmp_no][1], single_tree[tmp_no][2], single_tree[tmp_no][2], '_',single_tree[tmp_no][3], single_tree[tmp_no][4], '_', '_' ]
            single_tree[tmp_no] = '\t'.join(single_tree[tmp_no])
        single_tree = '\n'.join( single_tree )
        fw_depen_tree.write(single_tree + '\n\n')

    fw_depen_tree.close()
    fr_depen_tree.close()





if __name__ == '__main__':
    mfile_my = 'D:/TestData/deal_data/miandian_deal-line.txt'
    mfile_my_en_rela = 'D:/TestData/deal_data/deal_my-en-line'
    mfile_en_my_rela = 'D:/TestData/deal_data/deal_en-my-line'
    mfile_depen = 'D:/TestData/deal_data/test_parser_syn-line.txt'
    mfr_file = 'D:/TestData/deal_data/answer-line.conll'
    mfw_file = 'D:/TestData/deal_data/answer-line-test-6.conll'
    deal_last_process(mfile_my, mfile_my_en_rela, mfile_en_my_rela, mfile_depen, mfw_file)
    deal_dependence_tree_two(mfr_file, mfw_file)