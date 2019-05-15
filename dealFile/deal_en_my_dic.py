
def deal_en_my_emb(file_en, file_my, fwrite) :
    fr_en = open(file_en,'r',encoding='utf-8')
    fr_my = open(file_my,'r',encoding='utf-8')
    fw_emb = open(fwrite,'a+', encoding='utf-8')
    fr_en = fr_en.readlines()
    fr_my = fr_my.readlines()
    tmp = []
    for c_e in range(len(fr_en)) :
        tmp.append(fr_en[c_e].strip())
    for c_m in range(len(fr_my)) :
        tmp.append(fr_my[c_m].strip())
    fw_emb.write('\n'.join(tmp))
if __name__ == '__main__':
    file_en = 'enmap.emb'
    file_my = 'mianmap.emb'
    fwrite = 'en_my_emb'
    deal_en_my_emb(file_en, file_my, fwrite)
