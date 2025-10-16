Hoax Detector Project Overview
Aplikasi ini bertujuan untuk mendeteksi apakah sebuah berita itu hoax atau tidak berdasarkan judul dan narasi yang diberikan. Proyek ini terdiri dari:
1.	Frontend (ReactJS + TailwindCSS): Antarmuka pengguna tempat pengguna dapat memasukkan judul dan narasi berita untuk memprediksi apakah konten tersebut hoax atau tidak dan didalamnya terdapat halaman untuk login, register, log out, home, history, dan profile.
2.	Backend (Python + Flask): API yang memproses data yang dimasukkan (username, password, data predict), menjalankan model untuk prediksi (model Logistic Regression), dan mengembalikan hasilnya.
3.	Server (Node.js + Express): Menyediakan server untuk menangani login, registrasi, dan pengelolaan pengguna.
4.	Model Machine Learning: Model ini dilatih untuk mengklasifikasikan berita menjadi "Hoax" atau "Not Hoax" berdasarkan teks yang diberikan. Model dilatih menggunakan dataset yang didapatkan pada kaggel yaitu dataset yang berjudul Indonesia False News(Hoax) Dataset.
________________________________________
Cara Menginstal Aplikasi
1. Frontend (ReactJS + TailwindCSS)
1.	Clone atau Unduh Proyek ke komputer lokal Anda.
2.	Instalasi dependensi untuk frontend:
cd /frontend/src/
npm install
3.	Jalankan aplikasi React:
npm start
Aplikasi ini akan berjalan di http://localhost:3000.
2. Backend (Python + Flask)
1.	Instalasi dependensi Python. Pastikan Anda sudah menginstal Python 3.x. Kemudian, instal dependensi yang diperlukan:
cd backend
2.	Jalankan server Flask:
pip install -r requirements.txt
python app.py
Server Flask akan berjalan di http://localhost:5001.
3. Server (Node.js + Express)
1.	Instalasi dependensi untuk server:
cd /frontend/src/api
npm install
2.	Jalankan server Node.js:
node server.js
Server Node.js akan berjalan di http://localhost:5000.
________________________________________
Cara Menggunakan Aplikasi
Frontend Penggunaan
1.	Login/Registrasi: Saat aplikasi pertama kali diakses, pengguna dapat melakukan registrasi dan login menggunakan LoginPage.
2.	Masukkan Berita untuk Prediksi:
o	Pengguna dapat memasukkan judul (judul) dan narasi (narasi) berita.
o	Setelah memasukkan berita, pengguna dapat mengklik "Predict" untuk mengirimkan data.
o	Sistem akan menampilkan apakah berita tersebut Hoax atau Not Hoax.
3.	History: Pengguna dapat melihat riwayat prediksi yang telah dilakukan melalui halaman HistoryPage.
Backend Penggunaan
1.	Route Login:
o	POST /login: Menerima username dan password, mengembalikan respon sukses atau gagal.
2.	Route Registrasi:
o	POST /register: Menerima username dan password, dan mendaftarkan pengguna jika username belum terdaftar.
3.	Route Prediksi:
o	POST /predict: Menerima input judul dan narasi.
o	Backend menggunakan model machine learning (model_logreg.pkl) dan vectorizer TF-IDF (tfidf_vectorizer.pkl) untuk memprediksi apakah berita tersebut hoax atau tidak.

Server (Node.js + Express) Penggunaan
1.	Route Registrasi Pengguna:
o	POST /register: Menyimpan informasi pengguna baru di file users.json. Memeriksa apakah pengguna sudah terdaftar sebelum mendaftar pengguna baru.
2.	Route Login Pengguna:
o	POST /login: Mengautentikasi pengguna berdasarkan username dan password, kemudian mengembalikan respon login yang sesuai.
________________________________________
Cara Kerja Aplikasi
1.	Frontend (ReactJS):
o	React menangani antarmuka pengguna, memungkinkan pengguna untuk berinteraksi dengan aplikasi dan melakukan prediksi.
o	Aplikasi frontend berkomunikasi dengan backend Flask menggunakan axios untuk permintaan HTTP.
2.	Backend (Flask):
o	File app.py berisi route API yang memproses input teks, membersihkan dan memvectorisasikan teks, kemudian menjalankan model untuk memprediksi apakah berita tersebut hoax atau tidak.
o	Backend berjalan di port 5001, sementara frontend React berkomunikasi dengannya di port 3000.
3.	Server (Node.js + Express):
o	server.js menangani route untuk login dan registrasi pengguna.
o	Menggunakan users.json untuk menyimpan data pengguna yang terdaftar.
o	Server ini berjalan di port 5000 dan digunakan oleh frontend untuk otentikasi pengguna.



