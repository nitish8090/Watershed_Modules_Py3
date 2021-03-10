n = 19

triplet_list = [(i * 3 - 2, i * 3 - 1, i * 3) for i in range(1, int(n / 3) + 1)]
print(triplet_list)

triplet_list = [[i*3+p for p in range(-2, 1)] for i in range(1, int(n / 3) + 1)]
print(triplet_list)

i = 3
alo = [p for p in range(-2, 1)]
print(alo)
