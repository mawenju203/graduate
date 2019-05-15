#coding=utf-8
import io
from gensim.models import Word2Vec
from word_list import Word_List
import embeddings
import numpy as np
def train_word_model():
    list_word = Word_List()
    list_word.ReadFile('D:/TestData/20190312_second/data_my.my-tok-position_file2')
    print (len(list_word.word_list_r))
    model = Word2Vec(list_word.word_list_r, size=50, alpha=0.005, window=5, min_count=1, workers=4)
    model.save("word2vec_en_position_50.model")

def useModel():
    model = Word2Vec.load('word2vec_my_en.model')
    print ( model.wv.similarity('star', 'freedoms') )
    print ( model.most_similar(['friend']))


def share_embedding(words,matrix):
    f = open('D:/TestData/predata/miandian_Position_50.txt', mode='w', encoding='utf-8', errors='surrogateescape')
    embeddings.write(words, matrix, f)


def deal_file_read(file_path):
    fr_ans = io.open(file_path, 'r', encoding='utf-8')
    fw_ans = io.open('D:/TestData/predata/rela_words_cos', 'a+', encoding='utf-8')
    for word_split in fr_ans.readlines():
        word_split = word_split.split('\t')[:-1]
        fw_ans.write(' '.join(word_split) + '\n')
    fr_ans.close()
    fw_ans.close()

def get_word_embed():
    fr_ans = io.open('D:/TestData/predata/data_my.my-tok-position_file2', 'r', encoding='utf-8')
    #fw_ans = io.open('D:/TestData/predata/miandian_embed.txt', 'a+', encoding='utf-8')
    model = Word2Vec.load("word2vec_en_position_50.model")
    #ic_words = dict()
    words = []
    matrix = []
    for word_ans in fr_ans.readlines():
        word_ans = word_ans.strip()
        try:
            tmp = model[word_ans]
        except KeyError:
            #fw_ans.write(word_ans + '\t' + ' '.join(str(np.zeros(50)).split(' ')) + '\n')
            print (word_ans)
            continue
        #dic_words[word_ans] = list(model[word_ans]) 
        #np.savez('data.npz', str=str, arr=arr, dict=dict)
        words.append(word_ans)
        matrix.append(tmp)
        #fw_ans.write(word_ans + '\t' + ' '.join(str(tmp).split(' ')) + '\n')
    share_embedding(words,matrix)
    fr_ans.close()
    #fw_ans.close()


def get_SecretWord_embed():
    fr_ans = io.open('D:/TestData/predata/data_my.my-tok-position_file2', 'r', encoding='utf-8')
    model = Word2Vec.load("word2vec_en_position_50.model")
    words = []
    matrix = []
    fr_ans = ' '.join([x.strip() for x in fr_ans])
    fr_ans = set(fr_ans.split(' '))
    for word_ans in fr_ans :
        try:
            tmp = model[word_ans]
        except KeyError:
            print (word_ans)
            continue
        words.append(word_ans)
        matrix.append(tmp)
    share_embedding(words, matrix)



if __name__ == '__main__':
    #deal_file_read('D:/TestData/predata/rela_words_cos.txt_3')
    #useModel()
    #train_word_model()
    get_SecretWord_embed()

