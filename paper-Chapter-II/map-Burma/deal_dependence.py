#coding = utf-8

def string_translate_int (str_no):
    tmp = ''
    for single_int in str_no:
        if single_int.isdigit() == True:
            tmp += single_int
        else :
            break
    return tmp


def deal_sentence_parser(single_sentence, single_depence,sentence_no):
    single_sentence = single_sentence.split(' ')
    single_dependence = single_depence[1:-2].split(', ')
    single_sentence.insert(0,'root')
    len_dependence = len(single_dependence)
    for depen_no in range(1,len_dependence,2):
        dependence_no = single_dependence[depen_no].rfind('-')
        single_dependence[depen_no] = string_translate_int(single_dependence[depen_no][dependence_no + 1: -1])
        tmp_dependence = single_dependence[depen_no - 1][0:single_dependence[depen_no - 1].rfind('(')]
        dependence_note = single_dependence[depen_no - 1].rfind('-')
        single_dependence[depen_no - 1] = single_dependence[depen_no - 1][dependence_note + 1:] + '\t' + tmp_dependence
        try :
            single_sentence[int(single_dependence[depen_no])] += '\t' + single_dependence[depen_no - 1]
        except IndexError:
            print (sentence_no, '\t' ,int(single_dependence[depen_no]), '\t', len(single_sentence))
            continue
    for senten_no in range(len(single_sentence)):
        single_sentence[senten_no] = str(senten_no) + '\t' + single_sentence[senten_no]
    return single_sentence


def deal_dependence_parser(file_sentence, file_dependence, fi_w_depen):
    fr_sentence = open(file_sentence,'r',encoding='utf-8')
    fr_dependence = open(file_dependence,'r',encoding='utf-8')
    fw_dependence = open(fi_w_depen,'a+', encoding='utf-8')
    sentences = fr_sentence.readlines()
    dependences = fr_dependence.readlines()
    print (len(sentences),'\t',len(dependences))
    for sentence_lineno in range (len(sentences)):
        #print (sentence_lineno)
        tmp_lineno = deal_sentence_parser(sentences[sentence_lineno], dependences[sentence_lineno], sentence_lineno)
        tmp_lineno = ' '.join(tmp_lineno[1: ])
        fw_dependence.write(tmp_lineno)
    fw_dependence.close()
    fr_dependence.close()
    fr_sentence.close()



if __name__ == '__main__':
    fi_sentence = 'D:/TestData/english_new_tok.txt'
    fi_dependence = 'D:/TestData/test_parser.txt'
    fi_w_depen = 'D:/TestData/test_parser_syn-connect.txt'
    deal_dependence_parser(fi_sentence,fi_dependence,fi_w_depen)




