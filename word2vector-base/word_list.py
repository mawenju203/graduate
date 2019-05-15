#coding = utf-8
import io
import os
class Word_List(object):
    word_list_r = []
    '''
    def __init__(self, object):
        
        fr = io.open(object, 'r',encoding='utf-8')
        for words in fr.readlines():
            words = words.strip().split(' ')
            self.word_list_r.append(words)
        fr.close()
    '''

    def ReadFile(self,fileName):
        fr = io.open(fileName, 'r',encoding='utf-8')
        for words in fr.readlines():
            words = words.strip().split(' ')
            self.word_list_r.append(words)
        fr.close()

    def dealData_new(self, pathFile):
        if os.path.isfile(pathFile) :
            fr = io.open((os.path.join(pathFile, pathFile)), 'r', encoding='utf-8')
            for words in fr.readlines():
                if len(words.strip()) == 0 :
                    continue
                words = words.strip()
                self.word_list_r.append(words)
            fr.close()
        else :
            for fileName in os.listdir(pathFile):
                newPath = os.path.join(pathFile, fileName)
                self.dealData_new(newPath)


    def dealData(self, pathFile):
        if os.path.isdir(pathFile) :
            for fileName in os.listdir(pathFile):
                fr = io.open((os.path.join(pathFile, pathFile)), 'r', encoding='utf-8')
                for words in fr.readlines():
                    if len(words.strip()) == 0 :
                        continue
                    words = words.strip().split(' ')
                    self.word_list_r.append(words)
                fr.close()

if __name__ == '__main__' :
    dataList = Word_List()
    dataList.dealData_new('C:/Users/Administrator/Desktop/DeepLearning-Lab-master/data/')
    fw_new = io.open('C:/Users/Administrator/Desktop/DeepLearning-Lab-master/mian_data.conllx', 'a+', encoding='utf-8')
    dataList.word_list_r = list(set(dataList.word_list_r))
    fw_new.write('\n'.join(dataList.word_list_r))
    print (len(dataList.word_list_r))




