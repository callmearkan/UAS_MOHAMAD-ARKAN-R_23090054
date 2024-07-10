import pandas as pd

# Data dalam bentuk array 2 dimensi
data = {
    'Nama': ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'],
    'Algoritma dan Struktur Data 2': [50, 90, None],
    'Matematika Numerik': [80, 65, 60],
}

df = pd.DataFrame(data)

df.fillna(value=pd.NA, inplace=True)

print("Data Nilai Mahasiswa:")
print(df)

print("\nRata-rata nilai untuk setiap mata kuliah:")
rata_rata_mk = df.mean(numeric_only=True)
print(rata_rata_mk)

print("\nRata-rata nilai untuk setiap mahasiswa:")
rata_rata_mhs = df.set_index('Nama').mean(axis=1, numeric_only=True)
print(rata_rata_mhs)