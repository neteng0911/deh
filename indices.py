fin = open('ind.txt','rt' )
fout = open ('indices.txt', 'wt')
for line in fin:
    fout.write(line.replace('\t',','))
fin.close()
fout.close()