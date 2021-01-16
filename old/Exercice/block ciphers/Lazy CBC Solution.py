"""
input  =    f3a578cad2654d493ec266edcdd0d93d 2807ca7c410a82b7ee94096d7b83f56b 2807ca7c410a82b7ee94096d7b83f56b 2807ca7c410a82b7ee94096d7b83f56b
output =    00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000

Mentre il primo blocco in input e' xorato con la chave, lo lascio stare, MA SO ' \
'che il secondo, una volta passato per l'AES con una certa chiave avro in uscita tutti 0.
 Nota inoltre che il pattern 2807... si ripete sempre., quindi vuol dire che l'univo modo pe aver' \
 0000000 in uscita e' avere 2807...in ingresso, quindi quel mio f3a57..., dovra diventare un 2807... per avere in uscita 000
 quindi la chiave con cui viene xorato f3a57... per farlo diventare 2807 non e;' altor che f3a5...^2807

"""