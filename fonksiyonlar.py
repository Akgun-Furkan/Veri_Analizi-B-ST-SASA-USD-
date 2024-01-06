import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind
from scipy.stats import mode #numpy içerisinde mod hesaplama fonksiyonu olmadığından scipy kütüphanesinden stats modulunu ekliyorum.
def basit_hesap(x):
    print(x.name)
    print(" Ortalama:", np.mean(x))  # ortalama hesaplayıp text olarak bastırıyorum
    print("Medyan:", np.median(x))  # medyan hesaplayıp text olarak bastırıyorum
    print("Standard Sapma:", np.std(x))  # standart sapma hesaplayıp text olarak bastırıyorum
    print("Minimum:", np.min(x))  # en  küçük değer hesaplayıp text olarak bastırıyorum
    print("Maximum:", np.max(x))  # En büyük değer hesaplayıp text olarak bastırıyorum
    print("25th Percentile:", np.percentile(x, 25))  # %25 percentile çıkarıyorum
    print("75th Percentile:", np.percentile(x, 75))
    return 0
def grafik_çizme(x,y):
    # Grafiğimi çizdirmeden önce x ekseninde hangi değişken olacak, y ekseninde hangi değişken olacak planlıyorum.
    plt.figure(figsize=(5, 3))
    plt.plot(x, y)
    # Grafiği güzelleştirecek dokunuşlar yapıyorum.
    title=input("tablonun adını giriniz===")
    plt.title(title)
    plt.xlabel(input("x ekseninin adını giriniz==="))
    a=plt.ylabel(input ("y ekseninin adını giriniz==="))
    a=str(a)
    if(a=="usd"):
        plt.ylim(0,30)
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')

    return plt.show()

def serpilme_diyagramı(x,y):
    # grafiğimizin büyüklüğünü ayrarlayalım
    plt.figure(figsize=(7, 4))
    # serpilme diyagramını (scatterplot) çizdirelim
    plt.scatter(x,y)
    plt.title(input("serpilme diyagramına vermek istediğiniz ismi giriniz==="))
    plt.xlabel(input("x eksenine vermek istediğiniz değeri giriniz=="))
    plt.ylabel(input("y eksenine girmek istediğiniz değeri giriniz"))

    krls = np.corrcoef(x,y)  # korolasyon hesaplama
    print("Korolasyon değer==",krls)
    return plt.show()
#değerleri normalize etmek gerekli!!!!!

#krolasyon sıcaklık haritası
def ısı_haritası(veri):

    krls = veri.corr() # 3'lü korolasyon hesaplama
    sns.set(font_scale=1.0)  # Heatmap üzerindeki karakter büyüklüğünü ayrarladım
    plt.figure(figsize=(8, 6))  # figurun büyüklüğünü ayararladım
    sns.heatmap(krls, annot=True, cmap="coolwarm", linewidths=.5, fmt=".2f", square=True)
    #Argumanların açıklaması Matris:Korelasyon matrisini sakladığımız nesne, annot: True oldugu için kutuların üzerine korelasyon değerleri basılmıştır.
    #cmap= Soğuk renklerde düşük korelasyon, sıcak renkler de yüksek korelasyon atamaktadır.
    #linewidth kutular arası aralıkları ayrarlar
    #fmt virgulden sonraki ondalık gösterim sayısını ayrarlar
    plt.title("Korelasyon Sıcaklık Haritası")
    return plt.show()

#box plat
#Her zaman olduğu gibi bir x değişkeni tanımlayalım. Bu sefer aylık Lpg fiyatlarını incleyelim.
def box_plate(x):

    plt.figure(figsize=(8, 6)) #Boxplot'ın büyüklüğünü ayrarlıyorum.
    box = plt.boxplot(x, vert=False, patch_artist=True) #Boxplot'ı çizdirip box isimli nesnede saklıyorum.
    plt.title(input("Title giriniz")) #Boxplot'uma bir başlık koyuyorum
    plt.xlabel("Değerler") #Boxplot'da bildiğiniz gibi bir y ekseni yok o nedenle sadece x ekseni için etiket giriyorum.
    plt.grid(True) #Izgara ister miyim?
    return plt.show()

def histogram(x):
    # histogramı tekrar çizdirelim.
    # seaborn dan çizdirdiğim için sns'yi çağırdım.
    # Medyanı hesaplayalım
    median = np.median(x)

    # Aritmetik Ortalamayı hesaplayalım
    mean = np.mean(x)

    # Calculate standard deviation
    stddev = np.std(x)

    # histogram çizdirelim.
    # seaborn dan çizdirdiğim için sns'yi çağırdım.
    sns.histplot(data=x)

    # mod, medyan ve ortalamnın yerini gösteren dik çizgileri ekleyelim
    plt.axvline(median, color='blue', linestyle='dashed', label='Medyan')
    plt.axvline(mean, color='green', linestyle='solid', label='Ortalama')

    # color çizginin rengini atar, linestyle düz çizgi veya nokta nokta şeklinde çizdirir, label üzerine etiket koyar

    # Set the title and labels
    plt.title("Veri Setinin Ortalama, Ortanca (Medyan) ve En Sık Değer (Mod) içeren Histogramı ")
    plt.xlabel(input("x ekseni isim"))
    plt.ylabel("Frekans")

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()
def dağılım_grafiği(veri):
    # Standart sapma hesaplama
    standart_sapma = np.std(veri)

    # Standart hata hesaplama
    standart_hata = standart_sapma / np.sqrt(len(veri))

    # Dağılım grafiğini çizme
    sns.histplot(veri, kde=True)  # Histogram ve yoğunluk grafiği
    plt.axvline(np.mean(veri), color='red', linestyle='--', label='Ortalama')  # Ortalama çizgisi
    plt.axvline(np.mean(veri) + standart_sapma, color='green', linestyle='--',

                label='Standart Sapma')  # Standart sapma üst sınırı
    plt.axvline(np.mean(veri) - standart_sapma, color='green', linestyle='--',
                label='Standart Sapma')  # Standart sapma alt sınırı
    plt.legend()  # Açıklamaları ekleme
    plt.show()

def yoğunlukGrafiği(x):
    # Yoğunluk grafiği (density plot) çizimi
    plt.figure(figsize=(8, 6))
    sns.kdeplot(x, shade=True, color='green')
    plt.title('Dağılım - Yoğunluk Grafiği')
    plt.xlabel('Değerler')
    plt.ylabel('Yoğunluk')
    return plt.show()
def t_testi(veri):
    # Verilerin korelasyonunu kontrol etme
    korelasyon = veri.corr()

    # T-testi uygulama (BIST 100 ile SASA hisse fiyatları arasında USD_TRY kuruna bağlı bir farklılık var mı?)
    t_stat, p_value = stats.ttest_ind(veri['Sasa_fiyat'], veri['Bist'], equal_var=False)

    print("\nT-testi Sonuçları:")
    print(f"T İstatistiği: {t_stat}")
    print(f"P Değeri: {p_value}")

    alpha = 0.05  # Anlamlılık düzeyi
    if p_value < alpha:
        print("İstatistiksel olarak anlamlı bir farklılık bulundu. H0 reddedildi.")
        test_result="h0 reddedildi"
    else:
        print("İstatistiksel olarak anlamlı bir farklılık bulunamadı. H0 kabul edildi.")
        test_result = "h0 kabul edildi"

    sns.barplot(x=['SASA Hisse','BIST 100 '], y=[np.mean(veri['Sasa_fiyat']), np.mean(veri['Bist'])])
    plt.ylabel('Ortalama Değer')
    plt.title(f'T Testi Sonucu: p={p_value:.4f} ({test_result})')
    plt.show()




















