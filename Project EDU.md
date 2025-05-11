# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Permasalahan bisnis yang diidentifikasi dalam proyek ini meliputi:

1. **Faktor-faktor apa saja yang berkontribusi terhadap tingginya tingkat dropout (attrition) di Jaya Jaya Institut?**  
   Jaya Jaya Institut menghadapi masalah serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikannya. Penyebab dropout sangat beragam, mulai dari masalah akademik seperti kegagalan mata kuliah dan minimnya evaluasi, hingga faktor non-akademik seperti latar belakang keluarga, status ekonomi, dan usia saat pendaftaran. Namun, institusi belum memiliki sistem yang mampu menganalisis dan mengidentifikasi keterkaitan faktor-faktor ini secara menyeluruh dan berbasis data.

2. **Bagaimana institusi dapat mengembangkan strategi berbasis data untuk menurunkan dropout rate secara signifikan?**  
   Selama ini, strategi intervensi dilakukan secara umum dan reaktif, tanpa mempertimbangkan data historis siswa secara mendalam. Untuk meningkatkan efektivitas dan efisiensi intervensi, diperlukan sebuah pendekatan analitik yang mampu memetakan risiko dropout setiap siswa secara individual. Dengan demikian, pihak manajemen dan tenaga pendidik dapat melakukan upaya pencegahan secara lebih proaktif dan terarah.

3. **Apa pola atau indikator kunci yang dapat memprediksi dropout secara dini?**  
   Identifikasi dini terhadap siswa berisiko tinggi sangat penting untuk mencegah putus sekolah. Namun saat ini, Jaya Jaya Institut belum memiliki model prediktif atau indikator risiko yang teruji. Menemukan pola dropout melalui data akademik, evaluasi per semester, dan informasi sosiodemografis merupakan langkah awal yang krusial untuk menyusun sistem pemantauan berkelanjutan.

---

### Cakupan Proyek

Untuk menjawab permasalahan tersebut, proyek ini akan mencakup kegiatan-kegiatan berikut:

1. **Pengumpulan dan Integrasi Data Historis Siswa**  
   - Menggabungkan data dari berbagai sumber (nilai akademik, latar belakang demografis, status orang tua, evaluasi kurikuler, dan faktor eksternal seperti ekonomi makro).  
   - Pembersihan data (data cleansing) untuk menangani missing value, inkonsistensi, dan duplikasi.

2. **Eksplorasi dan Analisis Data**  
   - Melakukan analisis statistik deskriptif untuk memahami karakteristik siswa yang dropout dan yang lulus.  
   - Mengidentifikasi variabel yang memiliki korelasi kuat terhadap status dropout.

3. **Pengembangan Model Prediktif**  
   - Menggunakan pendekatan machine learning (misalnya logistic regression, decision tree, random forest, atau XGBoost) untuk memprediksi kemungkinan dropout.  
   - Menentukan fitur/variabel penting dalam prediksi berdasarkan hasil model.

4. **Evaluasi Model dan Validasi Hasil**  
   - Menggunakan metrik seperti akurasi, precision, recall, dan F1-score untuk mengukur performa model.  
   - Melakukan validasi silang (cross-validation) agar model tetap andal pada data baru.

5. **Rekomendasi Strategi Intervensi**  
   - Menyusun rekomendasi kebijakan dan strategi intervensi yang tepat berdasarkan output model.  
   - Mempersiapkan sistem pemantauan siswa berkelanjutan berbasis risiko.

## Data Understanding
### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv
Setup environment:
```
pip install joblib numpy pandas seaborn matplotlib sklearn
```
Berikut ini gambaran dari data yang tersedia:
| #  | Column                                         | Non-Null Count | Dtype    |
|----|-----------------------------------------------|----------------|----------|
| 1  | Marital_status                                 | 4424           | int64    |
| 2  | Application_mode                               | 4424           | int64    |
| 3  | Application_order                              | 4424           | int64    |
| 4  | Course                                         | 4424           | int64    |
| 5  | Daytime_evening_attendance                     | 4424           | int64    |
| 6  | Previous_qualification                         | 4424           | int64    |
| 7  | Previous_qualification_grade                   | 4424           | float64  |
| 8  | Nacionality                                    | 4424           | int64    |
| 9  | Mothers_qualification                          | 4424           | int64    |
| 10 | Fathers_qualification                          | 4424           | int64    |
| 11 | Mothers_occupation                             | 4424           | int64    |
| 12 | Fathers_occupation                             | 4424           | int64    |
| 13 | Admission_grade                                | 4424           | float64  |
| 14 | Displaced                                      | 4424           | int64    |
| 15 | Educational_special_needs                      | 4424           | int64    |
| 16 | Debtor                                         | 4424           | int64    |
| 17 | Tuition_fees_up_to_date                        | 4424           | int64    |
| 18 | Gender                                         | 4424           | int64    |
| 19 | Scholarship_holder                             | 4424           | int64    |
| 20 | Age_at_enrollment                              | 4424           | int64    |
| 21 | International                                  | 4424           | int64    |
| 22 | Curricular_units_1st_sem_credited              | 4424           | int64    |
| 23 | Curricular_units_1st_sem_enrolled              | 4424           | int64    |
| 24 | Curricular_units_1st_sem_evaluations           | 4424           | int64    |
| 25 | Curricular_units_1st_sem_approved              | 4424           | int64    |
| 26 | Curricular_units_1st_sem_grade                 | 4424           | float64  |
| 27 | Curricular_units_1st_sem_without_evaluations   | 4424           | int64    |
| 28 | Curricular_units_2nd_sem_credited              | 4424           | int64    |
| 29 | Curricular_units_2nd_sem_enrolled              | 4424           | int64    |
| 30 | Curricular_units_2nd_sem_evaluations           | 4424           | int64    |
| 31 | Curricular_units_2nd_sem_approved              | 4424           | int64    |
| 32 | Curricular_units_2nd_sem_grade                 | 4424           | float64  |
| 33 | Curricular_units_2nd_sem_without_evaluations   | 4424           | int64    |
| 34 | Unemployment_rate                              | 4424           | float64  |
| 35 | Inflation_rate                                 | 4424           | float64  |
| 36 | GDP                                            | 4424           | float64  |
| 37 | Status                                         | 4424           | object   |

Tidak terdapat missing values pada data. Hampir seluruh data sudah dalam bentuk numerik, hanya kolom Status yang berbentuk string, berikut distribusi data pada kolom Status:
| Status   | Count |
|----------|-------|
| Graduate | 2209  |
| Dropout  | 1421  |
| Enrolled | 794   |

### Exploratory Data Analysis
#### Univariate Data Analysis

Berikut ini adalah analisis univariate menggunakan histogram dari masing-masing kolom yang ada pada data:
![Univariate](https://github.com/user-attachments/assets/e0511e00-6b9c-4ef9-a94b-47c9ac1cb8fc)

Berdasarkan histogram yang ditampilkan, meskipun seluruh data telah berbentuk numerikal, sebenarnya terdapat sejumlah kolom yang merepresentasikan data kategorikal. Beberapa di antaranya adalah kolom biner yang hanya memiliki dua nilai, seperti Daytime_evening_attendance, Displaced, Educational_special_needs, Debtor, Tuition_fees_up_to_date, Gender, Scholarship_holder, dan International, yang masing-masing berisi nilai 0 dan 1. Nilai-nilai tersebut pada dasarnya merepresentasikan kondisi ya atau tidak, sehingga lebih tepat diperlakukan sebagai data kategorikal. 

Selain itu, terdapat pula kolom lain yang tampaknya telah melalui proses label encoding, seperti Marital_status, Application_mode, Course, Nationality, Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation, dan Previous_qualification. Kolom-kolom ini memiliki nilai integer diskrit dengan jumlah kategori yang terbatas, yang menunjukkan bahwa nilai numerik tersebut tidak mencerminkan nilai kuantitatif, melainkan kategori yang berbeda. Berikut ini detail deskripsi dari masing-masing variabel:

| Column name                                     | Description |
|------------------------------------------------|-------------|
| Marital status                                 | The marital status of the student. (Categorical) 1 – single, 2 – married, 3 – widower, 4 – divorced, 5 – facto union, 6 – legally separated |
| Application mode                               | The method of application used by the student. (Categorical) e.g., 1 - 1st phase - general contingent, 2 - Ordinance No. 612/93, ..., 57 - Change of institution/course (International) |
| Application order                              | The order in which the student applied. (Numerical, 0 = first choice; 9 = last choice) |
| Course                                         | The course taken by the student. (Categorical) e.g., 33 - Biofuel Production Technologies, ..., 9991 - Management (evening attendance) |
| Daytime/evening attendance                     | Whether the student attends classes during the day or in the evening. (Categorical) 1 – daytime, 0 - evening |
| Previous qualification                         | The qualification obtained before enrolling in higher education. (Categorical) e.g., 1 - Secondary education, ..., 43 - Higher Education - Master (2nd cycle) |
| Previous qualification (grade)                 | Grade of previous qualification (0 to 200) |
| Nacionality                                    | The nationality of the student. (Categorical) e.g., 1 - Portuguese, 2 - German, ..., 109 - Colombian |
| Mother's qualification                         | The qualification of the student's mother. (Categorical) e.g., 1 - Secondary Education, ..., 44 - Higher Education - Doctorate (3rd cycle) |
| Father's qualification                         | The qualification of the student's father. (Categorical) e.g., 1 - Secondary Education, ..., 44 - Higher Education - Doctorate (3rd cycle) |
| Mother's occupation                            | The occupation of the student's mother. (Categorical) e.g., 0 - Student, 1 - Executives, ..., 194 - Meal preparation assistants |
| Father's occupation                            | The occupation of the student's father. (Categorical) e.g., 0 - Student, 1 - Executives, ..., 195 - Street vendors and service providers |
| Admission grade                                | Admission grade (0 to 200) |
| Displaced                                      | Whether the student is a displaced person. (Categorical) 1 – yes, 0 – no |
| Educational special needs                      | Whether the student has special educational needs. (Categorical) 1 – yes, 0 – no |
| Debtor                                         | Whether the student is a debtor. (Categorical) 1 – yes, 0 – no |
| Tuition fees up to date                        | Whether the student's tuition fees are up to date. (Categorical) 1 – yes, 0 – no |
| Gender                                         | The gender of the student. (Categorical) 1 – male, 0 – female |
| Scholarship holder                             | Whether the student is a scholarship holder. (Categorical) 1 – yes, 0 – no |
| Age at enrollment                              | Age of the student at time of enrollment (Numerical) |
| International                                  | Whether the student is an international student. (Categorical) 1 – yes, 0 – no |
| Curricular units 1st sem (credited)            | Number of first semester curricular units credited. (Numerical) |
| Curricular units 1st sem (enrolled)            | Number of first semester curricular units enrolled. (Numerical) |
| Curricular units 1st sem (evaluations)         | Number of first semester curricular units evaluated. (Numerical) |
| Curricular units 1st sem (approved)            | Number of first semester curricular units approved. (Numerical) |
| Curricular units 1st sem (grade)               | Average grade in first semester curricular units. (Float, 0–20) |
| Curricular units 1st sem (without evaluations) | Number of first semester curricular units without evaluations. (Numerical) |
| Curricular units 2nd sem (credited)            | Number of second semester curricular units credited. (Numerical) |
| Curricular units 2nd sem (enrolled)            | Number of second semester curricular units enrolled. (Numerical) |
| Curricular units 2nd sem (evaluations)         | Number of second semester curricular units evaluated. (Numerical) |
| Curricular units 2nd sem (approved)            | Number of second semester curricular units approved. (Numerical) |
| Curricular units 2nd sem (grade)               | Average grade in second semester curricular units. (Float, 0–20) |
| Curricular units 2nd sem (without evaluations) | Number of second semester curricular units without evaluations. (Numerical) |
| Unemployment rate                              | National unemployment rate at time of enrollment (%). (Float) |
| Inflation rate                                 | National inflation rate at time of enrollment (%). (Float) |
| GDP                                            | Gross Domestic Product per capita at time of enrollment (in thousands of currency units). (Float) |
| Status                                         | Final academic status of the student. (Categorical: Enrolled, Graduate, Dropout) |

#### Bivariate Data Analysis

Berikut ini analisis bivariate antara masing-masing kolom dengan kolom Status:
![Bivariate Categorical](https://github.com/user-attachments/assets/00c0c269-3a71-4b67-90e7-e34362c6eb38)

Berdasarkan bar chart di atas, terlihat bahwa sebagian besar mahasiswa yang mengalami dropout cenderung memiliki status sebagai debtor, tidak membayar biaya pendidikan secara tepat waktu (tuition fees not up to date), dan bukan penerima beasiswa (non-scholarship holder). Pola ini menunjukkan adanya keterkaitan yang cukup kuat antara kondisi finansial mahasiswa dengan risiko mereka untuk tidak menyelesaikan studi. Mahasiswa yang mengalami kesulitan ekonomi tampaknya menghadapi hambatan tambahan yang dapat berdampak pada keberlangsungan studi mereka. Oleh karena itu, dapat disimpulkan bahwa faktor finansial merupakan salah satu penyebab utama yang berkontribusi terhadap angka dropout dalam populasi ini. Temuan ini menunjukkan pentingnya intervensi seperti dukungan beasiswa atau kebijakan pembayaran yang fleksibel untuk membantu mempertahankan mahasiswa yang rentan secara ekonomi agar tetap melanjutkan pendidikan mereka hingga lulus.

Berikut ini analisis bivariate antara kolom lainnya dengan kolom Status:
![Bivariate Numerical](https://github.com/user-attachments/assets/90aaad1d-f9a2-4866-8575-8f6a890b7681)

Berdasarkan box plot yang ditampilkan, terdapat pola yang cukup jelas antara status kelulusan mahasiswa dengan usia saat pertama kali mendaftar (age at enrollment) serta kinerja akademik pada semester pertama dan kedua. Mahasiswa yang mengalami dropout cenderung memiliki rata-rata usia pendaftaran yang lebih tinggi dibandingkan dengan mereka yang berhasil lulus. Hal ini dapat mengindikasikan bahwa mahasiswa yang lebih tua menghadapi tantangan tambahan dalam menyelesaikan studi, seperti tanggung jawab pekerjaan atau keluarga. Selain itu, mahasiswa yang dropout juga menunjukkan nilai akademik yang lebih rendah, baik pada semester pertama maupun semester kedua, dibandingkan dengan mahasiswa yang graduate. Hal ini terlihat dari lebih rendahnya jumlah mata kuliah yang disetujui (approved), serta skor nilai (grade) yang lebih rendah. Dengan demikian, selain faktor usia, performa akademik yang kurang baik juga menjadi indikator signifikan terhadap kemungkinan mahasiswa tidak menyelesaikan studi mereka. Temuan ini menegaskan pentingnya dukungan akademik dan pembinaan yang lebih intensif, terutama bagi mahasiswa dengan performa awal yang kurang memuaskan.

#### Multivariate Data Analysis

Berikut ini analisis multivariate antara kolom dengan menggunakan heatmap:

![Multivariate](https://github.com/user-attachments/assets/a25387b6-ec12-4f88-91ce-1cf19c7df012)

Berdasarkan heatmap korelasi yang ditampilkan, terlihat bahwa beberapa variabel memiliki hubungan yang cukup kuat satu sama lain, menunjukkan adanya kemungkinan multikolinearitas. Misalnya, usia saat mendaftar (age at enrollment) berkorelasi dengan status pernikahan (marital status) dan mode pendaftaran (application mode), yang bisa mengindikasikan bahwa mahasiswa yang lebih tua cenderung memiliki status pernikahan tertentu atau memilih mode pendaftaran tertentu. Selain itu, terdapat korelasi yang tinggi antara nilai masuk universitas (admission grade) dan nilai kualifikasi sebelumnya (previous qualification grade), yang menunjukkan bahwa kinerja akademik sebelumnya cukup konsisten.

Korelasi yang signifikan juga terlihat antara latar belakang pendidikan orang tua; kualifikasi ayah dan ibu menunjukkan hubungan yang kuat, begitu pula dengan jenis pekerjaan ayah dan ibu, mencerminkan kesamaan tingkat pendidikan dan bidang pekerjaan dalam satu rumah tangga. Yang paling mencolok adalah hubungan antara variabel akademik seperti jumlah mata kuliah yang diambil, diikuti evaluasinya, jumlah yang disetujui, serta nilai pada semester pertama dan kedua. Variabel-variabel ini menunjukkan korelasi yang sangat kuat satu sama lain, mengindikasikan bahwa performa akademik mahasiswa pada satu semester sangat berkaitan dengan performa pada semester lainnya.

Multikolinearitas ini penting untuk diperhatikan dalam pemodelan prediktif, karena dapat memengaruhi stabilitas dan interpretasi dari koefisien model regresi. Perlu dilakukan seleksi fitur atau penerapan teknik seperti PCA untuk mengatasinya.

## Data Preparation / Preprocessing

Pada tahap data preparation, dilakukan pemisahan data mahasiswa yang masih berstatus aktif (Enrolled) ke dalam file terpisah dan data tersebut tidak disertakan dalam analisis lebih lanjut. Fokus analisis hanya ditujukan pada mahasiswa yang telah lulus (Graduate) atau yang mengalami putus studi (Dropout). Selanjutnya, status mahasiswa dikonversi menjadi variabel biner yang merepresentasikan apakah seorang mahasiswa mengalami putus studi atau tidak, di mana nilai 1 menunjukkan status Dropout dan nilai 0 menunjukkan status Graduate. Setelah proses transformasi label selesai, variabel status awal dihapus karena sudah tidak diperlukan lagi. Untuk keperluan pelatihan dan evaluasi model, data kemudian dibagi menjadi dua bagian, yaitu data pelatihan dan data pengujian, dengan proporsi 80:20 secara acak namun terkontrol untuk memastikan replikasi hasil yang konsisten. Tahapan ini memastikan bahwa data yang digunakan dalam proses modeling telah disaring dan disiapkan secara optimal.
```
df[df['Status'] == 'Enrolled'].to_csv("enrolled_students.csv", index=False)
df = df[df['Status'] != 'Enrolled']
df['Dropout'] = (df['Status'] == 'Dropout').astype('int')
df.drop(columns=['Status'], inplace=True)

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
```

### Undersampling
Berikut ini adalah hasil sebaran nilai dropout pada data pelatihan:
| Dropout | Count |
|---------|-------|
| 0       | 1760  |
| 1       | 1144  |

Untuk mengatasi ketidakseimbangan antara dua kelas tersebut, yaitu mahasiswa yang tidak dropout dan yang dropout, maka dilakukan beberapa langkah penyesuaian. Data pelatihan awal dipisahkan berdasarkan kelas, kemudian dilakukan undersampling pada kelas mayoritas (mahasiswa yang tidak dropout) sehingga jumlahnya setara dengan kelas minoritas. Setelah itu, kedua kelompok data digabung kembali dan diacak ulang guna membentuk data pelatihan yang seimbang.

### Scaling
Tahap selanjutnya adalah memisahkan fitur dari label target baik pada data pelatihan maupun data pengujian. Seluruh fitur numerik kemudian dinormalisasi menggunakan metode Min-Max Scaler, dengan tujuan mengubah skala nilai setiap fitur ke rentang 0 hingga 1. Skaler untuk masing-masing fitur disimpan secara terpisah agar dapat digunakan kembali saat proses prediksi pada data baru. Hasil dari tahapan ini adalah data pelatihan dan pengujian yang telah seimbang dan terstandardisasi, siap untuk digunakan dalam pelatihan model prediktif.

### Principal Component Analysis (PCA)
Berdasarkan hasil heatmap sebelumnya, teridentifikasi adanya multikolinearitas antar kolom. Oleh karena itu, dilakukan analisis Principal Component Analysis (PCA) untuk mereduksi dimensi dan mengatasi multikolinearitas tersebut. Sebelum PCA diterapkan, kolom-kolom dibagi menjadi beberapa kelompok berdasarkan tingkat linearitas antar variabelnya. Setelah itu, dilakukan perhitungan variance dari masing-masing kelompok variabel.

```
pca_academic_columns = ['Course', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled', 
                        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved', 
                        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
                        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled', 
                        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved', 
                        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations']
```
![pca academic](https://github.com/user-attachments/assets/6ac5eacf-8ef1-402f-a53b-82e20fe8f0e6)

Pada kelompok variabel akademik, analisis PCA menunjukkan bahwa empat principal components pertama sudah mampu menjelaskan lebih dari 90% total variasi dari 13 variabel yang diukur. Hal ini mengindikasikan bahwa terdapat hubungan yang kuat atau korelasi tinggi antar variabel akademik, seperti jumlah mata kuliah yang diambil, jumlah evaluasi, nilai yang diperoleh, dan tingkat kelulusan di masing-masing semester. Dengan demikian, informasi yang terkandung dalam variabel-variabel ini sebagian besar tumpang tindih dan dapat direpresentasikan secara efisien dalam bentuk empat komponen utama. Reduksi dimensi ini tidak hanya menyederhanakan struktur data tetapi juga meningkatkan efisiensi dalam analisis selanjutnya, seperti dalam pembangunan model prediktif. Selain itu, penggunaan komponen utama ini membantu menghindari masalah multikolinearitas yang dapat mempengaruhi hasil analisis statistik atau pembelajaran mesin.

```
pca_parents_columns = ['Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation']
```
![pca parents](https://github.com/user-attachments/assets/8462d89b-2cda-41ea-89de-ba02ca3392ff)

Untuk variabel latar belakang orang tua, hasil PCA menunjukkan bahwa dua principal components saja sudah cukup untuk menjelaskan lebih dari 90% variasi dari empat variabel yang terkait, yaitu pendidikan dan pekerjaan ayah serta ibu. Hasil ini menunjukkan bahwa variabel-variabel tersebut memiliki pola keterkaitan yang sangat erat dan saling merepresentasikan satu sama lain. Misalnya, tingkat pendidikan orang tua kemungkinan berkaitan langsung dengan jenis pekerjaan yang dijalani. Oleh karena itu, dua komponen utama yang terbentuk dari proses PCA dapat dianggap sebagai representasi ringkas dari status sosial ekonomi keluarga mahasiswa. Komponen ini penting untuk mempertimbangkan pengaruh faktor keluarga terhadap prestasi akademik mahasiswa maupun kebijakan pemberian dukungan finansial dan akademik.

```
pca_background_columns = ['Marital_status', 'Application_mode', 'Application_order',
                          'Previous_qualification', 'Previous_qualification_grade',
                          'Admission_grade', 'Age_at_enrollment']
```
![pca background](https://github.com/user-attachments/assets/ddd01138-80d5-4e8d-bfcf-fc563aca55da)

Sedangkan pada variabel latar belakang mahasiswa, diperlukan lima principal components untuk dapat menjelaskan lebih dari 90% variasi dari tujuh variabel yang meliputi status pernikahan, jalur pendaftaran, urutan pilihan program studi, kualifikasi pendidikan sebelumnya, nilai masuk, serta usia saat mendaftar. Ini menunjukkan bahwa hubungan antar variabel pada kelompok ini tidak sekuat dua kelompok sebelumnya, sehingga informasi tersebar lebih merata di antara variabel-variabel tersebut. Meski demikian, PCA tetap berhasil mereduksi dimensi dari tujuh menjadi lima tanpa kehilangan banyak informasi penting. Komponen-komponen ini dapat dipandang sebagai representasi dari faktor demografis dan akademik awal yang membentuk profil unik tiap mahasiswa. Informasi ini dapat dimanfaatkan untuk segmentasi mahasiswa, identifikasi kelompok berisiko putus studi, maupun pengembangan strategi intervensi berbasis data.

Hasil akhir dari data train setelah dilakukan praproses, termasuk reduksi dimensi menggunakan PCA, terdiri dari 23 variabel numerik dengan jumlah total 2.288 observasi. Tabel berikut merangkum masing-masing kolom beserta tipe datanya dan kategorisasi berdasarkan peran atau sumber variabel:

| #   | Column                        | Non-Null Count | Dtype   |
|-----|-------------------------------|----------------|---------|
| 1   | Daytime_evening_attendance    | 2288           | float64 |
| 2   | Nacionality                   | 2288           | float64 |
| 3   | Displaced                     | 2288           | float64 |
| 4   | Educational_special_needs     | 2288           | float64 |
| 5   | Debtor                        | 2288           | float64 |
| 6   | Tuition_fees_up_to_date       | 2288           | float64 |
| 7   | Gender                        | 2288           | float64 |
| 8   | Scholarship_holder            | 2288           | float64 |
| 9   | International                 | 2288           | float64 |
| 10  | Unemployment_rate             | 2288           | float64 |
| 11  | Inflation_rate                | 2288           | float64 |
| 12  | GDP                           | 2288           | float64 |
| 13  | pca_academic_1                | 2288           | float64 |
| 14  | pca_academic_2                | 2288           | float64 |
| 15  | pca_academic_3                | 2288           | float64 |
| 16  | pca_academic_4                | 2288           | float64 |
| 17  | pca_parents_1                 | 2288           | float64 |
| 18  | pca_parents_2                 | 2288           | float64 |
| 19  | pca_background_1              | 2288           | float64 |
| 20  | pca_background_2              | 2288           | float64 |
| 21  | pca_background_3              | 2288           | float64 |
| 22  | pca_background_4              | 2288           | float64 |
| 23  | pca_background_5              | 2288           | float64 |

Struktur data ini menunjukkan bahwa sebagian besar variabel awal telah dikompresi menjadi sejumlah principal components untuk mengurangi kompleksitas, menjaga informasi penting, dan meminimalkan multikolinearitas. Data ini telah siap untuk digunakan dalam model pembelajaran mesin atau analisis prediktif lainnya.

## Modelling

Evaluasi terhadap tiga model klasifikasi yang terdiri dari Decision Tree, Random Forest, dan Gradient Boosting menunjukkan perbedaan yang signifikan dalam hal akurasi dan keseimbangan performa antar kelas. Decision Tree memiliki akurasi sebesar 80%, dengan nilai f1-score yang cukup rendah untuk kelas 1 (0.74), mengindikasikan bahwa model ini kurang optimal dalam mengenali kategori tersebut. Sementara itu, Random Forest mencatat performa terbaik dengan akurasi 89%, serta nilai precision dan recall yang seimbang untuk kedua kelas, menjadikannya model yang kuat dan andal. Gradient Boosting juga memberikan hasil yang kompetitif, dengan akurasi 88% dan f1-score kelas 1 sebesar 0.85. Menariknya, Gradient Boosting menunjukkan recall tertinggi untuk kelas 1 (0.88), menjadikannya pilihan tepat untuk skenario yang memprioritaskan deteksi kasus kelas minoritas secara akurat. Secara keseluruhan, Random Forest unggul sebagai model paling seimbang, sementara Gradient Boosting layak dipertimbangkan untuk fokus pada sensitivitas terhadap kelas 1.
| Model              | Class | Precision | Recall | F1-score | Support |
|--------------------|-------|-----------|--------|----------|---------|
| Decision Tree      | 0     | 0.84      | 0.83   | 0.83     | 449     |
|                    | 1     | 0.73      | 0.75   | 0.74     | 277     |
|                    | Avg (macro) | 0.79  | 0.79   | 0.79     | 726     |
|                    | Avg (weighted) | 0.80 | 0.80   | 0.80     | 726     |
|                    | Accuracy |         |        | **0.80** |         |
|--------------------|-------|-----------|--------|----------|---------|
| Random Forest      | 0     | 0.90      | 0.93   | 0.91     | 449     |
|                    | 1     | 0.88      | 0.83   | 0.85     | 277     |
|                    | Avg (macro) | 0.89  | 0.88   | 0.88     | 726     |
|                    | Avg (weighted) | 0.89 | 0.89   | 0.89     | 726     |
|                    | Accuracy |         |        | **0.89** |         |
|--------------------|-------|-----------|--------|----------|---------|
| Gradient Boosting  | 0     | 0.92      | 0.88   | 0.90     | 449     |
|                    | 1     | 0.81      | 0.88   | 0.85     | 277     |
|                    | Avg (macro) | 0.87  | 0.88   | 0.87     | 726     |
|                    | Avg (weighted) | 0.88 | 0.88   | 0.88     | 726     |
|                    | Accuracy |         |        | **0.88** |         |


## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
