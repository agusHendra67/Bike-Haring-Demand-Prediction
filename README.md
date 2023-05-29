# Bike-Sharing-Demand-Prediction

### **Business Problem Understanding**

**Context**

Sistem bike sharing adalah sarana penyewaan sepeda dimana proses perekrutan anggota, persewaan, dan pengembalian sepeda dilakukan secara otomatis melalui jaringan lokasi kios di seluruh kota. Dengan menggunakan sistem ini, orang dapat menyewa sepeda dari satu lokasi dan mengembalikannya ke tempat lain sesuai kebutuhan. Melansir dari halaman web [https://en.wikipedia.org/wiki/Capital_Bikeshare], Capital Bikeshare mulai beoperasi dari tahun 2010, dan hingga saat ini, januari 2023, sudah memiliki 700+ kios dan lebih dari 5400 unit sepeda yang merupakan sistem penyewaan sepeda terbesar di amerika serikat hingga 2013 sebelum Citi Bike kota New Yoek City ada di tahun 2013.

Data yang dihasilkan oleh sistem ini menarik perhatian para peneliti karena durasi perjalanan, lokasi keberangkatan, lokasi kedatangan, dan waktu yang telah berlalu dicatat secara eksplisit. Oleh karena itu, sistem bike sharing berfungsi sebagai jaringan sensor yang dapat digunakan untuk mempelajari mobilitas di suatu kota.  Dalam model bisnis capital bikeshare membebaskan penyewaan sepeda di jam/waktu berapapun (denga/ sistem sewa) dan terdapat dua jenis keanggotaan yaitu pengguna terdaftar (registered users) dan pengguna kasual (casual users). Ada banyak faktor yang mempengaruhi seseorang akan menyewa sepeda, salah satunya waktu (cuaca, jam, season dll). Dengan bertambahnya jumlah pengguna yang artinya adanya peningkatan permintaan sepeda, tentu saja bertambahnya jumlah profit yang didapatkan (baik pengguna terdaftar maupun kasual).

**Problem Statement**

Salah satu tantangan terbesar bagi perusahaan Capital Bikeshare adalah pemecahan masalah untuk dapat memiliki model bisnis yang menguntungkan secara finansial dan juga mengoptimalkan sistem bike-sharing untuk memenuhi permintaan yang berfluktuasi dan meminimalkan biaya operasional.

Mengingat banyak faktor yang mempengaruhi jumlah sepeda yang akan disewa dari sistem bike-sharing pada waktu tertentu. Pernyataan masalah permintaan bike-sharing adalah memprediksi jumlah sepeda yang akan disewa dari sistem bike-sharing pada waktu tertentu berdasarkan faktor-faktor seperti cuaca, hari dalam seminggu, dan waktu. 

**Goals**

Berdasarkan permasalahan tersebut, Capital Bikeshare tentu perlu memiliki "tool" atau lebih tepatnya sebuah model prediktif yang dapat secara akurat **memperkirakan permintaan penyewaan sepeda (jumlah pengguna sepeda) untuk mengoptimalkan alokasi sepeda dan meningkatkan efisiensi sistem berbagi sepeda secara keseluruhan**. Adanya perbedaan pada berbagai fitur yang terdapat pada suatu waktu, seperti cuaca, hari dalam seminggu, tipe hari (weekday atau weekend), temperatur, humiditas dapat menambah keakuratan prediksi jumlah pengguna sepeda, yang mana dapat mendatangkan profit bagi Capital Bikeshare, dan juga tentunya memnuhi permintaan penyewa sepeda dengan tepat dalam cost yang seminimal mungkin.

**Analytic Approach**

Jadi dari penjabaran di atas, kita akan menganalisis data untuk dapat menemukan pola dari fitur-fitur yang ada, yang membedakan hari tertentu dengan yang lainnya dalam hal jumlah total pengguna sepeda (baik yang registered maupun casual users). 

Selanjutnya, kita akan membangun suatu model regresi yang akan membantu perusahaan untuk dapat menyediakan 'tool' atau model prediktif yang mampu prediksi jumlah sepeda yang akan disewa atau jumlah pengguna di waktu tertentu. Disini kita akan melakukan eksperimen dengan beberapa algoritma model regresi yang sering digunakan seperti Linear Regression, KNN, SGD, Random Forest, XGB, dan LGBM. Dimana kita akan memilih satu model (atau gabungan dari beberapa model) untuk membuat tool tersebut yang sesuai dengan data dari Capital Bikeshare.

**Metric Evaluation**

Evaluasi metrik yang akan digunakan adalah RMSE, MAE, dan sMAPE, di mana RMSE adalah nilai rataan akar kuadrat dari error, MAE adalah rataan nilai absolut dari error, sedangkan sMAPE adalah rataan persentase error yang dihasilkan oleh model regresi (catatan : disini digunakan sMAPE bukan MAPE dikarenakan adanya nilai 0 pada data jumlah pengguna). Semakin kecil nilai RMSE, MAE, dan sMAPE yang dihasilkan, berarti model semakin akurat dalam memprediksi jumlah sepeda/ jumlah pengguna sesuai dengan limitasi fitur yang digunakan. 

Selain itu disini saya juga akan menggunakan RMSLE (Root Mean Squared Log Error) yang dimana metric ini hanya mempertimbangkan kesalahan relatif antara antara nilai prediksi dan nilai aktual. RMSLE juga memiliki sifat menimbulkan penalti/error yang lebih besar untuk estimasi yang terlalu rendah (underestimated) dari variabel aktual daripada estimasi yang lebih tinggi (overestimated). Sedangkan sMAPE bisa digunakan untuk mengecek seberapa jauh sebuah model dapat menghandel nilai overestimated prediction, karena sMPAE sensitif dengan nilai prediksi yang lebih tinggi dari aktual, sedangkan RMSLE kebalikannya.

****

### **Data Understanding**

**Dataset Information**

- Dataset merupakan data penyewaan sepeda dari Capital Bikeshare pada tahun 2011 dan 2012.
- Setiap baris data merepresentasikan informasi terkait waktu dan lainnya.

**Attributes Information**

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| dteday | Object | Date |
| hum | Float | normalized humidity.The values are divided into 100 (max)  |
| weathersit | Integer | weather. -	1: Clear, Few clouds, Partly cloudy, Partly cloudy, 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist, 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds, 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog |
| holiday | Integer | holiday or not |
| season | Integer | season (1: winter, 2: spring, 3: summer, 4: fall) |
| atemp | Float | Normalized feeling temperature in Celsius. The values are derived via (t-tmin)/(tmax-tmin), tmin=-16, t_max=+50 (only in hourly scale) |
| temp | Float | normalized temperature in Celsius. The values are derived via (t-tmin)/(tmax-tmin), tmin=-8, t_max=+39 (only in hourly scale) |
| hr | Integer | Hours of day (0 to 23) |
| casual | Integer| count of casual users |
| registered | Integer | count of registered users |
| cnt | Integer | count of total rental bikes including both casual and registered |

### Data Preprocessing and Modeling

📑 **Steps involved**

Data Preprocessing : Mengecek nilai kosong (missing value), drop data duplikat, ubah format

Feature Extraction/creation : Membuat fitur baru seperti day, month, year, week_of_year, quarter dari Date column .

Feature encoding : Encoding data kategori

Feature Scaling : , scaling menggunakan Standard scaler untuk data numerik

Implementasi beberapa Model Regresi

Hyperparameter tuning

Comparison of models
-----------------------------------------------------
### Algorithm used

1. Linear Regression
2. KNN Regressor
3. SGD Regressor
4. SVR
5. Lasso
6. DecisionTree Regressor
7. RandomForest Regressor
8. XGBoost regressor
9. LightGBM (LGBM) regressor

Result
-----------------------------------------------------

![image](result image.png)
