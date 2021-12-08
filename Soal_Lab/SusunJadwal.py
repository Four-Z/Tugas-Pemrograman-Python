def printPerintah():
    print("""
=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
""")


MENIT_DALAM_JAM = 60
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]
NAMA_HARI = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]

MATKUL_TERSEDIA = [
    ["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] + JAM[9] + 40],
    ["ddp 1 c", HARI[2] + JAM[8] + 0, HARI[2] + JAM[9] + 40],
    ["ddp 1 b", HARI[1] + JAM[8] + 0, HARI[1] + JAM[9] + 40],
    ["manbis", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
    ["matdis 1 a", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
    ["matdis 1 b", HARI[0] + JAM[9] + 0, HARI[0] + JAM[10] + 40],
    ["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]


MATKUL_DIAMBIL = []
while(True):
    printPerintah()
    menu = (input("Masukkan Pilihan: "))

    if menu == "1":
        matkul = input("Masukkan nama matkul: ").lower().strip()
        count = 0
        for i in MATKUL_TERSEDIA:
            if matkul in i:
                MATKUL_DIAMBIL.extend([i])
                count = 1
        if(count == 0):
            print("Matkul tidak ditemukan")

    elif menu == "2":
        matkul = input("Masukkan nama matkul: ").lower().strip()
        count = 0
        for i in MATKUL_DIAMBIL[:]:
            if matkul in i:
                MATKUL_DIAMBIL.remove(i)
                count = 1
        if(count == 0):
            print("Matkul tidak ditemukan")

    elif menu == "3":
        count = 0
        for i in range(len(MATKUL_DIAMBIL)):
            for j in range(1, len(MATKUL_DIAMBIL[0])-1):
                for k in range(len(MATKUL_DIAMBIL)):
                    if(i != k):
                        if(MATKUL_DIAMBIL[i][j] >= MATKUL_DIAMBIL[k][j] and MATKUL_DIAMBIL[i][j] <= MATKUL_DIAMBIL[k][j+1]):
                            print(
                                f"{MATKUL_DIAMBIL[k][0]} bentrok {MATKUL_DIAMBIL[i][0]}")
                            count = 1
        if(count == 0):
            print("Tidak ada mata kuliah yang bermasalah")

    elif menu == "4":
        if(len(MATKUL_DIAMBIL) > 0):
            for i in range(len(MATKUL_DIAMBIL)):
                mk = MATKUL_DIAMBIL[i][0]
                mk = mk.upper()
                for j in range(1, len(MATKUL_DIAMBIL[0])):
                    if(j == 1):
                        hari_start = MATKUL_DIAMBIL[i][j]//MENIT_DALAM_HARI
                        waktu_start = (MATKUL_DIAMBIL[i][j] -
                                       HARI[hari_start]) / MENIT_DALAM_JAM
                        jam_start = str(int(waktu_start//1)).zfill(2)
                        menit_start = str(round(waktu_start % 1)).zfill(2)
                    if(j == 2):
                        hari_end = MATKUL_DIAMBIL[i][j]//MENIT_DALAM_HARI
                        waktu_end = (MATKUL_DIAMBIL[i][j] -
                                     HARI[hari_end]) / MENIT_DALAM_JAM
                        jam_end = str(int(waktu_end//1)).zfill(2)
                        menit_end = str(round(waktu_end % 1*60)).zfill(2)

                print(
                    f'{mk}   {NAMA_HARI[hari_start]}, {jam_start}.{menit_start} s/d {NAMA_HARI[hari_end]}, {jam_end}.{menit_end}')
        else:
            print("Tidak ada matkul yang diambil")

    elif menu == "5":
        print("Terima Kasih!")
        break

    else:
        print("Maaf, pilihan tidak tersedia")
