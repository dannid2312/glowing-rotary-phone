# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan lebih dari 1.000 karyawan yang tersebar di berbagai wilayah di Indonesia. Seiring pertumbuhan perusahaan yang pesat, tantangan dalam pengelolaan sumber daya manusia menjadi semakin kompleks. Salah satu tantangan utama yang dihadapi adalah tingginya attrition rate — rasio jumlah karyawan yang keluar terhadap total karyawan — yang tercatat mencapai lebih dari 10%.

Tingginya attrition rate ini tidak hanya berdampak pada stabilitas operasional, tetapi juga meningkatkan biaya rekrutmen dan pelatihan, serta menghambat upaya perusahaan dalam mempertahankan pengetahuan dan pengalaman karyawan.

Manajemen perusahaan menyadari pentingnya memahami faktor-faktor yang mendorong karyawan untuk meninggalkan perusahaan dan mencari solusi berbasis data untuk mengurangi angka attrition, memperbaiki kebijakan internal, dan menciptakan lingkungan kerja yang lebih baik.

### Permasalahan Bisnis

Permasalahan bisnis yang diidentifikasi dalam proyek ini meliputi:
- Faktor-faktor apa saja yang berkontribusi terhadap tingginya tingkat attrition di Jaya Jaya Maju?
- Bagaimana perusahaan dapat mengembangkan strategi berbasis data untuk menurunkan attrition rate secara signifikan?

### Cakupan Proyek

Dalam proyek ini, ruang lingkup pekerjaan yang akan dilakukan meliputi:
1. Eksplorasi dan Pemahaman Data
   Menganalisis data karyawan yang tersedia, termasuk informasi terkait demografi, gaji, lama kerja, performa, promosi, pelatihan, dan faktor lainnya.
2. Identifikasi Faktor Penyebab Attrition
   Menggunakan analisis statistik dan eksplorasi data untuk mengidentifikasi variabel-variabel yang paling berpengaruh terhadap keputusan karyawan untuk keluar.
3. Pembangunan Model Prediktif
   Membuat model machine learning (logistic regression) untuk memprediksi kemungkinan seorang karyawan mengundurkan diri.
   Mengevaluasi kinerja model menggunakan metrik yang sesuai (accuracy, precision, recall, f1-score).
4. Segmentasi Karyawan
   Melakukan segmentasi (clustering) untuk menemukan pola kelompok karyawan yang memiliki risiko tinggi terhadap attrition.
5. Penyusunan Rekomendasi Strategis
   Memberikan rekomendasi berbasis temuan analisis untuk membantu HR dan manajemen menurunkan attrition rate, misalnya melalui program retensi, pengembangan karier, atau penyesuaian kompensasi.
6. Visualisasi dan Penyampaian Hasil
   Menyusun dashboard atau laporan visual untuk memudahkan stakeholder memahami faktor-faktor kritis dan memantau perkembangan attrition ke depannya.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```
pip install matplotlib seaborn pandas numpy joblib sklearn
```

Berdasarkan employee_data.csv yang diperoleh, terdapat missing values pada kolom Attrition.

![Data Description](https://github.com/user-attachments/assets/df62e146-2560-42dc-9f3b-a3b08d9ce9dc)

#### Exploratory Data Analysis (EDA)

Berdasarkan hasil EDA terhadap kolom numerik, diperoleh informasi bahwa EmployeeId memiliki nilai yang seluruhnya unique, sedangkan nilai EmployeeCount dan StandardHours hanya memiliki 1 nilai. Oleh sebab itu, ketiga kolom tersebut akan dihapus dan tidak akan digunakan untuk analisis ke depannya. 

![EDA-Numerical](https://github.com/user-attachments/assets/8fd19ff1-abf1-49e2-a304-5103ac424cb7)

Dari histogram diatas, dapat diperoleh informasi juga bahwa umur dan tingkat pendidikan pegawai memiliki distribusi normal sehingga merepresentasikan sebaran pegawai dari berbagai generasi. Sebagian besar data lainnya memiliki distribusi dengan right skewness dimana sebagian besar nilai terdapat di sebelah kiri, seperti DistanceFromHome, JobLevel, MonthlyIncome, PercentSalaryHike, dan durasi tahun bekerja. Dapat disimpulkan bahwa sebagai besar pegawai merupakan pegawai berpangkat rendah dengan income yg rendah juga, dan mereka tinggal dekat dari kantor yang belum lama di kantor.

![EDA-Categorical](https://github.com/user-attachments/assets/8e14300b-ba10-499a-82fd-15e18208d516)

Dari grafik diatas, dapat diperoleh bahwa seluruh pegawai sudah masuk usia kerja yaitu lebih dari 18 tahun. Lebih dari setengah pegawai merupakan pegawai pria, dimana sebagian besar pegawai sudah menikah. Lebih dari setengah pegawai bekerja di bagian Research & Development dengan latar belakang mayoritas adalah Life Sciences kemudian diikuti oleh Medical. Lebih dari 25% pegawai bekerja OverTime dan sebagian besar pegawai jarang bepergian dinas.

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
