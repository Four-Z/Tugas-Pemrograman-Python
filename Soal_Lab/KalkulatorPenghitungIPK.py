print("Selamat datang di Kalkulator IPK")


def inputMK():
    jumlah_MK = int(input("Masukkan jumlah Mata Kuliah: "))
    if(jumlah_MK <= 0):
        while(jumlah_MK <= 0):
            print("Nilai yang kamu masukkan tidak valid")
            jumlah_MK = int(input("Masukkan jumlah Mata Kuliah: "))
        return jumlah_MK
    return jumlah_MK


mutu_lulus = 0
mutu_total = 0
total_sks = 0
total_sks_lulus = 0


def kalkulasi(nilai, jumlahSKS):
    global mutu_lulus
    global mutu_total
    global total_sks
    global total_sks_lulus
    minimal = 0
    maksimal = 50
    bobot = 0
    while(True):

        if(nilai < 40):
            bobot = 0
        elif(nilai >= 40 and nilai < 55):
            bobot = 1

        if(nilai >= minimal and nilai < maksimal):
            mutu = jumlahSKS*bobot
            total_sks += jumlahSKS
            mutu_total += mutu
            if(nilai >= 55):
                mutu_lulus += mutu
                total_sks_lulus += jumlahSKS

            break
        minimal = maksimal
        maksimal += 5

        if(bobot < 2.00):
            bobot += 1
        elif(bobot == 2.00 or bobot == 3.00):
            bobot += 0.30
        elif(round(bobot % 1, 2) == 0.30):
            bobot += 0.40
        elif(round(bobot % 1, 2) == 0.70):
            bobot += 0.30

        bobot = round(bobot, 2)


jumlah_MK = inputMK()
for i in range(1, jumlah_MK+1):
    mataKuliah = input(f"\nMasukkan nama mata kuliah ke-{i}: ")

    jumlahSKS = int(input(f"Masukkan jumlah SKS {mataKuliah} :"))
    if(jumlahSKS <= 0):
        while(jumlahSKS <= 0):
            print("Nilai yang kamu masukkan tidak valid")
            jumlahSKS = int(input(f"Masukkan jumlah SKS {mataKuliah} :"))

    nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
    if(nilai < 0):
        while(nilai < 0):
            print("Nilai yang kamu masukkan tidak valid")
            nilai = float(input("Masukkan nilai yang kamu dapatkan: "))

    kalkulasi(nilai, jumlahSKS)

ipk = round(mutu_lulus/total_sks_lulus, 2)
ipt = round(mutu_total/total_sks, 2)

mutu_lulus = round(mutu_lulus, 2)
mutu_total = round(mutu_total, 2)

print(f"Jumlah SKS Lulus: {total_sks_lulus} / {total_sks}")
print(f"Jumlah Mutu Lulus: {mutu_lulus} / {mutu_total}")
print(f"IPK: {mutu_lulus} / {total_sks_lulus}: {ipk}")
print(f"IPT: {mutu_total} / {total_sks}: {ipt}")
