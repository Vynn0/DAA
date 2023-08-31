# 2. Fungsi untuk menukar posisi dua variabel x dan y, dengan kasus :
# Ada 2 buah: manggis dan pisang. Manggis di piring 1, Pisang di piring 2. Piring 3 kosong.

"""
Algoritma

Definisikan tukar_posisi(x,y)
Deklarasikan piring dengan buah nya yang sudah ditentukan
Cetak piring sebelum pertukaran

Tukar posisi piring 1 dan 2 mengunnakan fungsi tukar_posisi(x,y)
Cetak piring sesudah pertukaran
"""

"""
Pseudocode

DEFINISIKAN TUKAR_POSISI(x,y) sebagai:
  temp = x
  x = y
  y = temp
  return x,y

DEKLARASIKAN
manggis = "piring 1"
pisang = "piring 2"

CETAK PIRING SEBELUM PERTUKARAN
print("Sebelum pertukaran:")
print("Manggis:", manggis)
print("Pisang:", pisang)

tukar_posisi manggis dengan pisang

CETAK PIRING SETELAH PERTUKARAN
print("\nSetelah pertukaran:")
print("Manggis:", manggis)
print("Pisang:", pisang)
"""

def tukar_posisi(x, y):
    temp = x
    x = y
    y = temp
    return x, y

manggis = "piring 1"
pisang = "piring 2"

print("Sebelum pertukaran:")
print("Manggis:", manggis)
print("Pisang:", pisang)

manggis, pisang = tukar_posisi(manggis, pisang)

print("\nSetelah pertukaran:")
print("Manggis:", manggis)
print("Pisang:", pisang)
