ph = float(input("Masukkan nilai pH (0 - 14): "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")
