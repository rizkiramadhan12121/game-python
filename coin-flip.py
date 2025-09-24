import random

heads_count = 0

for i in range(5):
    flip = random.choice(["Heads", "Tails"])
    print("Lemparan ke-", i+1, ":", flip)
    if flip == "Heads":
        heads_count += 1

print("\nJumlah 'Heads' yang muncul:", heads_count)
