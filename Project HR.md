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
   Membuat model machine learning (Logistic Regression) untuk memprediksi kemungkinan seorang karyawan mengundurkan diri.
   Mengevaluasi kinerja model menggunakan metrik yang sesuai (accuracy, precision, recall, f1-score).
4. Penyusunan Rekomendasi Strategis
   Memberikan rekomendasi berbasis temuan analisis untuk membantu HR dan manajemen menurunkan attrition rate, misalnya melalui program retensi, pengembangan karier, atau penyesuaian kompensasi.
5. Visualisasi dan Penyampaian Hasil
   Menyusun dashboard atau laporan visual untuk memudahkan stakeholder memahami faktor-faktor kritis dan memantau perkembangan attrition ke depannya.

### Data Understanding

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```
pip install matplotlib seaborn pandas numpy joblib sklearn
```

Berdasarkan employee_data.csv yang diperoleh, terdapat missing values pada kolom Attrition.

| No | Column                     | Non-Null Count | Dtype   |
|----|----------------------------|----------------|---------|
| 1  | EmployeeId                 | 1470           | int64   |
| 2  | Age                        | 1470           | int64   |
| 3  | Attrition                  | 1058           | float64 |
| 4  | BusinessTravel             | 1470           | object  |
| 5  | DailyRate                  | 1470           | int64   |
| 6  | Department                 | 1470           | object  |
| 7  | DistanceFromHome           | 1470           | int64   |
| 8  | Education                  | 1470           | int64   |
| 9  | EducationField             | 1470           | object  |
| 10 | EmployeeCount              | 1470           | int64   |
| 11 | EnvironmentSatisfaction    | 1470           | int64   |
| 12 | Gender                     | 1470           | object  |
| 13 | HourlyRate                 | 1470           | int64   |
| 14 | JobInvolvement             | 1470           | int64   |
| 15 | JobLevel                   | 1470           | int64   |
| 16 | JobRole                    | 1470           | object  |
| 17 | JobSatisfaction            | 1470           | int64   |
| 18 | MaritalStatus              | 1470           | object  |
| 19 | MonthlyIncome              | 1470           | int64   |
| 20 | MonthlyRate                | 1470           | int64   |
| 21 | NumCompaniesWorked         | 1470           | int64   |
| 22 | Over18                     | 1470           | object  |
| 23 | OverTime                   | 1470           | object  |
| 24 | PercentSalaryHike          | 1470           | int64   |
| 25 | PerformanceRating          | 1470           | int64   |
| 26 | RelationshipSatisfaction   | 1470           | int64   |
| 27 | StandardHours              | 1470           | int64   |
| 28 | StockOptionLevel           | 1470           | int64   |
| 29 | TotalWorkingYears          | 1470           | int64   |
| 30 | TrainingTimesLastYear      | 1470           | int64   |
| 31 | WorkLifeBalance            | 1470           | int64   |
| 32 | YearsAtCompany             | 1470           | int64   |
| 33 | YearsInCurrentRole         | 1470           | int64   |
| 34 | YearsSinceLastPromotion    | 1470           | int64   |
| 35 | YearsWithCurrManager       | 1470           | int64   |


#### Exploratory Data Analysis (EDA)

Berdasarkan hasil EDA terhadap kolom numerik, diperoleh informasi bahwa EmployeeId memiliki nilai yang seluruhnya unique, sedangkan nilai EmployeeCount dan StandardHours hanya memiliki 1 nilai. Oleh sebab itu, ketiga kolom tersebut akan dihapus dan tidak akan digunakan untuk analisis ke depannya. 

![EDA-Numerical](https://github.com/user-attachments/assets/8fd19ff1-abf1-49e2-a304-5103ac424cb7)

Dari histogram diatas, dapat diperoleh informasi juga bahwa umur dan tingkat pendidikan pegawai memiliki distribusi normal sehingga merepresentasikan sebaran pegawai dari berbagai generasi. Sebagian besar data lainnya memiliki distribusi dengan right skewness dimana sebagian besar nilai terdapat di sebelah kiri, seperti DistanceFromHome, JobLevel, MonthlyIncome, PercentSalaryHike, dan durasi tahun bekerja. Dapat disimpulkan bahwa sebagai besar pegawai merupakan pegawai berpangkat rendah dengan income yg rendah juga, dan mereka tinggal dekat dari kantor yang belum lama di kantor.

![EDA-Categorical](https://github.com/user-attachments/assets/8e14300b-ba10-499a-82fd-15e18208d516)

Dari grafik diatas, dapat diperoleh bahwa seluruh pegawai sudah masuk usia kerja yaitu lebih dari 18 tahun. Lebih dari setengah pegawai merupakan pegawai pria, dimana sebagian besar pegawai sudah menikah. Lebih dari setengah pegawai bekerja di bagian Research & Development dengan latar belakang mayoritas adalah Life Sciences kemudian diikuti oleh Medical. Lebih dari 25% pegawai bekerja OverTime dan sebagian besar pegawai jarang bepergian dinas.

### Data Preparation

Berdasarkan tahapan data understanding, didapatkan informasi bahwa hanya kolom Attrition yang memiliki nilai kosong sehingga nilai kosong tersebut dapat diganti nilai 0. Kemudian EmployeeId seluruhnya unique, sedangkan EmployeeCount, Over18, dan StandardHours hanya memiliki 1 nilai, sehingga keempat kolom tersebut tidak digunakan untuk analisis lebih lanjut.

```
df['Attrition'] = df['Attrition'].fillna(0)
df.drop(columns=['EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours'], inplace=True)
```

Setelah itu dilakukan pembagian data, yaitu 70% untuk data train yang digunakan untuk melakukan pemodelan prediksi dan 30% untuk data test yang digunakan untuk mengukur tingkat akurasi model. Dari data test tersebut, diambil sebagian kecil data sebesar 10% dari data test untuk digunakan sebagai contoh deployment dari model machine learning yang dibuat.

```
target = 'Attrition'
X = df.drop(columns=target)
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_test, X_dep, y_test, y_dep = train_test_split(X_test, y_test, test_size=0.1, random_state=42, stratify=y_test)
```

### Modelling

Pemodelan dilakukan menggunakan logistic regression untuk mengukur parameter mana saja yang memberikan pengaruh kepada nilai attrition.
Selain itu juga digunakan fungsi ColumnTransformer sebagai preprocessor untuk memudahkan konversi kolom sehingga lebih mudah ketika melakukan deployment. Berikut ini hasil evaluasi dari model machine learning dibuat:

Classification Report:
| Class            | Precision | Recall | F1-Score | Support |
| ---------------- | --------- | ------ | -------- | ------- |
| 0.0              | 0.95      | 0.77   | 0.85     | 348     |
| 1.0              | 0.29      | 0.69   | 0.41     | 48      |
| **Accuracy**     |           |        | **0.76** | 396     |
| **Macro avg**    | 0.62      | 0.73   | 0.63     | 396     |
| **Weighted avg** | 0.87      | 0.76   | 0.79     | 396     |

Confusion Matrix:
|              | Predicted 0 | Predicted 1 |
| ------------ | ----------- | ----------- |
| **Actual 0** | 267         | 81          |
| **Actual 1** | 15          | 33          |

Model Logistic Regression menunjukkan performa yang cukup baik dalam mendeteksi kasus attrition. Dengan recall sebesar 0.69 pada kelas 1.0 (Attrition), model ini mampu mengenali sebagian besar karyawan yang berisiko keluar dari perusahaan. Meskipun precision-nya pada kelas ini masih rendah (0.29), nilai recall yang tinggi menunjukkan bahwa model sensitif terhadap kasus-kasus attrition, yang penting dalam konteks prediksi dini. Secara keseluruhan, model ini mencapai akurasi sebesar 76% dan f1-score sebesar 0.79 (weighted), yang mencerminkan keseimbangan performa dalam memprediksi kedua kelas. Dengan demikian, Logistic Regression dinilai sesuai untuk tujuan analisis ini karena mampu memberikan deteksi awal yang cukup andal terhadap potensi attrition di tempat kerja.

### Evaluation

Grafik berikut menampilkan 30 fitur paling berpengaruh terhadap kemungkinan seseorang mengundurkan diri (attrition) dari pekerjaannya berdasarkan model Logistic Regression. Sumbu horizontal menunjukkan koefisien dari masing-masing fitur, yang mencerminkan arah dan kekuatan pengaruhnya terhadap kemungkinan attrition. Fitur-fitur dengan koefisien positif (ditandai dengan warna merah) meningkatkan kemungkinan attrition, sedangkan fitur-fitur dengan koefisien negatif (ditandai dengan warna hijau) menurunkan kemungkinan tersebut.

![Most Influential Features](https://github.com/user-attachments/assets/718bdb31-ba79-46a2-a9a7-89775d03c3e9)

Fitur yang paling meningkatkan kemungkinan attrition adalah JobLevel yang rendah, JobRole_Sales Representative, dan JobRole_Laboratory Technician, menunjukkan bahwa posisi dengan level jabatan lebih rendah atau peran tertentu lebih rentan terhadap pengunduran diri. Begitu pula dengan variabel OverTime_Yes, BusinessTravel_Travel_Frequently, dan YearsAtCompany yang lebih rendah juga berkorelasi dengan meningkatnya attrition.

Sebaliknya, fitur yang paling menurunkan kemungkinan attrition adalah MonthlyIncome yang tinggi, OverTime_No, dan BusinessTravel_Non-Travel. Artinya, karyawan dengan gaji lebih tinggi, tidak bekerja lembur, dan jarang bepergian untuk urusan bisnis cenderung lebih bertahan di perusahaan. Selain itu, pengalaman kerja yang lebih banyak, kepuasan terhadap lingkungan kerja (EnvironmentSatisfaction), serta masa kerja yang lebih lama di peran saat ini (YearsInCurrentRole) juga berkontribusi terhadap menurunnya risiko pengunduran diri.

Fitur-fitur seperti JobSatisfaction, JobInvolvement, dan YearsWithCurrManager juga memiliki pengaruh negatif terhadap attrition, yang menegaskan pentingnya keterlibatan dan kepuasan kerja serta hubungan dengan atasan dalam mempertahankan karyawan. Secara keseluruhan, grafik ini menyoroti bahwa faktor jabatan, penghasilan, jenis pekerjaan, pengalaman kerja, dan kondisi kerja memainkan peran penting dalam memengaruhi keputusan karyawan untuk tetap atau meninggalkan pekerjaannya.

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Proyek ini berhasil melaksanakan seluruh ruang lingkup yang direncanakan, mulai dari eksplorasi data hingga penyusunan rekomendasi strategis. Data karyawan yang dianalisis mencakup berbagai aspek seperti demografi, jabatan, penghasilan, masa kerja, promosi, pelatihan, dan kepuasan kerja. Tujuan utamanya adalah memahami faktor-faktor utama yang mendorong keputusan karyawan untuk mengundurkan diri dari perusahaan.

Melalui analisis statistik dan eksploratif, ditemukan bahwa faktor-faktor seperti level jabatan yang rendah, jenis pekerjaan tertentu (seperti Sales Representative dan Laboratory Technician), frekuensi lembur yang tinggi, serta tingkat pendapatan yang rendah merupakan penyebab utama besarnya attrition. Model prediktif berbasis logistic regression dikembangkan untuk memperkirakan kemungkinan seorang karyawan mengundurkan diri, dan menunjukkan performa yang baik berdasarkan metrik seperti akurasi, precision, recall, dan f1-score.

Hasil analisis ini kemudian digunakan sebagai dasar penyusunan rekomendasi strategis yang ditujukan untuk tim HR dan manajemen. Rekomendasi meliputi peningkatan struktur kompensasi, pengelolaan lembur, perbaikan jalur karier, serta peningkatan keterlibatan dan kepuasan kerja karyawan. Seluruh hasil proyek telah divisualisasikan dalam format yang mendukung pemahaman dan pengambilan keputusan oleh para pemangku kepentingan.

### Rekomendasi Action Items

Berdasarkan temuan tersebut, berikut adalah ringkasan strategi yang disarankan untuk menurunkan tingkat attrition dan meningkatkan retensi talenta:

1. Optimalisasi Kompensasi dan Insentif
Perusahaan perlu melakukan peninjauan ulang terhadap struktur gaji dan insentif terutama bagi jabatan berisiko tinggi seperti Sales Representative dan Laboratory Technician. Penyesuaian kompensasi yang kompetitif akan berdampak langsung terhadap peningkatan loyalitas karyawan.

2. Manajemen Lembur yang Lebih Seimbang
Lembur berlebihan berkontribusi signifikan terhadap meningkatnya attrition. Perusahaan disarankan menetapkan batasan lembur yang jelas dan memastikan kompensasi yang setara, guna menjaga kesehatan kerja dan motivasi karyawan.

3. Pengurangan Beban Perjalanan Dinas
Tingginya frekuensi perjalanan bisnis juga meningkatkan potensi attrition. Strategi efisiensi perjalanan melalui digitalisasi pertemuan dan evaluasi urgensi perjalanan perlu diterapkan untuk menciptakan keseimbangan kerja yang lebih baik.

4. Percepatan Mobilitas Karier
Waktu yang lama sejak promosi terakhir menjadi indikator risiko pengunduran diri. Perusahaan harus menyediakan jalur karier yang jelas dan memperluas akses promosi untuk menjaga semangat dan aspirasi karyawan.

5. Penguatan Faktor Kepuasan dan Keterlibatan Karyawan
Faktor non-finansial seperti kepuasan terhadap lingkungan kerja, hubungan dengan atasan, serta keterlibatan dalam pekerjaan memiliki dampak signifikan dalam menurunkan attrition. Investasi pada aspek ini penting sebagai bagian dari strategi retensi jangka panjang.

6. Retensi Talenta Berpengalaman
Karyawan dengan masa kerja panjang dan pengalaman tinggi cenderung lebih loyal, namun tetap berisiko keluar jika tidak diberi perhatian. Pemberian proyek strategis, fleksibilitas kerja, dan program penghargaan jangka panjang direkomendasikan untuk mempertahankan kelompok ini.

7. Penyesuaian Proses Rekrutmen dan Penempatan
Posisi tertentu memiliki kecenderungan attrition yang lebih tinggi. Oleh karena itu, proses rekrutmen perlu diarahkan untuk menemukan kecocokan yang lebih baik dengan kebutuhan dan karakteristik jabatan, serta memperkuat program onboarding.

Dengan implementasi strategi-strategi tersebut, perusahaan diharapkan dapat menurunkan tingkat attrition secara signifikan, menjaga stabilitas organisasi, serta meningkatkan efisiensi dan produktivitas sumber daya manusia.
