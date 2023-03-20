

import pandas as pd
import glob



def parse_file():
    filelist = []
    for file in glob.glob('*.txt'):
        filelist.append(file)


    
    indices = [0,4,5,7,8,15,16,36,37] # list the indices to split on
    parsed_data = [] # returned array by line
    for file in filelist:
        with open(file, "r") as f:
            #header = next(f) #skip the header
            #data_mov = header[18:26] # and get data_mov from header
            for line in f: #loop through lines
                #split each line by the indices
                #parts = [data_mov] + [line.rstrip()[i:j] for i,j in zip(indices, indices[1:]+[None])]
                parts =[line[i:j] for i,j in zip(indices, indices[1:])]
                parsed_data.append(parts)

                new_parsed_data = [[s.strip() for s in sub_list  if s !=' '] for sub_list in parsed_data]

                df = pd.DataFrame(new_parsed_data)
                df.columns = ['ΕΤΟΣ', 'ΜΗΝΑΣ', 'ΚΩΔΙΚΟΣ','ΟΝΟΜΑ']
                with pd.ExcelWriter("output.xls") as writer:
                    df.to_excel(writer)
    print("***************")
    print(new_parsed_data)


    print(filelist)

parse_file()


