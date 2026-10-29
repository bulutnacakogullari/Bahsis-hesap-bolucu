print('---Bahşiş ve Hesap Bölücü---')
# Girdiler
tutar = float(input('Toplam tutarı girin (₺): '))
kisi_sayisi = int(input('Kişi sayısını girin: '))
bahsis_orani = float(input('Bahşiş oranını girin (%): '))

# İşlemler
bahsis_tutari = tutar * (bahsis_orani / 100)
toplam_tutar = tutar + bahsis_tutari
kisi_basi = toplam_tutar / kisi_sayisi

# Çıktı
print(f'\nToplam Tutar (Bahşiş Dahil): {toplam_tutar:.2f} ₺')
print(f'Kişi Başı Ödenecek Tutar: {kisi_basi:.2f} ₺')
