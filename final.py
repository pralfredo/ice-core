## Making Dictionary of Words
import pandas as pd
file_path = "final.xlsx"
df = pd.read_excel(file_path)
dct = df.groupby('Years')['Topics'].apply(list).to_dict()
list = [{k:v} for k,v in dct.items()]
result = {} 
for dx in list:
    result.update(dx)

print(result)
## Making Dictionary of MaxCount
dict = {}
for x in range(1969,2022):
    a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0
    if x!=1971:
        list = result[x]
        for out in list:
            print(out)
            if out == 1: a+=1
            elif out == 2: b+=1
            elif out == 3: c+=1
            elif out == 4: d+=1
            elif out == 5: e+=1
            elif out == 6: f+=1
            elif out == 7: g+=1
            elif out == 8: h+=1
            elif out == 9: i+=1
            elif out == 10: j+=1
            elif out == 11: k+=1
            elif out == 12: l+=1
    dict[x] = [a, b, c, d, e, f, g , h, i, j, k, l]
print(dict)


## Making xlsx of the prepped Dict
all = []
for year, list in dict.items():
    all.append(list)
import xlsxwriter
with xlsxwriter.Workbook('what.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(all):
        worksheet.write_row(row_num, 0, data)