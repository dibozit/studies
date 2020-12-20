import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First','Last','Address','City','State','Area Code', 'Income']

df.drop(columns='Address', inplace=True) #Address kolonunu çıkarttım datadan
df=df.set_index('Area Code') #Area Code her kişi için unique, o yüzden area code'u index yaptım

#print(df.loc[8074]) #area code'u 8074 olan line'ı süzüyorum
#print(df.iloc[0]) #ilk sıradaki kişiyi çağırmak için

#herkesin ilk ismine bakmak için, this is a slice method. Because there is no number on the right side of the colomn,
# it is taking the location of the index 8074 to the end of the row
#print(df.loc[8074:,'First'])

#böyle süzdüğümde herkes nicname'leriyle geldi, sadece isimlere ulaşabilmek için her boşluktan sonra spliet etmesini
# istiyorum datanın. bunun için name kolonundaki her değerin string value'sunu çağırıp split etmeliyim
#print(df.First.str.split(expand=True))

#şimdi de sadece name'in ilk kolonu gelsin istiyorum
df.First = df.First.str.split(expand=True) #böyle yaparak First kolonunu yeniden tanımladım
print(df) #artık sadece first isimler geliyor, bir tek arada NaN diye biri var, onu kaldırmak istiyorum

df=df.replace(np.nan, 'N/A', regex=True) #nan'ı N/A olarak değiştirdim

to_excel=df.to_excel('modified.xlsx')