#%%
# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Membaca data dari CSV
# Data BPR per Lokasi
data = {
    "Lokasi": [
        "Jawa Barat", "Banten", "DKI Jakarta", "D.I Yogyakarta", "Jawa Tengah", "Jawa Timur",
        "Bengkulu", "Jambi", "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau",
        "Kepulauan Riau", "Sumatera Selatan", "Bangka Belitung", "Lampung",
        "Kalimantan Selatan", "Kalimantan Barat", "Kalimantan Timur", "Kalimantan Tengah",
        "Kalimantan Utara", "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Utara",
        "Sulawesi Tenggara", "Sulawesi Barat", "Gorontalo", "Nusa Tenggara Barat",
        "Bali", "Nusa Tenggara Timur", "Maluku", "Papua", "Maluku Utara", "Papua Barat", "Lainnya"
    ],
    "KP": [
        218, 52, 28, 46, 238, 241, 5, 18, 1, 45, 64, 27,
        44, 21, 3, 23, 14, 17, 14, 6, 2, 6, 18, 15,
        15, 2, 2, 19, 128, 11, 1, 7, 2, 3, 0
    ],
    "KC": [
        368, 69, 16, 52, 623, 279, 7, 8, 0, 56, 51, 12,
        31, 18, 4, 37, 23, 6, 13, 9, 1, 18, 16, 29,
        7, 1, 2, 58, 62, 10, 9, 18, 7, 4, 0
    ],
    "KPK": [
        307, 54, 4, 109, 863, 788, 1, 4, 10, 46, 72, 22,
        8, 8, 5, 17, 11, 8, 29, 9, 8, 21, 8, 19,
        2, 0, 1, 35, 102, 10, 11, 4, 3, 0, 0
    ]
}

df = pd.DataFrame(data)
df['Total'] = df['KP'] + df['KC'] + df['KPK']
# %%
# Pengolahan Data
# Menghitung persentase kontribusi
df['Persentase KP (%)'] = (df['KP'] / df['Total']) * 100
df['Persentase KC (%)'] = (df['KC'] / df['Total']) * 100
df['Persentase KPK (%)'] = (df['KPK'] / df['Total']) * 100

# Menampilkan data
print(df[['Lokasi', 'Total', 'Persentase KP (%)', 'Persentase KC (%)', 'Persentase KPK (%)']])
# %%
# Visualisasi Persentase Kontribusi BPR berdasarkan Lokasi
plt.figure(figsize=(14, 10))
bar_width = 0.25
index = range(len(df))

# Bar untuk KP
plt.bar(index, df['Persentase KP (%)'], bar_width, label='KP', color='b')
# Bar untuk KC
plt.bar([i + bar_width for i in index], df['Persentase KC (%)'], bar_width, label='KC', color='g')
# Bar untuk KPK
plt.bar([i + 2 * bar_width for i in index], df['Persentase KPK (%)'], bar_width, label='KPK', color='r')

plt.xlabel('Lokasi')
plt.ylabel('Persentase (%)')
plt.title('Persentase Kontribusi Jenis BPR Berdasarkan Lokasi - Desember 2024')
plt.xticks([i + bar_width for i in index], df['Lokasi'], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
# %%
# Rekomendasi berdasarkan analisis
high_kp = df[df['Persentase KP (%)'] > 50]  # Lokasi dengan kontribusi KP tinggi
low_kp = df[df['Persentase KP (%)'] < 10]   # Lokasi dengan kontribusi KP rendah

print("Rekomendasi untuk Lokasi dengan Kontribusi KP Tinggi:")
for index, row in high_kp.iterrows():
    print(f"- Pertahankan dan tingkatkan layanan di {row['Lokasi']} untuk mempertahankan kontribusi KP yang tinggi.")

print("\nRekomendasi untuk Lokasi dengan Kontribusi KP Rendah:")
for index, row in low_kp.iterrows():
    print(f"- Lakukan analisis lebih lanjut di {row['Lokasi']} untuk memahami faktor penyebab rendahnya kontribusi KP.")
# %%
# Kesimpulan
# - Data menunjukkan bahwa Jawa Tengah memiliki kontribusi KP tertinggi, diikuti oleh Jawa Timur dan DKI Jakarta.
# - Sebaliknya, beberapa provinsi seperti Papua Barat dan Maluku Utara memiliki kontribusi KP yang rendah.
# - Rekomendasi untuk fokus pada provinsi dengan kontribusi KP tinggi untuk meningkatkan produk dan pemasaran.
# - Untuk provinsi dengan kontribusi KP rendah, perlu dilakukan analisis lebih lanjut untuk memahami penyebabnya.
# %%