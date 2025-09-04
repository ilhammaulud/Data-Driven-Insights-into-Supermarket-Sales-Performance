# Data-Driven Insights into Supermarket Sales Performance

## Repository Outline

```
1. README.md - Penjelasan gambaran umum project
2. P2M3_ilham_maulud_GX.ipynb - Notebook yang berisi data quality validation framework
3. P2M3_ilham_maulud_ddl.txt - Sekumpulan perintah SQL yang digunakan untuk mendefinisikan struktur database
4. P2M3_ilham_maulud_DAG_graph.jpg - Alur proses mengolah data
5. P2M3_ilham_maulud_conceptual.txt - Jawaban dari pertanyaan conceptual
6. P2M3_ilham_maulud_DAG.py - Workflow yang berisi sekumpulan task yang harus dijalankan secara berurutan
7. P2M3_ilham_maulud_data_raw.csv - Dataset asli
8. P2M3_ilham_maulud_data_clean.csv - Dataset yang sudah bersih
9. Folder image - Berisikan introduction, visualisasi dan kesimpulan
```

## Problem Background
Perkembangan ritel modern saat ini semakin kompetitif, termasuk di sektor supermarket. Banyak faktor yang memengaruhi performa penjualan, mulai dari lokasi cabang, jenis produk, preferensi pelanggan, hingga promosi yang dijalankan. Analisis data penjualan dapat membantu perusahaan memahami pola belanja konsumen, mengidentifikasi produk yang laris maupun kurang diminati, dan memaksimalkan strategi penjualan di masa depan.

Dataset “Supermarket Sales” berisi data transaksi penjualan dari beberapa cabang supermarket, termasuk informasi mengenai produk, kategori, kuantitas, harga, diskon, dan waktu transaksi. Dataset ini dapat dijadikan dasar untuk melakukan eksplorasi data dan analisis penjualan yang komprehensif.


## Project Output
Output dari project ini berupa:

1. Data Pipeline (Airflow DAG)

    - Alur otomatisasi untuk membaca data supermarket, membersihkan data, melakukan transformasi, serta menjalankan validasi menggunakan Great Expectations (GX).
    - Pipeline ini memastikan data yang digunakan sudah konsisten, valid, dan sesuai dengan standar bisnis.

2. Data Validation Report

    - Menggunakan Great Expectations untuk memverifikasi kualitas data.
    - Validasi dilakukan pada berbagai aspek, seperti nilai unik, rentang nilai (between), tipe data (in type list), dan distribusi statistik (mean/median).
    - Hasil validasi dapat digunakan sebagai acuan apakah data layak untuk dianalisis lebih lanjut.

3. Dashboard (Kibana)

    - Visualisasi data penjualan supermarket yang interaktif, meliputi distribusi produk, tren penjualan, segmentasi pelanggan, metode pembayaran, dan analisis cabang.
    - Dashboard ini memberikan insight bisnis yang mudah dipahami oleh tim marketing, sales, dan manajemen.

4. Business Insights & Recommendations

    - Narasi analisis dari hasil EDA dan dashboard.

    - Insight berfokus pada tren penjualan, perilaku konsumen, serta rekomendasi strategi penjualan dan promosi untuk meningkatkan profitabilitas.

## Data
Data yang digunakan dalam proyek ini berasal dari dataset publik Supermarket Sales Dataset yang tersedia di Kaggle. Dataset ini berisi catatan transaksi penjualan dari beberapa cabang supermarket di tiga kota besar.

Karakteristik Data:

1. Jumlah baris: 1.000 transaksi
2. Jumlah kolom: 17 kolom
3. Tidak terdapat missing values pada dataset.
4. Tipe data terdiri dari kategorikal dan numerik.

## Method
Proyek ini menggunakan pendekatan Exploratory Data Analysis (EDA) dan Data Validation untuk memahami pola penjualan di supermarket serta memastikan kualitas data yang digunakan.

Metode yang digunakan antara lain:

1. Data Cleaning & Preprocessing

    - Menghilangkan inkonsistensi data.
    - Memastikan tipe data sesuai.
    - Menambahkan kolom turunan seperti Total (hasil perhitungan Unit Price × Quantity + Tax).

2. Data Validation dengan Great Expectations (GX)

    - Menetapkan expectations untuk menjaga kualitas data, seperti:

        - Nilai unik pada Invoice ID.
        - Nilai Customer Type hanya boleh "Member" atau "Normal".
        - Nilai Total harus ≥ 0.
        - Kolom Quantity harus berupa integer.
        - Nilai rata-rata Rating berada di rentang 5–10.

    - Validasi ini dilakukan untuk memastikan dataset bersih dan layak dianalisis.

3. Exploratory Data Analysis (EDA)

    - Analisis distribusi data.
    - Analisis tren penjualan berdasarkan waktu.
    - Analisis perilaku pelanggan berdasarkan tipe dan metode pembayaran.
    - Visualisasi menggunakan Kibana Dashboard dengan berbagai jenis plot (bar chart, pie chart, line chart, dll).

4. Insight & Business Recommendation

    - Hasil EDA digunakan untuk memberikan insight penjualan.
    - Insight ini mendukung divisi Marketing, Sales, dan Manajemen dalam pengambilan keputusan.

## Stacks
Project ini menggunakan kombinasi bahasa pemrograman, tools, dan library Python untuk mendukung proses analisis dan validasi data:

1. Bahasa Pemrograman

    - Python 3.12

2. Library Python

    - Pandas → untuk manipulasi dan analisis data.
    - Great Expectations (GX) → untuk validasi dan menjaga kualitas data.
    - Numpy → untuk perhitungan numerik dasar.

3. Tools

    - Apache Airflow → untuk orkestrasi pipeline (ETL, data cleaning, validasi).
    - Kibana → untuk visualisasi data dan pembuatan dashboard interaktif.
    - Git & GitHub → untuk version control dan kolaborasi.

4. Environment

    - Virtual Environment (venv) untuk isolasi dependensi project.

## Reference
- Dataset: [Supermarket Sales Dataset](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- [Great Expectations](https://docs.greatexpectations.io)
- [Apache Airflow](https://airflow.apache.org/docs/)
- [Kibana](https://www.elastic.co/guide/en/kibana)
---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)