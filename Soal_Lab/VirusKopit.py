
def perintah():
    print('''
List perintah:
1. RANTAI_PENYEBARAN
2. CEK_PENULARAN
3. EXIT
''')


rantai = {}
print("Masukkan rantai penyebaran:")
while(True):
    temp = list(input().split(" "))
    rantai_temp = {temp[0]: temp[1:len(temp)]}
    if temp[0] == 'selesai':
        break
    else:
        rantai.update(rantai_temp)

check2 = True


def rantai_penyebaran(penular):
    global rantai
    global check2
    try:
        for i in range(len(rantai[penular])):
            print(f"-{rantai[penular][i]}")
            rantai_penyebaran(rantai[penular][i])
    except:
        print(f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")
        check2 = False


def cek_penularan(tertular, penular):
    global rantai
    try:
        for i in range(len(rantai[penular])):
            if rantai[penular][i] == tertular:
                check = True
            cek_penularan(tertular, rantai[penular][i])

        if check:
            print('YA')
        else:
            print('TIDAK')
    except:
        print(f"Maaf, nama {penular} tidak ada dalam rantai penyebaran.")


while(True):
    command = input("Masukkan perintah: ")

    if "RANTAI_PENYEBARAN " in command:
        command = command.split()
        rantai_penyebaran(command[1])
        if check2:
            print(f"-{command[1]}")
    elif "CEK_PENULARAN " in command:
        command = command.split()
        cek_penularan(command[1], command[2])

    elif command == 'EXIT':
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        break
    else:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
