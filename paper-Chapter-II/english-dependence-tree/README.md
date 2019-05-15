dependence_20.py : 是为了对20万句英文的句子做依存句法分析

安装stanfordcorenlp包之前：
1：下载安装JDK 1.8及以上版本。
2：下载Stanford CoreNLP文件，解压。
3：处理中文还需要下载中文的模型jar文件，然后放到stanford-corenlp-full-＊＊-＊-＊根目录下即可（注意一定要下载这个文件哦，否则它默认是按英文来处理的）。
（https://stanfordnlp.github.io/CoreNLP/history.html）

pip install stanfordcorenlp


# coding=utf-8
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'/home/gld/stanford-corenlp-full-2016-10-31/', lang='zh')#默认是英文

sentence = '清华大学位于北京。'
print nlp.word_tokenize(sentence)
print nlp.pos_tag(sentence)
print nlp.ner(sentence)
print nlp.parse(sentence)
print nlp.dependency_parse(sentence)




dependence-deal.py : 将英文的pos和dependence 处理为英文的依存句法分析方法

deal_en_dependence(fread_depen , fread_pos , fw_answer) 处理的数据格式：
1 China NNP 2 nsubj	2 supports VBZ 0 ROOT	3 and CC 2 cc	4 actively RB 5 advmod	5 participates VBZ 2 conj	6 in IN 9 case	7 the DT 9 det	8 environmental JJ 9 amod	9 activities NNS 2 nmod	10 launched VBN 9 acl	11 by IN 14 case	12 the DT 14 det	13 UN NNP 14 compound	14 organizations NNS 10 nmod	15 . . 2 punct

get_answer(fw_answer , fw_answer_last) 处理后的数据格式：
1	China	China	NNP	NNP	_	2	nsubj	_	_
2	supports	supports	VBZ	VBZ	_	0	ROOT	_	_
3	and	and	CC	CC	_	2	cc	_	_
4	actively	actively	RB	RB	_	5	advmod	_	_
5	participates	participates	VBZ	VBZ	_	2	conj	_	_
6	in	in	IN	IN	_	9	case	_	_
7	the	the	DT	DT	_	9	det	_	_
8	environmental	environmental	JJ	JJ	_	9	amod	_	_
9	activities	activities	NNS	NNS	_	2	nmod	_	_
10	launched	launched	VBN	VBN	_	9	acl	_	_
11	by	by	IN	IN	_	14	case	_	_
12	the	the	DT	DT	_	14	det	_	_
13	UN	UN	NNP	NNP	_	14	compound	_	_
14	organizations	organizations	NNS	NNS	_	10	nmod	_	_
15	.	.	.	.	_	2	punct	_	_
