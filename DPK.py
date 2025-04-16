# %%
#Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Membaca data dari CSV
data = {
    "Lokasi": ["Jawa Barat", "Banten", "DKI Jakarta", "D.I Yogyakarta", "Jawa Tengah", "Jawa Timur", 
               "Bengkulu", "Jambi", "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", 
               "Kepulauan Riau", "Sumatera Selatan", "Bangka Belitung", "Lampung", 
               "Kalimantan Selatan", "Kalimantan Barat", "Kalimantan Timur", "Kalimantan Tengah", 
               "Kalimantan Utara", "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Utara", 
               "Sulawesi Tenggara", "Sulawesi Barat", "Gorontalo", "Nusa Tenggara Barat", 
               "Bali", "Nusa Tenggara Timur", "Maluku", "Papua", "Maluku Utara", 
               "Papua Barat", "Lainnya"],
    "Tabungan": [5256, 813, 337, 2465, 17360, 4665, 51, 153, 18, 917, 902, 619, 1264, 
                 320, 38, 1317, 253, 390, 143, 385, 56, 133, 352, 363, 156, 93, 13, 
                 880, 4525, 258, 176, 223, 30, 36, 0],
    "Deposito": [11546, 4253, 4286, 4662, 19933, 11522, 74, 791, 11, 1078, 671, 793, 
                 7983, 1162, 114, 6227, 856, 956, 205, 1037, 44, 941, 2048, 1351, 
                 119, 24, 23, 695, 12379, 407, 1479, 636, 84, 103, 0],
}

df = pd.DataFrame(data)
df['Total DPK'] = df['Tabungan'] + df['Deposito']
df['Pangsa (%)'] = (df['Total DPK'] / df['Total DPK'].sum()) * 100
# %%
## Analisis Data

# Menampilkan data
print(df)

# Menampilkan statistik deskriptif
print(df.describe())
# %%
# Visualisasi Total DPK berdasarkan Lokasi
plt.figure(figsize=(12, 8))
sns.barplot(x='Total DPK', y='Lokasi', data=df.sort_values('Total DPK', ascending=False), palette='viridis')
plt.title('Total DPK Berdasarkan Lokasi Penghimpunan - Desember 2024')
plt.xlabel('Total DPK (Miliar Rupiah)')
plt.ylabel('Lokasi')
plt.show()

# Visualisasi Pangsa DPK
plt.figure(figsize=(10, 10))
plt.pie(df['Pangsa (%)'], labels=df['Lokasi'], autopct='%1.1f%%', startangle=140)
plt.title('Pangsa DPK Berdasarkan Lokasi Penghimpunan - Desember 2024')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
# %%
# Rekomendasi berdasarkan analisis
high_dpk = df[df['Total DPK'] > 10000]  # Provinsi dengan DPK tinggi
low_dpk = df[df['Total DPK'] < 500]     # Provinsi dengan DPK rendah

print("Rekomendasi untuk Provinsi dengan DPK Tinggi:")
for index, row in high_dpk.iterrows():
    print(f"- Fokus pada {row['Lokasi']} untuk meningkatkan produk dan pemasaran.")

print("\nRekomendasi untuk Provinsi dengan DPK Rendah:")
for index, row in low_dpk.iterrows():
    print(f"- Lakukan analisis lebih lanjut di {row['Lokasi']} untuk memahami faktor penyebab rendahnya DPK.")
# %%
# Kesimpulan
# - Data menunjukkan bahwa Jawa Tengah memiliki total DPK tertinggi, diikuti oleh Jawa Barat dan DKI Jakarta.
# - Sebaliknya, beberapa provinsi seperti Maluku Utara dan Papua Barat memiliki total DPK yang rendah.
# - Rekomendasi untuk fokus pada provinsi dengan DPK tinggi untuk meningkatkan produk dan pemasaran.
# - Untuk provinsi dengan DPK rendah, perlu dilakukan analisis lebih lanjut untuk memahami penyebabnya.

# %%
