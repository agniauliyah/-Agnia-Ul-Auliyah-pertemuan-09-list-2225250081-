
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def analisis_kelulusan(nilai):
    lulus = []
    tidak_lulus = []

    for angka in nilai:
        if angka >= 60:
            lulus.append(angka)
        else:
            tidak_lulus.append(angka)

    return lulus, tidak_lulus


nilai_mahasiswa = [75, 55, 80, 60, 45, 90, 88, 70, 65, 50]

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Semua nilai: {nilai_mahasiswa}")
print(f"Banyak data: {len(nilai_mahasiswa)}")
print(f"Total nilai: {sum(nilai_mahasiswa)}")
print(f"Rata-rata: {hitung_rata_rata(nilai_mahasiswa):.2f}")
print(f"Nilai minimum: {min(nilai_mahasiswa)}")
print(f"Nilai maksimum: {max(nilai_mahasiswa)}")

lulus, tidak_lulus = analisis_kelulusan(nilai_mahasiswa)

print(f"Nilai lulus: {lulus}")
print(f"Jumlah lulus: {len(lulus)}")
print(f"Jumlah tidak lulus: {len(tidak_lulus)}")
print(f"Nilai tidak lulus: {tidak_lulus}")