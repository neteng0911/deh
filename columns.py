fin = open('columns.txt','rt',encoding="utf8" )
fout = open ('columnsout.txt', 'wt')
for line in fin:
    fout.write(line.replace('ΚΕΝΟ',''))
fout.close()



fout = open('columnsout.txt', 'r')
fout2 = open ('columnsout2.txt', 'wt')
for line in fout:
    fout2.write(line.replace('\t\t', ',""'))
fin.close()
fout.close()
fout2.close()