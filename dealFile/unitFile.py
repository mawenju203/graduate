def unitFileEmb(fd1 , fd2 , fw) :
    fmian = open(fd1, 'r', encoding='utf-8')
    fen = open(fd2, 'r', encoding='utf-8')
    funit = open(fw, 'a+', encoding='utf-8')
    fmianD = fmian.readlines()
    fenD = fen.readlines()
    funit.write(''.join(fmianD[1:]) + '\n')
    funit.write(''.join(fenD[1:]) + '\n')
    fmian.close()
    fen.close()
    funit.close()



if __name__ == '__main__':
    fmian = '../mianmap.emb.bak'
    fen = '../enmap.emb'
    funit = '../unit_en_mian.conll'
    unitFileEmb(fmian , fen , funit)