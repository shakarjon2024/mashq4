
karta = input("16 xonali karta raqamini kiriting: ")

if len(karta) == 16:
    raqamlar = karta[0:4] + " " + karta[4:8] + " " + karta[8:12] + " " + karta[12:16]
    print('Raqamlarning  ko`rinishi:', raqamlar)

else:
    print("karta raqami 16 xonali bolishi kk.")
