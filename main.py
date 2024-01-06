import pandas as pd
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fonksiyonlar
from scipy.stats import mode #numpy içerisinde mod hesaplama fonksiyonu olmadığından scipy kütüphanesinden stats modulunu ekliyorum.
from sklearn.preprocessing import MinMaxScaler



#Pandas paketindeki read_excel fonksiyonu ile verimi içeriye alıyorum.
veriyolu =r'C:\Users\agnfu\OneDrive\Masaüstü\FBÜ\veri\proje_iiçin\bist.xlsx'
veriyolu2 = r'C:\Users\agnfu\OneDrive\Masaüstü\FBÜ\veri\proje_iiçin\sasa.xlsx'
veriyolu3=r'C:\Users\agnfu\OneDrive\Masaüstü\FBÜ\veri\proje_iiçin\usd.xlsx'
veri = pd.read_excel(veriyolu)  # Sütun başlıkları olmadığını belirtiyoruz
veri.columns = ['Tarih', 'Bist', 'Açılış', 'Yüksek', 'Düşük', 'Hac.', 'Fark %']  # Sütun isimlerini tanımlıyoruz
veri2 = pd.read_excel(veriyolu2)  # Sütun başlıkları olmadığını belirtiyoruz
veri2.columns = ['Tarih', 'Sasa_fiyat', 'Açılış', 'Yüksek', 'Düşük', 'Hac.', 'Fark %']  # Sütun isimlerini tanımlıyoruz
veri3=pd.read_excel(veriyolu3)
veri3.columns=['Tarih', 'USD/TRY', 'Açılış', 'Yüksek', 'Düşük', 'Fark %']

#print(veri.head())
#print(veri2.head()) #veri2 ilk 5 veri kontrol
#print(veri2.dtypes) #verinin tipini öğrenme

yeni_veri=veri.iloc[:,:2]
yeni_veri2=(veri2.iloc[:,1])
yeni_veri4=(veri3.iloc[:,1])
yeni_veri3=pd.concat([yeni_veri,yeni_veri2,yeni_veri4],axis=1)#[] içine almamızın nedeni concat içine sadece 1 veri girer
yv=yeni_veri3.fillna(46) #nan olan verimize 46 değerini atıyoruz
yv=yv[::-1]#veriyi ters çeviriyoruz
yv.iloc[0,3]=18.6

print(yv.head())


x=yv['Tarih']
y=yv['Sasa_fiyat']
a=yv['Bist']
usd=yv['USD/TRY']

#basit hesaplamalar
fonksiyonlar.basit_hesap(a)
print("************")
fonksiyonlar.basit_hesap(yv['Sasa_fiyat'])
print("************")
fonksiyonlar.basit_hesap(usd)
print("************")

#grafik çizdirme
fonksiyonlar.grafik_çizme(x,yv['Bist'])#tarih bist x=tarih a=bist #2023 yılı **** değer grafiği
print("************")
fonksiyonlar.grafik_çizme(x,yv['Sasa_fiyat'])#tarih sasa
print("************")
fonksiyonlar.grafik_çizme(x,yv['USD/TRY'])#tarih usd
print("************")




#box plate
fonksiyonlar.box_plate(a)
fonksiyonlar.box_plate(y)
fonksiyonlar.box_plate(usd)

#histogram
fonksiyonlar.histogram(a)
fonksiyonlar.histogram(y)
fonksiyonlar.histogram(usd)


#dağılım grafiği
fonksiyonlar.dağılım_grafiği(a)
fonksiyonlar.dağılım_grafiği(y)
fonksiyonlar.dağılım_grafiği(usd)

#yoğunluk grafiği
fonksiyonlar.yoğunlukGrafiği(a)
fonksiyonlar.yoğunlukGrafiği(y)
fonksiyonlar.yoğunlukGrafiği(usd)

#normalize edilmiş yv=nyv
nyv=yv
scaler=MinMaxScaler()
nyv['Bist']=scaler.fit_transform(nyv['Bist'].values.reshape(-1, 1))
nyv['Sasa_fiyat']=scaler.fit_transform(nyv['Sasa_fiyat'].values.reshape(-1, 1))
nyv['USD/TRY']=scaler.fit_transform(nyv['USD/TRY'].values.reshape(-1, 1))
print(nyv['Bist'])
#ısı haritası
fonksiyonlar.ısı_haritası(nyv[['Bist','Sasa_fiyat','USD/TRY']])

#serpilme diyagramı --->>>iki veri arasıdaki ilişki inceleme için

fonksiyonlar.serpilme_diyagramı(nyv['Bist'],nyv['Sasa_fiyat']) #bist ve sasa
fonksiyonlar.serpilme_diyagramı(nyv['Bist'],nyv['USD/TRY']) #bist ve usd
fonksiyonlar.serpilme_diyagramı(nyv['Sasa_fiyat'],nyv['USD/TRY']) #sasa ve usd
#t testi
fonksiyonlar.t_testi(yv)