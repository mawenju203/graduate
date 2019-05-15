import numpy as np
import embeddings
def deal_write_File(file_content, fw_path):
    fr_file = open(file_content, 'r', encoding='utf-8')
    fw_path = open(fw_path, 'a+', encoding='utf-8')
    fr_file = fr_file.readlines()
    for data in fr_file :
        data = data.strip()
        if len(data) == 0 :
            continue
        data = data.split(' ')
        data = [data[x] + '_' + str(x) for x in range(len(data))]
        fw_path.write(' '.join(data) + '\n')
    fw_path.close()
    print ("over")


def deal_matrix_words(srcfile, trgfile):

    srcfile = open(srcfile, encoding='utf-8', errors='surrogateescape')
    #trgfile = open(args.trg_input, encoding=args.encoding, errors='surrogateescape')
    src_words, src_matrix = embeddings.read(srcfile)
    dic_word_matrix = {}
    srcdata = srcfile.readlines()
    for line in range(len(src_words)) :
        srcSingle = src_words[line].split('_')[0]
        if srcSingle not in dic_word_matrix :
            dic_word_matrix[srcSingle] = [list(src_matrix[line])]
        else :
            dic_word_matrix[srcSingle].append(list(src_matrix[line]))
    words = []
    matrixs = []
    for itemKey , itemValue in dic_word_matrix.items() :
        itemValue = np.mean(np.array(itemValue) , 0)
        words.append(itemKey)
        matrixs.append(itemValue)
    trgfile = open(trgfile, mode='w', encoding='utf-8', errors='surrogateescape')
    embeddings.write(words, matrixs, trgfile)


def deal_my_with_position_File(file_content, fw_path, fEmPosition):
    srcfile = open(fw_path, encoding='utf-8', errors='surrogateescape')
    src_words, src_matrix = embeddings.read(srcfile)
    map_my_position = {}
    fr_file = open(file_content, 'r', encoding='utf-8')
    fr_file = fr_file.readlines()
    for singleWord in fr_file :
        singleWord = singleWord.strip().split('\t')
        map_my_position[singleWord[1]] = singleWord[0]
    for line in range(len(src_words)) :
        src_words[line] = map_my_position[src_words[line]]
    targetfile = open(fEmPosition, mode='w', encoding='utf-8', errors='surrogateescape')
    embeddings.write(src_words, src_matrix, targetfile)

if __name__ == '__main__' :
    file_tag = 'D:/TestData/predata/data_my.my-tok-position'
    file_Deal_tag = 'D:/TestData/20190312_second/miandian_Position_50_change.txt'
    file_new_tag = 'D:/TestData/20190312_second/miandian_my_Position_50_change.txt'
    #deal_write_File(file_tag , file_Deal_tag)
    #deal_matrix_words(file_tag, file_Deal_tag)
    deal_my_with_position_File(file_tag, file_Deal_tag, file_new_tag)