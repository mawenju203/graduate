# 建立词的位置信息
#coding = utf-8


#查看文本内容，查看数据的格式信息；
def deal_look_file_content(file_path_content, file_content, fw_path):
    file_path_content = open(file_path_content, 'r', encoding='utf-8')
    fr_file = open(file_content, 'r', encoding='utf-8')
    fw_path = open(fw_path, 'a+', encoding='utf-8')
    data_map = fr_file.readlines()
    dataDic = {}
    for data in data_map:
        if (len(data) == 1) :
            continue
        data = data.strip().split('\t')
        dataDic[data[0]] = data[1]

    dataContent = file_path_content.readlines()
    strContentMap = []
    for dataCon in dataContent :
        dataCon = dataCon.strip()
        if (len(dataCon) == 1) :
            continue
        tmp = []
        for data_line in dataCon.split(' ') :
            if (len(data_line) == 0) :
                continue
            tmp.append(dataDic[data_line])
        strContentMap.append(' '.join(tmp))
    fw_path.write('\n'.join(strContentMap))
    fw_path.close()
    fr_file.close()
    file_path_content.close()



def deal_look_File(file_content, fw_path):
    fr_file = open(file_content, 'r', encoding='utf-8')
    fw_path = open(fw_path, 'a+', encoding='utf-8')
    data_content = fr_file.readlines()
    listContent = [x.strip() for x in data_content]
    setContent = set(' '.join(listContent).split())
    for data in setContent :
        fw_path.write(data + "\t" + str(hash(data)) + '\n')
    print ('over')




if __name__ == '__main__':
    file_path_content = 'D:/TestData/predata/data_my.my-tok-line'
    file_tag = 'D:/TestData/predata/data_my.my - tag'
    file_path = 'D:/TestData/predata/data_my.my-tok-position'
    fw_path = 'D:/TestData/predata/data_my.my-tok-position_file'
    deal_look_file_content(file_path_content , file_path , fw_path)