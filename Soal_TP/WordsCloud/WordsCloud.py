import string
from msvcrt import getch
from html_functions import make_HTML_word, make_HTML_box, print_HTML_file

print("""Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.


""")
# input_file = input("Silakan masukan nama file: ")
input_file = "CommencementSpeechByGates2014.txt"
print("""56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan
(jumlah:kata)
""")


# from txt to string
with open(input_file) as input_text:
    lines = input_text.read()

# split string
lines = lines.lower()
x = lines.split()

# delete punctuation
clear_words = []
for words in x:
    for char in words:
        if char in string.punctuation:
            words = words.replace(char, "")

    clear_words.append(words)

# input stopwords.txt
with open("stopwords.txt") as input_text:
    stopWords = input_text.read()

stopWords = stopWords.split()

# delete words in stopwords
temp = []
for words in clear_words:
    if words not in stopWords:
        temp.append(words)

# delete duplicate element
final_clear = list(set(temp))

# count how many element occurs
count_list = []
for i in final_clear:
    count = temp.count(i)
    count_list.append([count, i])

# sort by highest
count_list.sort(reverse=True)

highest = count_list[0][0]
lowest = count_list[55][0]

# print to console
i = 0
while (i < 56):
    for j in range(4):
        print(f"{count_list[i][1]}:{count_list[i][0]}           ", end="\t")
        i += 1
    print("\n")


count_list = sorted(count_list[:56], key=lambda l: l[1], reverse=False)
# write to html
body = ''
for cnt, word in count_list[:56]:
    body = body + " " + make_HTML_word(word, cnt, highest, lowest)
    box = make_HTML_box(body)
    print_HTML_file(box, 'testFile')


print("Tekan Enter untuk keluar ...")
# Assign to a variable just to suppress output. Blocks until key press.
junk = getch()
