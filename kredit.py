#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# Data Kredit BPR per Lokasi
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
    "2018": [
        12554, 3393, 1571, 4724, 23620, 9836, 71, 687, 153, 1128, 1238, 939,
        5094, 1206, 94, 9111, 360, 630, 252, 436, 0, 2165, 2226, 977,
        226, 17, 24, 1056, 10431, 567, 1671, 1048, 115, 600, 0
    ],
    "2020": [
        13223, 3982, 2051, 5679, 28082, 10841, 74, 803, 135, 1205, 1355, 954,
        5152, 1457, 119, 10096, 425, 758, 241, 561, 39, 2288, 2268, 1329,
        229, 25, 53, 1194, 11522, 669, 1917, 1241, 200, 604, 0
    ],
    "2021": [
        13961, 4096, 2427, 5805, 29847, 11554, 79, 863, 57, 1406, 1369, 1028,
        5220, 1474, 109, 10322, 520, 977, 270, 826, 56, 2224, 2384, 1351,
        257, 79, 48, 1255, 11894, 672, 1974, 1354, 220, 602, 0
    ],
    "2022": [
        15834, 4918, 2995, 6146, 33363, 12774, 102, 969, 48, 1566, 1449, 1177,
        6219, 1621, 112, 10869, 599, 1123, 327, 1534, 66, 2212, 2537, 1536,
        300, 79, 53, 1405, 12274, 697, 2094, 1467, 244, 586, 0
    ],
    "2023": [
        16393, 5614, 3503, 6583, 34702, 15277, 141, 1081, 33, 1760, 1508, 1441,
        7458, 1904, 137, 11769, 1107, 1203, 409, 1830, 94, 2131, 2822, 1518,
        359, 90, 69, 1551, 12874, 747, 2224, 1646, 272, 539, 0
    ],
    "2024": [
        16446, 5652, 3428, 6584, 34674, 15332, 144, 1090, 34, 1758, 1505, 1455,
        7631, 1911, 139, 11821, 1203, 1183, 368, 1811, 93, 2132, 2836, 1529,
        360, 90, 73, 1572, 12885, 742, 2230, 1651, 274, 538, 0
    ]
}

df = pd.DataFrame(data)
# %%
# Menghitung total kredit per lokasi
df['Total Kredit'] = df[['2018', '2020', '2021', '2022', '2023', '2024']].sum(axis=1)

# Menampilkan data
print(df[['Lokasi', 'Total Kredit']])
# %%
# Visualisasi Total Kredit berdasarkan Lokasi
plt.figure(figsize=(12, 8))
sns.barplot(x='Total Kredit', y='Lokasi', data=df.sort_values('Total Kredit', ascending=False), palette='viridis')
plt.title('Total Kredit BPR Berdasarkan Lokasi (2018-2024)')
plt.xlabel('Total Kredit (Miliar Rp)')
plt.ylabel('Lokasi')
plt.show()
# %%
# Rekomendasi berdasarkan analisis
high_credit = df[df['Total Kredit'] > 20000]  # Lokasi dengan total kredit tinggi
low_credit = df[df['Total Kredit'] < 1000]    # Lokasi dengan total kredit rendah

print("Rekomendasi untuk Lokasi dengan Total Kredit Tinggi:")
for index, row in high_credit.iterrows():
    print(f"- Fokus pada {row['Lokasi']} untuk meningkatkan produk dan pemasaran.")

print("\nRekomendasi untuk Lokasi dengan Total Kredit Rendah:")
for index, row in low_credit.iterrows():
    print(f"- Lakukan analisis lebih lanjut di {row['Lokasi']} untuk memahami faktor penyebab rendahnya total kredit.")
# %%
# Kesimpulan
# - Data menunjukkan bahwa Jawa Tengah memiliki total kredit tertinggi, diikuti oleh Jawa Timur dan DKI Jakarta.
# - Sebaliknya, beberapa provinsi seperti Papua Barat dan Maluku Utara memiliki total kredit yang rendah.
# - Rekomendasi untuk fokus pada provinsi dengan total kredit tinggi untuk meningkatkan produk dan pemasaran.
# - Untuk provinsi dengan total kredit rendah, perlu dilakukan analisis lebih lanjut untuk memahami penyebabnya.
# %%