
# -*- coding: utf-8 -*-
import pandas as pd
import glob
import os
import pyxlsb
import uu


print(os.getcwd())
def parse_file():


    with open("indices.txt") as f:
        indices=f.read()
        for line in f:
            indices.append(line)# list the indices to split on
    #ind2=[0,4,5,7,8,15,16,36,37]
    # ind2 = [0,4,5,7,8,15,16,36,37,57,58,62,63,83,84,95,96,108,109,121,122,147,148,173,174,181,182,202,203,213,214,224,225,
    #            233,234,239,240,260,261,267,268,277,278,291,292,300,301,309,310,313,314,321,322,329,330,335,336,345,346,359,360,
    #            373,374,387,388,401,402,415,416,429,430,443,444,457,458,471,472,485,486,499,500,513,514,527,528,541,542,555,556,
    #            569,570,583,584,597,598,611,612,625,626,639,640,653,654,667,668,681,682,695,696,709,710,723,724,737,738,751,752,
    #            765,766,779,780,793,794,807,808,821,822,835,836,849,850,863,864,877,878,891,892,905,906,919,920,933,934,947,948,
    #            961,962,975,976,989,990,1003,1004,1017,1018,1031,1032,1045,1046,1059,1060,1073,1074,1087,1088,1091,1092,1105,1106,
    #            1119,1120,1123,1124,1137,1138,1151,1152,1155,1156,1169,1170,1183,1184,1187,1188,1201,1202,1215,1216,1229,1230,1237,
    #            1238,1251,1252,1259,1260,1273,1274,1281,1282,1295,1296,1309,1310,1323,1324,1331,1332,1345,1346,1359,1360,1373,1374,1387,1388,1401,1402,1415,1416,1429,1430,1438]
    # print(type(indices))
    ind= list(indices.split(' '))
    ind2=[]
    for i in ind:
        ind2.append(int(i))
    #
    # print('indices')
    # print(type(ind2))
    # print(ind2)
    # print(len(ind2))
    # colnum= (int(len(ind2)))/2+1
    # print('number of indiced columns')
    # print(colnum)

    f.close()

    parsed_data = [] # returned array by line
    #with open("FC202101.txt", "rb") as f:
        # contents = f.read().encode("IBM866")
        # print(contents)

    # with open("FC202101.txt", "r") as file1:
    #     with open("encodedfile.txt", "w",encoding='utf-8') as file2:
    #         file2.write(file1.read())
    # file1.close()
    # file2.close()
    #
    # print(file2)
    #encodedfile=open ('encodedfile.txt','w')

    with open ('FC202101.txt', 'rb') as f:
        for line in f:

            parts =[line[i:j] for i,j in zip(ind2, ind2[1:])]
            parsed_data.append(parts)
            print(len(parsed_data))




        new_parsed_data = [[s.strip() for s in sub_list  if s !=' '] for sub_list in parsed_data] #remove white spaces from data
            #final_parsed_data = [[s for s in sub_list  if s !=''] for sub_list in new_parsed_data] #remove white spaces from data

        #print(len(new_parsed_data))
        print("*************")
        print(new_parsed_data)
        df = pd.DataFrame(new_parsed_data)
        df2= df.iloc[:, :-111]
        #df2.columns=['ΕΤΟΣ', 'ΜΗΝΑΣ', 'ΚΩΔΙΚΟΣ ΠΟΛΛΑΠΛΟΥ', 'ΟΝΟΜΑ ΠΟΛΛΑΠΛΟΥ-1', 'ΟΝΟΜΑ ΠΟΛΛΑΠΛΟΥ-2', 'ΚΩΔΙΚΟΣ ΓΡΑΦΕΙΟΥ', 'ΟΝΟΜΑ ΓΡΑΦΕΙΟΥ', 'ΠΕΡΙΦΕΡΕΙΑ + ΑΡ.ΠΑΡΟΧΗΣ', 'ΛΟΓΑΡΙΑΣΜΟΣ ΣΥΜΒΑΣΗΣ', 'ΚΩΔΙΚΟΣ ΗΛΕΚΤΡΟΝΙΚΗΣ ΠΛΗΡΩΜΗΣ', 'ΟΝΟΜΑ ΠΕΛΑΤΗ', 'ΟΝΟΜΑ ΟΔΟΥ (Παροχης)', 'ΑΡΙΘΜ.ΟΔΟΥ (Παροχής)', 'ΠΟΛΗ (Παροχής)', 'ΑΦΜ', 'Α/Α ΕΚΔΟΣΗΣ ΛΟΓΑΡΙΑΣΜΟΥ', 'ΗΜΕΡΟΜ. ΕΚΔΟΣΗΣ ΛΟΓ/ΜΟΥ', 'ΤΙΜΟΛΟΓΙΟ', 'ΧΡΗΣΗ', 'ΚΩΔ.ΔΡΑΣΤΗΡΙΟΤΗΤΑΣ (ΣΤΑΚΟΔ)', 'ΑΡ.ΜΕΤΡΗΤΗ', 'ΠΡΟΚΑΤΑΒΟΛΗ', 'ΗΜΕΡ.ΤΕΛΕΥΤ. ΚΑΤΑΜΕΤΡΗΣΗΣ', 'ΗΜΕΡ.ΠΡΟΗΓ .ΚΑΤΑΜΕΤΡΗΣΗΣ', 'ΗΜΕΡΕΣ ΚΑΤΑΝΑΛΩΣΗΣ', 'ΠΑΡΟΥΣΑ ΕΝΔΕΙΞΗ', 'ΠΡΟΗΓΟΥΜΕΝΗ ΕΝΔΕΙΞΗ', 'ΣΥΝΤ. ΩΧΒ', 'ΚΑΤΑΝΑΛΩΣΗ ΕΝΕΡΓΕΙΑΣ (ΩΧΒ)', 'ΠΑΓΙΑ ΧΡΕΩΣΗ', 'ΑΞΙΑ ΕΝΕΡΓΕΙΑΣ', 'ΑΞΙΑ ΙΣΧΥΟΣ', 'ΚΟΣΤΟΣ ΔΙΚΑΙΩΜ.ΕΚΠΟΜΠΩΝ CO2', 'ΕΚΠΤΩΣΕΙΣ ( Εταιρικου Τιμ. )', 'ΕΚΠΤΩΣΕΙΣ ( Επιστρ.Παγίου )', 'ΕΚΠΤΩΣΕΙΣ ( Συνέπειας )', 'ΑΛΛΕΣ ΕΚΠΤΩΣΕΙΣ (Στήριξη Απόρων  Επιδοτήσεις κλπ.)', 'ΕΚΠΤΩΣΕΙΣ ΟΓΚΟΥ (Μέσης Τάσης)', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΧΡΕΩΣΗΣ ΠΡΟΜΗΘΕΙΑΣ ΡΕΥΜΑΤΟΣ', 'ΣΥΣΤΗΜΑ ΜΕΤΑΦΟΡΑΣ', 'ΣΥΣΤΗΜΑ ΔΙΑΝΟΜΗΣ', 'ΥΠ.ΚΟΙΝΗΣ ΩΦΕΛΕΙΑΣ', 'ΛΟΙΠΕΣ ΧΡΕΩΣΕΙΣ', 'ΕΤΜΕΑΡ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΡΥΘΜΙΖΟΜΕΝΩΝ ΧΡΕΩΣΕΩΝ', 'ΜΕΙΟΝ ΑΞΙΑ ΡΕΥΜΑΤΟΣ ΕΝΑΝΤΙ', 'ΕΙΔ.ΦΟΡΟΣ ΚΑΤΑΝΑΛΩΣΗΣ', 'ΕΙΔΙΚΟ ΤΕΛΟΣ 5‰', 'ΕΚΠΤΩΣΗ ΟΓΚΟΥ (Χαμηλής Τάσης)', 'ΤΟΚΟΙ ΥΠΕΡΗΜΕΡΙΑΣ + Χαρτόσημο 3 6 %', 'ΔΙΟΡΘΩΣΗ ΛΟΓΑΡΙΑΣΜΩΝ', 'ΑΚΥΡΩΣΗ ΛΟΓΑΡΙΑΣΜΩΝ', 'ΔΙΟΡΘΩΣΗ ΕΤΜΕΑΡ', 'ΔΙΟΡΘΩΣΗ ΕΦΚ', 'ΔΙΟΡΘΩΣΗ ΤΕΛΟΥΣ  5‰', 'ΧΡΕΩΣΕΙΣ ΔΙΚΤΥΟΥ (ΔΕΔΔΗΕ)', 'ΧΡΕΩΣΗ / ΣΥΜΨΗΦΙΣΜΟΣ ΠΡΟΚΑΤΑΒΟΛΗΣ', 'ΑΛΛΕΣ ΧΡΕΩΣΕΙΣ-ΠΙΣΤΩΣΕΙΣ (Τόκοι Διακανονισμού κλπ.)', 'ΜΕΤΑΦΟΡΑ ΑΠΌ ΛΟΓΑΡΙΑΣΜΟ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΠΡΟΗΓ.ΣΤΡΟΓΓΥΛΟΠΟΙΗΣΗ', 'ΠΑΡΟΥΣΑ ΣΤΡΟΓΓΥΛΟΠΟΙΗΣΗ', 'ΣΥΝΟΛΟ ΔΙΑΦΟΡΩΝ ΧΡΕΩΣΕΩΝ / ΠΙΣΤΩΣΕΩΝ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΛΟΙΠΩΝ ΕΚΤΑΚΤΩΝ ΧΡΕΩΣΕΩΝ', 'ΣΥΝΟΛΟ ΗΛΕΚΤΡΙΚΟΥ ΡΕΥΜΑΤΟΣ', 'ΑΞΙΑ ΦΠΑ - 1', 'ΠΟΣΟΣΤΟ ΦΠΑ - 1', 'ΠΟΣΟ ΦΠΑ - 1', 'ΑΞΙΑ ΦΠΑ - 2', 'ΠΟΣΟΣΤΟ ΦΠΑ - 2', 'ΠΟΣΟ ΦΠΑ - 2', 'ΑΞΙΑ ΦΠΑ - 3', 'ΠΟΣΟΣΤΟ ΦΠΑ - 3', 'ΠΟΣΟ ΦΠΑ - 3', 'ΑΞΙΑ ΦΠΑ - 4', 'ΠΟΣΟΣΤΟ ΦΠΑ - 4', 'ΠΟΣΟ ΦΠΑ - 4', 'ΣΥΝΟΛΟ ΦΠΑ', 'ΣΥΝΟΛΟ ΗΛ.ΡΕΥΜΑΤΟΣ + ΦΠΑ', 'ΔΗΜΟΤΙΚΑ ΤΕΛΗ - Μ2', 'ΔΗΜΟΤΙΚΑ ΤΕΛΗ - ΠΟΣΟ', 'ΔΗΜΟΤΙΚΟΣ ΦΟΡΟΣ - Μ2', 'ΔΗΜΟΤΙΚΟΣ ΦΟΡΟΣ - ΠΟΣΟ', 'ΤΕΛΟΣ ΑΚΙΝ.ΠΕΡΙΟΥΣΙΑΣ - ΤΜ', 'ΤΕΛΟΣ ΑΚΙΝ.ΠΕΡΙΟΥΣΙΑΣ - ΠΟΣΟ', 'ΑΝΑΔΡΟΜΙΚΑ  ΔΤ/ΔΦ', 'ΑΝΑΔΡΟΜΙΚΟ ΤΑΠ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΔΗΜΟΥ', 'ΕΡΤ', 'ΜΕΙΟΝ ΕΝΑΝΤΙ ΕΡΤ', 'ΣΥΝΟΛΟ ΕΡΤ', 'ΣΥΝΟΛΟ ΛΟΓΑΡΙΑΣΜΟΥ', 'ΣΥΝΟΛΟ ΤΡΕΧΟΝΤΑ ΜΗΝΑ', 'ΤΥΠΟΣ ΛΟΓΑΡΙΑΣΜΟΥ']
        # with open('columnsout3.txt') as d:
        #     col=d.read()
        #
        # col2=col.split(",")
        # print(col2)
        # print(type(col2))
        # df.columns=col2
        col2drop = [24]
        for x in range(1, 222, 2):
            col2drop.append(x)
        #print(col2drop)

        with pd.ExcelWriter('temp.xlsx') as writer:
            for col, dtype in df.dtypes.items():
                df[col] = df[col].apply(lambda x: x.decode("cp866"))
                df.to_excel(writer)

        df2 = pd.read_excel('temp.xlsx')
        df2.drop(df.columns[col2drop], axis=1, inplace=True)

        #df2.drop(df2.columns[[0,13]],axis = 1, inplace=True)

        df2.columns=['A/A','ΕΤΟΣ', 'ΜΗΝΑΣ', 'ΚΩΔΙΚΟΣ ΠΟΛΛΑΠΛΟΥ', 'ΟΝΟΜΑ ΠΟΛΛΑΠΛΟΥ-1', 'ΟΝΟΜΑ ΠΟΛΛΑΠΛΟΥ-2', 'ΚΩΔΙΚΟΣ ΓΡΑΦΕΙΟΥ', 'ΟΝΟΜΑ ΓΡΑΦΕΙΟΥ', 'ΠΕΡΙΦΕΡΕΙΑ + ΑΡ.ΠΑΡΟΧΗΣ', 'ΛΟΓΑΡΙΑΣΜΟΣ ΣΥΜΒΑΣΗΣ', 'ΚΩΔΙΚΟΣ ΗΛΕΚΤΡΟΝΙΚΗΣ ΠΛΗΡΩΜΗΣ', 'ΟΝΟΜΑ ΠΕΛΑΤΗ', 'ΟΝΟΜΑ ΟΔΟΥ (Παροχης)','ΠΟΛΗ (Παροχής)', 'ΑΦΜ', 'Α/Α ΕΚΔΟΣΗΣ ΛΟΓΑΡΙΑΣΜΟΥ', 'ΗΜΕΡΟΜ. ΕΚΔΟΣΗΣ ΛΟΓ/ΜΟΥ', 'ΤΙΜΟΛΟΓΙΟ', 'ΧΡΗΣΗ', 'ΚΩΔ.ΔΡΑΣΤΗΡΙΟΤΗΤΑΣ (ΣΤΑΚΟΔ)', 'ΑΡ.ΜΕΤΡΗΤΗ', 'ΠΡΟΚΑΤΑΒΟΛΗ', 'ΗΜΕΡ.ΤΕΛΕΥΤ. ΚΑΤΑΜΕΤΡΗΣΗΣ', 'ΗΜΕΡ.ΠΡΟΗΓ .ΚΑΤΑΜΕΤΡΗΣΗΣ', 'ΗΜΕΡΕΣ ΚΑΤΑΝΑΛΩΣΗΣ', 'ΠΑΡΟΥΣΑ ΕΝΔΕΙΞΗ', 'ΠΡΟΗΓΟΥΜΕΝΗ ΕΝΔΕΙΞΗ', 'ΣΥΝΤ. ΩΧΒ', 'ΚΑΤΑΝΑΛΩΣΗ ΕΝΕΡΓΕΙΑΣ (ΩΧΒ)', 'ΠΑΓΙΑ ΧΡΕΩΣΗ', 'ΑΞΙΑ ΕΝΕΡΓΕΙΑΣ', 'ΑΞΙΑ ΙΣΧΥΟΣ', 'ΚΟΣΤΟΣ ΔΙΚΑΙΩΜ.ΕΚΠΟΜΠΩΝ CO2', 'ΕΚΠΤΩΣΕΙΣ ( Εταιρικου Τιμ. )', 'ΕΚΠΤΩΣΕΙΣ ( Επιστρ.Παγίου )', 'ΕΚΠΤΩΣΕΙΣ ( Συνέπειας )', 'ΑΛΛΕΣ ΕΚΠΤΩΣΕΙΣ (Στήριξη Απόρων  Επιδοτήσεις κλπ.)', 'ΕΚΠΤΩΣΕΙΣ ΟΓΚΟΥ (Μέσης Τάσης)', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΧΡΕΩΣΗΣ ΠΡΟΜΗΘΕΙΑΣ ΡΕΥΜΑΤΟΣ', 'ΣΥΣΤΗΜΑ ΜΕΤΑΦΟΡΑΣ', 'ΣΥΣΤΗΜΑ ΔΙΑΝΟΜΗΣ', 'ΥΠ.ΚΟΙΝΗΣ ΩΦΕΛΕΙΑΣ', 'ΛΟΙΠΕΣ ΧΡΕΩΣΕΙΣ', 'ΕΤΜΕΑΡ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΡΥΘΜΙΖΟΜΕΝΩΝ ΧΡΕΩΣΕΩΝ', 'ΜΕΙΟΝ ΑΞΙΑ ΡΕΥΜΑΤΟΣ ΕΝΑΝΤΙ', 'ΕΙΔ.ΦΟΡΟΣ ΚΑΤΑΝΑΛΩΣΗΣ', 'ΕΙΔΙΚΟ ΤΕΛΟΣ 5‰', 'ΕΚΠΤΩΣΗ ΟΓΚΟΥ (Χαμηλής Τάσης)', 'ΤΟΚΟΙ ΥΠΕΡΗΜΕΡΙΑΣ + Χαρτόσημο 3 6 %', 'ΔΙΟΡΘΩΣΗ ΛΟΓΑΡΙΑΣΜΩΝ', 'ΑΚΥΡΩΣΗ ΛΟΓΑΡΙΑΣΜΩΝ', 'ΔΙΟΡΘΩΣΗ ΕΤΜΕΑΡ', 'ΔΙΟΡΘΩΣΗ ΕΦΚ', 'ΔΙΟΡΘΩΣΗ ΤΕΛΟΥΣ  5‰', 'ΧΡΕΩΣΕΙΣ ΔΙΚΤΥΟΥ (ΔΕΔΔΗΕ)', 'ΧΡΕΩΣΗ / ΣΥΜΨΗΦΙΣΜΟΣ ΠΡΟΚΑΤΑΒΟΛΗΣ', 'ΑΛΛΕΣ ΧΡΕΩΣΕΙΣ-ΠΙΣΤΩΣΕΙΣ (Τόκοι Διακανονισμού κλπ.)', 'ΜΕΤΑΦΟΡΑ ΑΠΌ ΛΟΓΑΡΙΑΣΜΟ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΠΡΟΗΓ.ΣΤΡΟΓΓΥΛΟΠΟΙΗΣΗ', 'ΠΑΡΟΥΣΑ ΣΤΡΟΓΓΥΛΟΠΟΙΗΣΗ', 'ΣΥΝΟΛΟ ΔΙΑΦΟΡΩΝ ΧΡΕΩΣΕΩΝ / ΠΙΣΤΩΣΕΩΝ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΛΟΙΠΩΝ ΕΚΤΑΚΤΩΝ ΧΡΕΩΣΕΩΝ', 'ΣΥΝΟΛΟ ΗΛΕΚΤΡΙΚΟΥ ΡΕΥΜΑΤΟΣ', 'ΑΞΙΑ ΦΠΑ - 1', 'ΠΟΣΟΣΤΟ ΦΠΑ - 1', 'ΠΟΣΟ ΦΠΑ - 1', 'ΑΞΙΑ ΦΠΑ - 2', 'ΠΟΣΟΣΤΟ ΦΠΑ - 2', 'ΠΟΣΟ ΦΠΑ - 2', 'ΑΞΙΑ ΦΠΑ - 3', 'ΠΟΣΟΣΤΟ ΦΠΑ - 3', 'ΠΟΣΟ ΦΠΑ - 3', 'ΑΞΙΑ ΦΠΑ - 4', 'ΠΟΣΟΣΤΟ ΦΠΑ - 4', 'ΠΟΣΟ ΦΠΑ - 4', 'ΣΥΝΟΛΟ ΦΠΑ', 'ΣΥΝΟΛΟ ΗΛ.ΡΕΥΜΑΤΟΣ + ΦΠΑ', 'ΔΗΜΟΤΙΚΑ ΤΕΛΗ - Μ2', 'ΔΗΜΟΤΙΚΑ ΤΕΛΗ - ΠΟΣΟ', 'ΔΗΜΟΤΙΚΟΣ ΦΟΡΟΣ - Μ2', 'ΔΗΜΟΤΙΚΟΣ ΦΟΡΟΣ - ΠΟΣΟ', 'ΤΕΛΟΣ ΑΚΙΝ.ΠΕΡΙΟΥΣΙΑΣ - ΤΜ', 'ΤΕΛΟΣ ΑΚΙΝ.ΠΕΡΙΟΥΣΙΑΣ - ΠΟΣΟ', 'ΑΝΑΔΡΟΜΙΚΑ  ΔΤ/ΔΦ', 'ΑΝΑΔΡΟΜΙΚΟ ΤΑΠ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ', 'ΣΥΝΟΛΟ ΔΗΜΟΥ', 'ΕΡΤ', 'ΜΕΙΟΝ ΕΝΑΝΤΙ ΕΡΤ', 'ΣΥΝΟΛΟ ΕΡΤ', 'ΣΥΝΟΛΟ ΛΟΓΑΡΙΑΣΜΟΥ', 'ΣΥΝΟΛΟ ΤΡΕΧΟΝΤΑ ΜΗΝΑ', 'ΤΥΠΟΣ ΛΟΓΑΡΙΑΣΜΟΥ']

        df2.to_excel('output.xlsx', index=False)






    #print('number_of_excel_col=' + str(len(columns)))
    print('number of excel columns')
    #print(len(columns))
    print("***************")
    #print(new_parsed_data)


parse_file()


