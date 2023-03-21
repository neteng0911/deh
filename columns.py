import os

if os.path.exists("columnsout2.txt"):
  os.remove("columnsout2.txt")
else:
  print("The file does not exist")
if os.path.exists("columnsout3.txt"):
  os.remove("columnsout3.txt")
else:
  print("The file does not exist")

fin = open('columns.txt','rt',encoding="utf8" )
fout = open ('columnsout.txt', 'wt')
for line in fin:
    fout.write(line.replace('ΚΕΝΟ',''))
fout.close()



fout = open('columnsout.txt', 'r')
fout2 = open ('columnsout2.txt', 'w+')
for line in fout:
    fout2.write(line.replace('\t\t', ','))


fout2.close()
fout2 = open ('columnsout2.txt', 'r')
fout3 = open('columnsout3.txt', 'w+')
colstr=fout2.read().split(',')
print (colstr)
print(len(colstr))


fout3.write(str(colstr))




fin.close()
fout.close()
fout2.close()
fout3.close()