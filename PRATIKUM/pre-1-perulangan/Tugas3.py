jumlah = int(input("Masukkan jumlah deret Fibonacci: "))
a, b = 0, 1

for i in range(jumlah):
    print(f"i ke-{i+1} -> {a}")
    a, b = b, a + b
