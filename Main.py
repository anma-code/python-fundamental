# Sekuential
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu"')
print('Maka budi berangkat ke toko')
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 75
jumlah_telur = 1571
print(f'Jumlah botol susu {jumlah_botol_susu} btl')
print(f'Jumlah telur {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Budi mengecek harga, dan ternyata uangnya cukup')
    print('Budi membeli 1 botol susu')
    if jumlah_telur > 0:
        print('Budi membeli 6 butir telur')
    else:
        print('Budi tidak jadi beli telur')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('Memberikan hasilnya kepada ibu')
