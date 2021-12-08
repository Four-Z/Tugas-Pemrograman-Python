import time

start = time.time()
inputfile = "WhatsMood/input.txt"
try:
    with open(inputfile) as text:
        text = text.read()

except FileNotFoundError:
    print("File input tidak ada :(.")
    exit()

if text == "":
    print("File input ada tapi kosong :(")
    exit()

text_temp = text.split("\n")

text_chanek = []
for i in text_temp:
    if "Pak Chanek:" in i:
        text_chanek.append(i)

happiness = 50
sadness = 50
angry = 50


def operasiHapiness(text_chanek):
    global happiness
    global sadness
    count = 0
    for i in text_chanek:
        i = i.split()
        for j in i:
            if j == "(smile)":
                count += 1
    happiness += 9*count
    sadness -= 6*count


def operasiSadness(text_chanek):
    global sadness
    global angry
    count = 0
    for i in text_chanek:
        i = i.split()
        for j in i:
            if j == "(sad)":
                count += 1
    sadness += 10*count
    angry -= 8*count


def operasiAngry(text_chanek):
    global angry
    global happiness
    count = 0
    for i in text_chanek:
        i = i.split()
        for j in i:
            if j == "(angry)":
                count += 1
    angry += 13*count
    happiness -= 5*count


def checkMood(mood):
    if (mood > 100):
        mood = 100
    elif (mood < 0):
        mood = 0
    return mood


operasiHapiness(text_chanek)
operasiSadness(text_chanek)
operasiAngry(text_chanek)

if "(smile)" in text:
    text = text.replace("(smile)", "\U0001f603")
if "(sad)" in text:
    text = text.replace("(sad)", "\U0001f622")
if '(angry)' in text:
    text = text.replace("(angry)", " \U0001f621")

print(text)

if happiness > (sadness & angry):
    perasaan = "bahagia"
elif sadness > (happiness & angry):
    perasaan = "sedih"
elif angry > (happiness & sadness):
    perasaan = "marah"
elif (sadness & angry) > happiness:
    perasaan = "sedih atau marah"
elif (happiness & angry) > sadness:
    perasaan = "senang atau marah"
elif (happiness & sadness) > angry:
    perasaan = "senang atau sedih"
else:
    perasaan = "kesimpulan tidak ditemukan"

print(f"""
Mengukur suasana hati....

##### Hasil Pengukuran #####
Happienss = {checkMood(happiness)} | Sadness = {checkMood(sadness)} | Anger = {checkMood(angry)}

##### Kesimpulan #####
Pak Chanek sedang {perasaan}.""")
end = time.time()
print(f"Runtime of the program is {end - start}")
