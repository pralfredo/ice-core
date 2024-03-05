def max_count(str): 
    # split the string by spaces in a
    a = str.split(" ")
    factor = 0.66
    greenland_count = 0; antarctica_count = 0; others_count =0
    # search for pattern in a
    for i in range(0, len(a)):
        # if match found increase count
        if (a[i] == "greenland" or a[i] == "gisp" or a[i] == "ngrip" or a[i] == "neem" or a[i] == "northgrip" or a[i] == "dye" or a[i] == "gris"):
           greenland_count = greenland_count + 1  
        elif (a[i] == "antarctic" or a[i] == "antarctica" or a[i] == "vostok" or a[i] == "epica" or a[i] == "wais" or a[i] == "maud" or a[i] == "dronning" or a[i] == "ross" or a[i] == "edc" or a[i] == "siple" or a[i] == "byrd" or a[i] == "talos" or a[i] == "taylor" or a[i] == "dml" or a[i] == "taldice" or a[i] == "concordia" or a[i] == "sam"):
           antarctica_count = antarctica_count + 1
        elif (a[i] == "tibetan" or a[i] == "asia" or a[i] == "european" or a[i] == "europe" or a[i] == "america" or a[i] == "china" or a[i] == "alpine" or a[i] == "asian" or a[i] == "alps" or a[i] == "svalbard" or a[i] == "american" or a[i] == "canada" or a[i] == "himalayas" or a[i] == "guliya" or a[i] == "everest" or a[i] == "andes" or a[i] == "australia" or a[i] == "iceland" or a[i] == "alaska" or a[i] == "altai" or a[i] == "shan" or a[i] == "loess" or a[i] == "dunde" or a[i] == "quelccaya" or a[i] == "himalaya" or a[i] == "tien" or a[i] == "illimani" or a[i] == "patagonia" or a[i] == "dasuopu" or a[i] == "laki" or a[i] == "himalayan"):
            others_count = others_count + 1 
    if (greenland_count+antarctica_count+others_count==0):
        return 0
    elif (factor*greenland_count>antarctica_count and factor*greenland_count>others_count):
        return 1
    elif (factor*antarctica_count>greenland_count and factor*antarctica_count>others_count):
        return 2
    elif (factor*others_count>greenland_count and factor*others_count>antarctica_count):
        return 3
    else:
        if greenland_count==0: return 4
        elif antarctica_count==0: return 5
        elif others_count==0: return 6
        else:
            return 7
     
## Making Dictionary of Words
import pandas as pd
file_path = "words.xlsx"
df = pd.read_excel(file_path)
dct = df.groupby('Years')['Words'].apply(list).to_dict()
l = [{k:v} for k,v in dct.items()]
result = {} 
for d in l:
    result.update(d)

## Making Dictionary of MaxCount
n = 0; g = 0; a = 0; o = 0; p1 = 0; p2 = 0; p3 = 0; p = 0; dict = {}
for i in range(1969,2022):
    gg = 0; aa = 0; oo = 0
    if i!=1971:
        list = result[i]
        for words in list:
            out = max_count(words)
            if out == 0: n+=1
            elif out == 1: g+=1; gg+=1
            elif out == 2: a+=1; aa+=1
            elif out == 3: o+=1; oo+=1
            elif out == 4: p1+=1; aa+=0.5; oo+=0.5
            elif out == 5: p2+=1; gg+=0.5; oo+=0.5
            elif out == 6: p3+=1; aa+=0.5; gg+=0.5
            elif out == 7: p+=1
    dict[i] = [gg, aa, oo]
print(p1+p2+p3+p)

## Making xlsx of the prepped Dict
all = []
for year, list in dict.items():
    all.append(list)
import xlsxwriter
with xlsxwriter.Workbook('test.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(all):
        worksheet.write_row(row_num, 0, data)