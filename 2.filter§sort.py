import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First','Last','Address','City','State','Area Code', 'Income']

#print(df.loc[df['City'] == 'Riverside']) #riverside'da yaşayan herkesi filtreledim

#print(df.loc[ (df['City']=='Riverside') & (df['First']=='John') ] ) #riverside'da yaşayan John isimli kişileri filtreledim

#çalışmada yeni bir kolon oluşturuyorum ve koşula göre, income şu kadarsa bu kadar tax olsun diye dolduruyorum:
df['Tax %']=df['Income'].apply(lambda x: .15 if 10000<x<40000 else .2 if 40000<x<80000 else .25)
print(df)

#Taxes Owed diye yeni bir kolon açtım ödenecek tax'in hesaplandığı
df['Taxes Owed'] = df['Income'] * df['Tax %']
print(df['Taxes Owed'])

#bazı kolonları çıkartacağım
to_drop=['Area Code','First','Address']
df.drop(columns=to_drop, inplace=True)
print(df)

#kolonlarda 60000'den küçük olan ve büyük olan gelirleri ayıralım
df['Test Col']= False
df.loc[df['Income']<60000, 'Test Col']=True
print(df) #bu tüm listeyi karşısında True ve False ile getirir
print(df.groupby(['Test Col']).mean()) #bu true olanların ortalama değerlerini ve false olanların ortalama
# değerlerini her kolon için getirir. eğer bu datanın her kolonu number lardan oluşmasaydı mean komutu bize sıkıntı
# çıkartırdı
print(df.groupby(['Test Col']).mean().sort_values('Income')) #bu komut true ve falseların ortlama değerlerini Income
# küçükten büyüğe sıralanacak şekilde sıraladı