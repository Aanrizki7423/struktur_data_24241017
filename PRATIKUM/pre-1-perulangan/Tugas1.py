jumlah_baris = int(input("Masukkan jumlah baris: "))
angka_range = range(1, jumlah_baris * 2, 2) # ramge (mulai, berhenti, step)

spasi_awal = jumlah_baris - 1 # 
for i in angka_range: 
    print(' ' * spasi_awal + '*' * i)
    spasi_awal -= 1 
