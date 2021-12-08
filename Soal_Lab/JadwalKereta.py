def perintah():
    print('''
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT
''')
    command = input("Masukkan perintah: ")
    return command


jadwal = []


def jadwalBerangkat():
    print("Selamat datang! Silakan masukkan jadwal KA:")
    while(True):
        inp = input()

        if(inp == 'selesai'):
            return
        else:
            jadwal.append(inp.split(" "))


def info_tujuan():
    global jadwal
    tujuan = []
    for i in range(len(jadwal)):
        if(jadwal[i][1] not in tujuan):
            tujuan.append(jadwal[i][1])

    print("KA di stasiun ini memiliki tujuan akhir:")
    for i in tujuan:
        print(i)


def check_kelas(command):
    if command[2] == "Eksekutif":
        command[2] = '1'
    elif command[2] == "Bisnis":
        command[2] = '2'
    elif command[2] == "Ekonomi":
        command[2] = '3'


def tujuan_kelas(command):
    command = command.split()
    check_kelas(command)
    check = True
    global jadwal
    for i in range(len(jadwal)):
        if jadwal[i][0][0] == command[2] and jadwal[i][1] == command[1]:
            check = False
            print(
                f"KA {jadwal[i][0]} berangkat pukul {jadwal[i][2]} dengan harga tiket {jadwal[i][3]}")

    if check:
        print("Tidak ada jadwal KA yang sesuai.")


def tujuan_kelas_termurah(command):
    command = command.split()
    check_kelas(command)
    global jadwal

    jadwal_termurah = []
    for i in range(len(jadwal)):
        if jadwal[i][0][0] == command[2] and jadwal[i][1] == command[1]:
            jadwal_termurah.append(jadwal[i])

    harga = jadwal_termurah[0][3]
    index = 0
    for i in range(len(jadwal_termurah)):
        if(int(jadwal_termurah[i][3]) < int(harga)):
            harga = int(jadwal_termurah[i][3])
            index = i

    print(
        f"KA {jadwal_termurah[index][0]} berangkat pukul {jadwal_termurah[index][2]} dengan harga tiket {jadwal_termurah[index][3]}")


def tujuan_jam(command):
    command = command.split()
    check = True
    global jadwal
    for i in range(len(jadwal)):
        if int(jadwal[i][2]) <= int(command[2]) and jadwal[i][1] == command[1]:
            check = False
            print(
                f"KA {jadwal[i][0]} berangkat pukul {jadwal[i][2]} dengan harga tiket {jadwal[i][3]}")

    if check:
        print("Tidak ada jadwal KA yang sesuai.")


def tujuan_jam_termurah(command):
    command = command.split()
    global jadwal

    jadwal_termurah = []
    for i in range(len(jadwal)):
        if int(jadwal[i][2]) <= int(command[2]) and jadwal[i][1] == command[1]:
            jadwal_termurah.append(jadwal[i])

    harga = jadwal_termurah[0][3]
    index = 0
    for i in range(len(jadwal_termurah)):
        if(int(jadwal_termurah[i][3]) < int(harga)):
            harga = int(jadwal_termurah[i][3])
            index = i

    print(
        f"KA {jadwal_termurah[index][0]} berangkat pukul {jadwal_termurah[index][2]} dengan harga tiket {jadwal_termurah[index][3]}")


jadwalBerangkat()
while(True):
    command = perintah()
    try:
        if command == "INFO_TUJUAN":
            info_tujuan()
        elif "TUJUAN_KELAS " in command:
            tujuan_kelas(command)
        elif "TUJUAN_KELAS_TERMURAH " in command:
            tujuan_kelas_termurah(command)
        elif "TUJUAN_JAM " in command:
            tujuan_jam(command)
        elif "TUJUAN_JAM_TERMURAH " in command:
            tujuan_jam_termurah(command)
        elif command == "EXIT":
            print("Terima kasih sudah menggunakan program ini!")
            break
        else:
            print("Perintah yang dimasukkan tidak valid.")
    except:
        print("Tidak ada jadwal KA yang sesuai")
