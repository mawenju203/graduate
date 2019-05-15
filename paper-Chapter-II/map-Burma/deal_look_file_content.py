#coding = utf-8

#查看文本内容，查看数据的格式信息；
def deal_look_file_content(file_content, fw_path):
    fr_file = open(file_content, 'r', encoding='utf-8')
    fw_path = open(fw_path, 'a+', encoding='utf-8')
    data_content = fr_file.readlines()
    print (len(data_content))
    c_i = 1
    for single_data in data_content :
        c_i += 1
        if c_i > 100000 :
            break
        '''
        if len(single_data.strip()) == 0:
            continue
        single_data = single_data.split('\t')[0]
        print (int(single_data))
        '''
        fw_path.write(single_data)
    fw_path.close()
    fr_file.close()

    '''
        single_data = single_data.strip().split('\t')
        if len(single_data) == 10:
            print ("== 10 ")
        #print ( single_data )
    '''

def deal_look_file_line(file_content, fw_path):
    fr_file = open(file_content, 'r', encoding='utf-8')
    fw_path = open(fw_path, 'a+', encoding='utf-8')
    data_content = fr_file.readlines()
    data_content = ' '.join( list (map(lambda tmp: tmp.strip(), data_content)) )
    unique_set = '\n'.join(set(data_content.split(' ')))
    fw_path.write(unique_set)
    fw_path.close()
    fr_file.close()


if __name__ == '__main__':
    file_path = 'D:/TestData/deal_my_embbeding/data_my.my-tok-line'
    fw_path = 'H:/coding-deep/glove.6B.100d.txt'
    train_file = 'D:/test/parser9_336/mian_en.100d.txt'
    deal_look_file_content(fw_path , train_file)

