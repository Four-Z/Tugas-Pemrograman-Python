from msvcrt import getch
input_file = input("Masukkan nama file input: ")
output = input("Masukkan nama file output: ")

try:
    with open(input_file) as input_text:
        lines = input_text.read()

    input_text.close()

    if(lines != ""):
        x = lines.split("\n")

        mention = 0
        hastag = 0
        url = 0

        output_file = open(output, 'w')
        for i in x:
            temp = i.split()
            for j in temp:
                if(j.startswith("@")):
                    output_file.write("(M) ")
                    mention += 1
                elif(j.startswith("#")):
                    output_file.write("(H) ")
                    hastag += 1
                elif(j.startswith("www.")):
                    output_file.write("(U) ")
                    url += 1
                else:
                    temp = j+" "
                    output_file.write(temp)
            output_file.write("\n ")

        total = f"""
###############
Mention :     {mention}
Hashtag :     {hastag}
Url     :     {url}
        """

        output_file.write(total)
        output_file.close()
        print(f"Output berhasil ditulis pada {output}")
        print("Program selesai. Tekan enter untuk keluar...")
        # Assign to a variable just to suppress output. Blocks until key press.
        junk = getch()

    else:
        print("File input ada tapi kosong :(")

except:
    print("File input tidak ditemukan :(’")
