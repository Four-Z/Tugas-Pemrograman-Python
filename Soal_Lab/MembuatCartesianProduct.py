
himpunan_A = input("Masukkan input himpunan A: ").split(",")
himpunan_B = input("Masukkan input himpunan B: ").split(",")

print("A x B = {", end=" ")
for i in himpunan_A:
    for j in himpunan_B:
        print(f"({i},{j})", end=" ")
print("}")
