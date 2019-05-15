#coding = utf-8

def turn_int_add1(list_str):
    return list(map(lambda tmp: tmp + 1,map(int,list_str)))

def turn_list_line(list_int):
    return '\t'.join(map(str, list_int))

def swap_two(str_data):
    str_data = str_data.split('\t')
    str_data = [str_data[1], str_data[0]]
    return list(map(int, str_data))


def turn_my_en(list_data):

    list_data = list(map(lambda tmp:swap_two(tmp), list_data))
    list_data = sorted(list_data)
    return ' '.join( list( map(lambda x_tmp: turn_list_line(x_tmp), list_data) ) )




def deal_en_my(file_en_my,path_write):
    fr_file = open(file_en_my, 'r', encoding='utf-8')
    fw_file = open(path_write, 'a+', encoding='utf-8')
    connect_en_my = fr_file.readlines()
    c_i = 1
    for single_en_my in connect_en_my:
        single_en_my_0, single_en_my_1 = single_en_my.split('\t')
        single_en_my_1 = single_en_my_1.strip()
        if len(single_en_my_1) > 0 :
            single_en_my_1 = list(map(lambda tmp: tmp.split('-'),single_en_my_1.split(' ')))
            single_en_my_1 = list(map(lambda tmp:turn_int_add1(tmp), single_en_my_1))
            single_en_my_1 = list(map(lambda tmp:turn_list_line(tmp), single_en_my_1))
            single_en_my_1 = ' '.join(single_en_my_1)
            fw_file.write(single_en_my_1 + '\n')
        else :
            fw_file.write('\n')
        c_i += 1
        #single_en_my = single_en_my_0 + '\n' + single_en_my_1
        #fw_file.write(single_en_my_0 + '\n' + single_en_my_1 + '\n\n')
        #fw_file.write(single_en_my + '\n')
    fr_file.close()
    fw_file.close()


def deal_en_my_two(file_en_my,path_write):
    fr_file = open(file_en_my, 'r', encoding='utf-8')
    fw_file = open(path_write, 'a+', encoding='utf-8')
    connect_en_my = fr_file.readlines()
    #c_i = 1
    for single_en_my in connect_en_my:
        single_en_my_0, single_en_my_1 = single_en_my.split('\t')
        single_en_my_1 = single_en_my_1.strip()
        if len(single_en_my_1) > 0 :
            single_en_my_1 = list(map(lambda tmp: tmp.split('-'),single_en_my_1.split(' ')))
            single_en_my_1 = list(map(lambda tmp:turn_int_add1(tmp), single_en_my_1))
            single_en_my_1 = list(map(lambda tmp:turn_list_line(tmp), single_en_my_1))
            single_en_my_1 = turn_my_en(single_en_my_1)
            fw_file.write(single_en_my_1 + '\n')
        else :
            fw_file.write('\n')
        #c_i += 1
        #single_en_my = single_en_my_0 + '\n' + single_en_my_1
        #fw_file.write(single_en_my_0 + '\n' + single_en_my_1 + '\n\n')
        #fw_file.write(single_en_my + '\n')
    fr_file.close()
    fw_file.close()


if __name__ == '__main__':
    path_en_my = 'D:/TestData/data_my.en-my'
    path_write_back = 'D:/TestData/deal_en-my-line'
    deal_en_my(path_en_my,path_write_back)