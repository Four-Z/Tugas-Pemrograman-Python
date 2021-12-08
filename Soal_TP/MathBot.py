import random


def pilihMode():
    print("""
Halo Selamat Datang di Math Bot
Pilih Mode:
1. Penjumlahan
2. Pengurangan
3. Campur
4. Akhiri program
    """)
    mode = int(input("Masukkan Perintah: "))
    return mode


def pilihKuis(mode):
    listMode = ["Penjumlahan", "Pengurangan", "Campur"]
    print(f"""
Baik, pilih mode {listMode[mode-1]} ya, sekarang pilih jenis kuis apa?
Pilih kuis:
1. Kuis Lepas
2. Kuis 5
3. Ganti mode
4. Akhiri Program
    """)
    kuis = input("Masukkan jenis kuis: ")
    return kuis


def Mode(mode, kuis):
    Listoperator = ["+", "-"]
    if(mode == 1):
        operator = Listoperator[0]
    elif(mode == 2):
        operator = Listoperator[1]

    listKuis = [True, 4]
    modeKuis = listKuis[int(kuis)-1]

    while(modeKuis >= 0):
        if(mode == 3):
            operator = random.choice(Listoperator)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print(f"Berapa {a} {operator} {b}?")
        jawab = (input("Jawab: ")).lower()
        temp = str(eval(f"{a}{operator}{b}"))
        if(jawab == temp):
            print("Hore Benar")
        elif(jawab == "akhiri kuis"):
            break
        else:
            print(f"Masih kurang tepat, ya. Jawabannya adalah {temp} ")

        if(type(modeKuis) == int):
            modeKuis -= 1


while(True):
    mode = pilihMode()

    if(mode == 4):
        print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
        break
    elif(mode <= 3):
        kuis = pilihKuis(int(mode))
    elif(mode > 4):
        continue

    if(kuis == "1" or kuis == "2"):
        Mode(mode, kuis)
    elif(kuis == "3"):
        continue
    elif(kuis >= "4"):
        print("Terima kasih telah bermain kuis ini. Sampai jumpa lagi!")
        break
