

import pandas as pd
import glob



def parse_file():



    indices = [0,4,5,7,8,15,16,36,37,57,58,62,63,83,84,95,96,108,109,121,122,147,148,173,174,181,182,202,203,213,214,224,225,
               233,234,239,240,260,261,267,268,277,278,291,292,300,301,309,310,313,314,321,322,329,330,335,336,345,346,359,360,
               373,374,387,388,401,402,415,416,429,430,443,444,457,458,471,472,485,486,499,500,513,514,527,528,541,542,555,556,
               569,570,583,584,597,598,611,612,625,626,639,640,653,654,667,668,681,682,695,696,709,710,723,724,737,738,751,752,
               765,766,779,780,793,794,807,808,821,822,835,836,849,850,863,864,877,878,891,892,905,906,919,920,933,934,947,948,
               961,962,975,976,989,990,1003,1004,1017,1018,1031,1032,1045,1046,1059,1060,1073,1074,1087,1088,1091,1092,1105,1106,
               1119,1120,1123,1124,1137,1138,1151,1152,1155,1156,1169,1170,1183,1184,1187,1188,1201,1202,1215,1216,1229,1230,1237,
               1238,1251,1252,1259,1260,1273,1274,1281,1282,1295,1296,1309,1310,1323,1324,1331,1332,1345,1346,1359,1360,1373,1374,1387,1388,1401,1402,1415,1416,1429,1430,1438]
    parsed_data = [] # returned array by line

    with open('vasikoold1.txt', "r") as f:
        #header = next(f) #skip the header
        #data_mov = header[18:26] # and get data_mov from header
        for line in f: #loop through lines
            #split each line by the indices
            #parts = [data_mov] + [line.rstrip()[i:j] for i,j in zip(indices, indices[1:]+[None])]
            parts =[line[i:j] for i,j in zip(indices, indices[1:])]
            parsed_data.append(parts)

            new_parsed_data = [[s.strip() for s in sub_list  if s !=' '] for sub_list in parsed_data]
            print(new_parsed_data)
            df = pd.DataFrame(new_parsed_data)
            df.columns = ['ΕΤΟΣ', 'ΜΗΝΑΣ', 'ΚΩΔΙΚΟΣ','ΟΝΟΜΑ']
            with pd.ExcelWriter('vasikoold1.xls') as writer:
                df.to_excel(writer)
    print("***************")
    print(new_parsed_data)


parse_file()


