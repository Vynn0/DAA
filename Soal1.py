"""
Algoritma

1. Tentukan bilangan pertama (a) dan bilangan kedua (b) yang akan dicari kelipatannya.
2. Cetak "Kelipatan a:" diikuti oleh daftar kelipatan a dari a hingga 12.
3. Cetak "Kelipatan b:" diikuti oleh daftar kelipatan b dari b hingga 12.
4. Untuk mencari KPK, lakukan loop dari nilai maksimum antara a dan b hingga a * b + 1. Jika ditemukan angka yang habis dibagi oleh a dan b, maka itu adalah KPK.
5. Cetak hasil KPK.
"""

"""
MULAI
INPUT NILAI A dan B
CETAK "Kelipatan", a, ":"
UNTUK i DARI a HINGGA 12 LANGKAH a:
CETAK i
    
CETAK UNTUK PINDAH BARIS
    
CETAK "Kelipatan", b, ":"
UNTUK i DARI b HINGGA 12 LANGKAH b:
CETAK i
    
CETAK UNTUK PINDAH BARIS
    
kpk = NONE

UNTUK i DARI MAKS(a, b) HINGGA a * b + 1
JIKA i MOD a = 0 DAN i MOD b = 0
kpk = i
BERHENTI
    
CETAK UNTUK PINDAH BARIS
CETAK "KPK dari", a, "dan", b, "adalah", kpk

SELESAI
"""

a = 3
b = 4

print("Kelipatan", a, ":", end=" ")
for i in range(a, 13, a):
    print(i, end=" ")

print() 
print("Kelipatan", b, ":", end=" ")
for i in range(b, 13, b):
    print(i, end=" ")

print()
kpk = None
for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        kpk = i
        break

print("\nKPK dari", a, "dan", b, "adalah", kpk)
