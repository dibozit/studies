import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None) #bunun içinde başlık yoktu, ilk satırdaki datayı başlık olarak
# alıyordu, bunun yerine header=None diyerek ilk satıra satır isimlerini getirmesini sağladık
df_txt = pd.read_csv('data.txt', delimiter='\t') #delimeter ile text halindeki datayı tablarla ayır komutunu verdik

#print(df_excel)
#print(df_txt)

df_csv.columns = ['First','Last','Address','City','State','Area Code', 'bisey'] #bunu yazarak kolonlara başlık ekledim
# print(df_csv)
# df_csv.to_excel('modified.xlsx') #bu komut ile yeni kolonu kaydediyorum

#print(df_csv.columns)
#print(df_csv['Last']) #bu komut ile Last başlıklı kolonun içindeki bilgileri çağırıyorsun
#print(df_csv[['State','Area Code']]) #double brackets kullanmak zorundasın because we're presenting the index of the
# dataframe as a list of columns
#print(df_csv['First'][0:3]) #First kolonunun ilk üç satırını getirir başlık dışındaki
#print(df_csv.iloc[2,1]) #satır, sütun sırasıyla yazıyorsun, bu üçüncü satır, ikinci sütundaki bilgi, 0,1,2 ve 0,
# 1 olduğu için 2,1 dedik. iloc da index location ın kısaltmasıymış

#mesela elimdeki datanın sadece belli kolonlarına ihtiyacım var, onları çekip kaydetmek için
#wanted_values= df_csv[['First','Last','State']]
#stored= wanted_values.to_excel('State_Location.xlsx',index=None)

