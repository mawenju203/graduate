stanford-parser.jar 解压后用于 缅甸语的依存句法分析模型的训练使用 ；


模型训练命令（linux）：
nohup java edu.stanford.nlp.parser.nndep.DependencyParser -trainFile parser9_332/Mtrain.stanford.conll  -devFile parser9_332/Mdev.new.conll  -embedFile  parser9_332/mian.50d.txt -maxIter 10001 -embeddingSize 50 -model  marklog/model/mian_Mnew_5w.model.txt.gz >marklog/log/log_Mnew_13_5w.txt 2>&1 &

模型评估（win）：
start  /b java edu.stanford.nlp.parser.nndep.DependencyParser -model   marklog/model/mian_Mnewmap_5w.model.txt.gz -testFile  parser9_332/Mdev.new.conll  -outFile marklog/log_answer/mian_Mnewmap_5w.conllx  >marklog/log_answer/log_mian_Mnewmap_5w.txt 2>&1 &
