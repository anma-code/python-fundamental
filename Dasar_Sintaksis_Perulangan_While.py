"""
Program Perulangan Membaca Buku dengan While
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua buku"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    print("Baca 1 buku yang belum dibaca")
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1